#!/usr/bin/env python3
"""
Generate a Markdown vulnerability page from a Vulnerability-Lookup search.

Default query mirrors:

https://vulnerability.circl.lu/search?ft_q=&vendor=misp&product=&assigner=&sort_sources%5B%5D=cvelistv5&sort_sources%5B%5D=gna-1&date_sort=published&sort_order=desc&cvss_min=&cvss_max=

The script deliberately uses the web search endpoint to obtain the exact set
of vulnerability IDs selected by the UI, then fetches each full record from
/api/vulnerability/<ID>. This avoids relying on the reduced vendor/product
search representation when fields such as affected products/CPEs are needed.

Dependencies:
    pip install requests beautifulsoup4

Example:
    python3 vl_markdown.py -o misp-vulnerabilities.md

Custom query:
    python3 vl_markdown.py \
        --vendor misp \
        --source cvelistv5 \
        --source gna-1 \
        --sort published \
        --order desc \
        -o misp-vulnerabilities.md
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import time
from collections.abc import Iterable
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlencode, urljoin

import requests
from bs4 import BeautifulSoup


DEFAULT_BASE_URL = "https://vulnerability.circl.lu"
DEFAULT_TIMEOUT = 30
DEFAULT_DELAY = 0.5
DEFAULT_MAX_RETRIES = 8
DEFAULT_BACKOFF = 2.0
USER_AGENT = "vl-markdown-export/1.0 (+https://vulnerability.circl.lu/)"

VULN_ID_RE = re.compile(
    r"^(?:CVE|GCVE|GHSA|EUVD|PYSEC|GSD|VAR|VARIoT|CERTFR|JVNDB|OSV)-",
    re.IGNORECASE,
)

CPE_RE = re.compile(r"^cpe:(?:2\.3:|/)", re.IGNORECASE)
CVSS_VECTOR_RE = re.compile(r"^CVSS:[234]\.[01]/", re.IGNORECASE)


CVE_ID_RE = re.compile(r"\bCVE-\d{4}-\d{4,}\b", re.IGNORECASE)
GCVE_ID_RE = re.compile(r"\bGCVE-\d+-\d{4}-\d+\b", re.IGNORECASE)


def extract_alias_ids(record: dict[str, Any], vuln_id: str = "") -> list[str]:
    """Extract explicit vulnerability aliases without scanning free-form prose.

    This intentionally limits itself to identifier/alias-like fields so that a
    mere reference to another CVE in a description does not cause two distinct
    vulnerabilities to be merged.
    """
    aliases: list[str] = []

    def add(value: Any) -> None:
        if isinstance(value, str):
            for match in CVE_ID_RE.findall(value):
                aliases.append(match.upper())
            for match in GCVE_ID_RE.findall(value):
                aliases.append(match.upper())
        elif isinstance(value, dict):
            for v in value.values():
                add(v)
        elif isinstance(value, (list, tuple, set)):
            for v in value:
                add(v)

    # Top-level and common structured alias fields.
    for key in (
        "aliases", "alias", "related", "relatedVulnerabilities",
        "cve", "cveId", "cve_id", "gcve", "gcveId", "gcve_id",
        "vulnId", "vulnerability_id",
    ):
        if key in record:
            add(record.get(key))

    metadata = record.get("cveMetadata")
    if isinstance(metadata, dict):
        for key in ("cveId", "aliases", "related"):
            add(metadata.get(key))

    # GCVE-0 is the compatibility namespace mapping directly to CVE.
    all_known = [vuln_id.upper()] + aliases
    for identifier in list(all_known):
        m = re.fullmatch(r"GCVE-0-(\d{4})-(\d+)", identifier, re.IGNORECASE)
        if m:
            aliases.append(f"CVE-{m.group(1)}-{m.group(2)}")

    return unique([a.upper() for a in aliases if a])


def deduplicate_records(
    records: list[tuple[str, dict[str, Any]]],
) -> list[tuple[str, dict[str, Any], list[str]]]:
    """Collapse records that explicitly map to the same CVE.

    CVE is preferred as the displayed identifier when both a CVE and a GCVE
    representation are present. GCVE identifiers are retained as aliases in
    the Markdown output. Records without an explicit shared CVE mapping remain
    separate.
    """
    groups: dict[str, list[tuple[str, dict[str, Any]]]] = {}
    order: list[str] = []

    for vuln_id, record in records:
        vid = vuln_id.upper()
        aliases = extract_alias_ids(record, vid)
        cve_ids = [a for a in aliases if a.startswith("CVE-")]
        if vid.startswith("CVE-"):
            cve_ids.insert(0, vid)

        # Only deduplicate when there is an explicit/common CVE identity.
        key = cve_ids[0] if cve_ids else vid
        if key not in groups:
            groups[key] = []
            order.append(key)
        groups[key].append((vid, record))

    result: list[tuple[str, dict[str, Any], list[str]]] = []
    for key in order:
        entries = groups[key]

        # Prefer the actual CVE record for display. Otherwise keep the first
        # record returned by the search, preserving the source ordering.
        chosen = next((entry for entry in entries if entry[0] == key), entries[0])
        display_id, display_record = chosen

        aliases: list[str] = []
        for entry_id, entry_record in entries:
            if entry_id != display_id:
                aliases.append(entry_id)
            for alias in extract_alias_ids(entry_record, entry_id):
                if alias != display_id:
                    aliases.append(alias)

        result.append((display_id, display_record, unique(aliases)))

    return result


def eprint(*args: Any, **kwargs: Any) -> None:
    print(*args, file=sys.stderr, **kwargs)


def md_escape(text: Any) -> str:
    """Escape text for ordinary Markdown prose/table cells."""
    if text is None:
        return ""
    value = str(text)
    value = value.replace("\\", "\\\\")
    value = value.replace("|", "\\|")
    value = value.replace("\r\n", "\n").replace("\r", "\n")
    return value.strip()


def md_inline_code(text: Any) -> str:
    value = str(text).strip()
    ticks = "`"
    if "`" in value:
        ticks = "``"
    return f"{ticks}{value}{ticks}"


def flatten_strings(value: Any) -> list[str]:
    """Collect scalar strings recursively, preserving order and uniqueness."""
    found: list[str] = []
    seen: set[str] = set()

    def walk(obj: Any) -> None:
        if isinstance(obj, str):
            s = obj.strip()
            if s and s not in seen:
                seen.add(s)
                found.append(s)
        elif isinstance(obj, dict):
            for v in obj.values():
                walk(v)
        elif isinstance(obj, (list, tuple, set)):
            for v in obj:
                walk(v)

    walk(value)
    return found


def unique(items: Iterable[str]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for item in items:
        item = item.strip()
        if item and item not in seen:
            seen.add(item)
            out.append(item)
    return out


def first_nonempty(*values: Any) -> str:
    for value in values:
        if isinstance(value, str) and value.strip():
            return value.strip()
    return ""


def get_nested(obj: Any, *path: Any) -> Any:
    cur = obj
    for part in path:
        if isinstance(part, int):
            if not isinstance(cur, list) or len(cur) <= part:
                return None
            cur = cur[part]
        else:
            if not isinstance(cur, dict) or part not in cur:
                return None
            cur = cur[part]
    return cur


def find_values_by_key(obj: Any, wanted_keys: set[str]) -> list[Any]:
    """Recursively collect values whose key matches wanted_keys."""
    wanted = {k.lower() for k in wanted_keys}
    values: list[Any] = []

    def walk(cur: Any) -> None:
        if isinstance(cur, dict):
            for key, value in cur.items():
                if str(key).lower() in wanted:
                    values.append(value)
                walk(value)
        elif isinstance(cur, list):
            for value in cur:
                walk(value)

    walk(obj)
    return values


def extract_vulnerability_id(record: dict[str, Any], fallback: str = "") -> str:
    candidates = [
        record.get("id"),
        record.get("cveMetadata", {}).get("cveId") if isinstance(record.get("cveMetadata"), dict) else None,
        record.get("vulnerability_id"),
        record.get("vulnId"),
        record.get("gcveId"),
        record.get("gcve_id"),
    ]
    for candidate in candidates:
        if isinstance(candidate, str) and candidate.strip():
            return candidate.strip().upper()
    return fallback.upper()


GENERIC_TITLES = {
    "cve program container",
    "cve program",
    "vulnerability",
    "vulnerability record",
    "security vulnerability",
    "n/a",
    "na",
    "unknown",
}


def is_generic_title(value: str) -> bool:
    title = re.sub(r"\s+", " ", value).strip().strip(" .:-")
    if not title:
        return True
    lowered = title.lower()
    if lowered in GENERIC_TITLES:
        return True
    if re.fullmatch(r"cve-\d{4}-\d+", lowered, re.IGNORECASE):
        return True
    if re.fullmatch(r"gcve-\d+-\d{4}-\d+", lowered, re.IGNORECASE):
        return True
    return False


def title_from_description(description: str, max_length: int = 150) -> str:
    """Create a compact human-readable title from an advisory description."""
    text = html.unescape(description or "")
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return ""

    # Remove a redundant vulnerability identifier at the beginning.
    text = re.sub(
        r"^(?:CVE-\d{4}-\d+|GCVE-\d+-\d{4}-\d+)\s*[:\-–—]?\s*",
        "",
        text,
        flags=re.IGNORECASE,
    )

    # Prefer the first sentence. If it is still long, use a natural clause
    # boundary before truncating.
    sentence = re.split(r"(?<=[.!?])\s+", text, maxsplit=1)[0].strip()
    if len(sentence) > max_length:
        clauses = re.split(r"\s+(?:because|where|when|which|while|via|through|due to)\s+|[;:]\s+", sentence, maxsplit=1, flags=re.IGNORECASE)
        if clauses and len(clauses[0].strip()) >= 35:
            sentence = clauses[0].strip()

    if len(sentence) > max_length:
        cut = sentence[: max_length - 1].rstrip()
        if " " in cut:
            cut = cut.rsplit(" ", 1)[0]
        sentence = cut.rstrip(" ,;:-") + "…"

    return sentence.strip().rstrip(".")


def extract_title(record: dict[str, Any]) -> str:
    candidates: list[str] = []

    # CVE 5 CNA container. Older CVE records frequently use generic values
    # such as 'CVE Program Container'; keep them only as a last resort.
    cna = get_nested(record, "containers", "cna")
    if isinstance(cna, dict):
        title = cna.get("title")
        if isinstance(title, str) and title.strip():
            candidates.append(title.strip())

    for key in ("title", "summary", "name"):
        value = record.get(key)
        if isinstance(value, str) and value.strip():
            candidates.append(value.strip())

    # OSV-like summaries or titles can be nested after wrappers.
    values = find_values_by_key(record, {"title", "summary"})
    for value in values:
        if isinstance(value, str) and value.strip():
            candidates.append(value.strip())

    # Prefer a genuine supplied title.
    for candidate in unique(candidates):
        if not is_generic_title(candidate):
            return re.sub(r"\s+", " ", candidate).strip()

    # Fall back to a concise title synthesized from the actual description.
    description = extract_description(record)
    generated = title_from_description(description)
    if generated:
        return generated

    # If absolutely nothing else exists, retaining a non-empty generic title
    # is still more informative than an empty heading.
    return candidates[0] if candidates else ""


def choose_english_text(items: Any) -> str:
    if isinstance(items, str):
        return items.strip()

    if isinstance(items, list):
        # Prefer English CVE-style entries.
        for item in items:
            if isinstance(item, dict):
                lang = str(item.get("lang", "")).lower()
                value = first_nonempty(
                    item.get("value"),
                    item.get("description"),
                    item.get("text"),
                )
                if value and (not lang or lang.startswith("en")):
                    return value
        # Fall back to first usable entry.
        for item in items:
            if isinstance(item, dict):
                value = first_nonempty(
                    item.get("value"),
                    item.get("description"),
                    item.get("text"),
                )
                if value:
                    return value
            elif isinstance(item, str) and item.strip():
                return item.strip()

    if isinstance(items, dict):
        return first_nonempty(
            items.get("value"),
            items.get("description"),
            items.get("text"),
        )

    return ""


def extract_description(record: dict[str, Any]) -> str:
    cna = get_nested(record, "containers", "cna")
    if isinstance(cna, dict):
        description = choose_english_text(cna.get("descriptions"))
        if description:
            return description

    for key in ("description", "details"):
        value = record.get(key)
        description = choose_english_text(value)
        if description:
            return description

    values = find_values_by_key(record, {"descriptions", "description", "details"})
    for value in values:
        description = choose_english_text(value)
        if description:
            return description

    return ""


def extract_dates(record: dict[str, Any]) -> tuple[str, str]:
    metadata = record.get("cveMetadata")
    if not isinstance(metadata, dict):
        metadata = {}

    published = first_nonempty(
        metadata.get("datePublished"),
        record.get("Published"),
        record.get("published"),
        record.get("datePublished"),
        record.get("date_published"),
    )
    modified = first_nonempty(
        metadata.get("dateUpdated"),
        record.get("Modified"),
        record.get("modified"),
        record.get("updated"),
        record.get("dateUpdated"),
        record.get("date_modified"),
    )
    return published, modified


def extract_source(record: dict[str, Any]) -> str:
    for key in ("source", "vulnerability_source", "_source"):
        value = record.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
        if isinstance(value, dict):
            result = first_nonempty(value.get("name"), value.get("id"))
            if result:
                return result

    # CVE 5 provider metadata is not exactly the feeder source, but useful.
    provider = get_nested(record, "containers", "cna", "providerMetadata")
    if isinstance(provider, dict):
        return first_nonempty(provider.get("shortName"), provider.get("orgId"))

    return ""


def extract_cwes(record: dict[str, Any]) -> list[str]:
    cwes: list[str] = []

    problem_types = get_nested(record, "containers", "cna", "problemTypes")
    if isinstance(problem_types, list):
        for problem in problem_types:
            if not isinstance(problem, dict):
                continue
            for description in problem.get("descriptions", []) or []:
                if not isinstance(description, dict):
                    continue
                cwe = description.get("cweId")
                desc = description.get("description")
                if isinstance(cwe, str) and cwe.strip():
                    if isinstance(desc, str) and desc.strip() and desc.strip() != cwe.strip():
                        cwes.append(f"{cwe.strip()} — {desc.strip()}")
                    else:
                        cwes.append(cwe.strip())

    for value in find_values_by_key(record, {"cwe", "cweid", "cwe_id"}):
        for s in flatten_strings(value):
            if re.search(r"\bCWE-\d+\b", s, re.IGNORECASE):
                cwes.append(s)

    return unique(cwes)


def extract_cpes(record: dict[str, Any]) -> list[str]:
    cpes: list[str] = []

    # Common keys in NVD / legacy / enriched records.
    for value in find_values_by_key(
        record,
        {
            "cpe",
            "cpes",
            "criteria",
            "vulnerable_configuration",
            "vulnerable_configuration_cpe_2_2",
        },
    ):
        for s in flatten_strings(value):
            if CPE_RE.match(s):
                cpes.append(s)

    # CVE 5 affected.cpes extension.
    affected = get_nested(record, "containers", "cna", "affected")
    if isinstance(affected, list):
        for product in affected:
            if not isinstance(product, dict):
                continue
            for s in flatten_strings(product.get("cpes", [])):
                if CPE_RE.match(s):
                    cpes.append(s)

    return unique(cpes)


def versions_to_text(versions: Any) -> str:
    if not isinstance(versions, list):
        return ""

    rendered: list[str] = []
    for version in versions:
        if isinstance(version, str):
            rendered.append(version)
            continue
        if not isinstance(version, dict):
            continue

        value = first_nonempty(version.get("version"), version.get("lessThan"))
        status = first_nonempty(version.get("status"))
        version_type = first_nonempty(version.get("versionType"))

        tail: list[str] = []
        if version.get("lessThan"):
            tail.append(f"< {version['lessThan']}")
        if version.get("lessThanOrEqual"):
            tail.append(f"≤ {version['lessThanOrEqual']}")
        if status:
            tail.append(status)
        if version_type:
            tail.append(version_type)

        if value and tail:
            rendered.append(f"{value} ({', '.join(tail)})")
        elif value:
            rendered.append(value)
        elif tail:
            rendered.append(", ".join(tail))

    return "; ".join(unique(rendered))


def extract_affected(record: dict[str, Any]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    cna_affected = get_nested(record, "containers", "cna", "affected")
    if isinstance(cna_affected, list):
        for item in cna_affected:
            if not isinstance(item, dict):
                continue
            cpes = [
                s for s in flatten_strings(item.get("cpes", []))
                if CPE_RE.match(s)
            ]
            rows.append(
                {
                    "vendor": first_nonempty(item.get("vendor")),
                    "product": first_nonempty(item.get("product"), item.get("packageName")),
                    "versions": versions_to_text(item.get("versions")),
                    "cpes": ", ".join(cpes),
                }
            )

    # OSV-style affected entries.
    osv_affected = record.get("affected")
    if isinstance(osv_affected, list):
        for item in osv_affected:
            if not isinstance(item, dict):
                continue
            package = item.get("package")
            vendor = ""
            product = ""
            if isinstance(package, dict):
                product = first_nonempty(package.get("name"))
                ecosystem = first_nonempty(package.get("ecosystem"))
                if ecosystem:
                    vendor = ecosystem

            versions = item.get("versions")
            version_text = ", ".join(flatten_strings(versions)) if versions else ""

            if product or vendor or version_text:
                rows.append(
                    {
                        "vendor": vendor,
                        "product": product,
                        "versions": version_text,
                        "cpes": "",
                    }
                )

    # Deduplicate.
    seen: set[tuple[str, str, str, str]] = set()
    deduped: list[dict[str, str]] = []
    for row in rows:
        key = (
            row["vendor"],
            row["product"],
            row["versions"],
            row["cpes"],
        )
        if key not in seen:
            seen.add(key)
            deduped.append(row)
    return deduped


def extract_references(record: dict[str, Any]) -> list[str]:
    refs: list[str] = []

    def add_ref(value: Any) -> None:
        if isinstance(value, str):
            if value.startswith(("http://", "https://")):
                refs.append(value)
        elif isinstance(value, dict):
            url = value.get("url")
            if isinstance(url, str) and url.startswith(("http://", "https://")):
                refs.append(url)
        elif isinstance(value, list):
            for entry in value:
                add_ref(entry)

    cna_refs = get_nested(record, "containers", "cna", "references")
    add_ref(cna_refs)

    add_ref(record.get("references"))
    add_ref(record.get("related"))

    # Recursive fallback for nested source formats.
    for value in find_values_by_key(record, {"references", "reference", "urls"}):
        add_ref(value)

    return unique(refs)


def extract_cvss(record: dict[str, Any]) -> list[dict[str, str]]:
    results: list[dict[str, str]] = []

    def inspect_metric(metric: Any) -> None:
        if not isinstance(metric, dict):
            return

        for key, value in metric.items():
            if isinstance(value, dict) and key.lower().startswith("cvss"):
                vector = first_nonempty(value.get("vectorString"), value.get("vector"))
                score = value.get("baseScore")
                severity = first_nonempty(value.get("baseSeverity"), value.get("severity"))
                version = first_nonempty(value.get("version"))

                if vector or score is not None or severity:
                    results.append(
                        {
                            "version": version or key,
                            "score": "" if score is None else str(score),
                            "severity": severity,
                            "vector": vector,
                        }
                    )

            # Some feeds put CVSS values directly in a metric object.
            vector = value.get("vectorString") if isinstance(value, dict) else None
            if isinstance(vector, str) and CVSS_VECTOR_RE.match(vector):
                score = value.get("baseScore")
                severity = first_nonempty(value.get("baseSeverity"), value.get("severity"))
                version = first_nonempty(value.get("version"))
                results.append(
                    {
                        "version": version,
                        "score": "" if score is None else str(score),
                        "severity": severity,
                        "vector": vector,
                    }
                )

    metrics = get_nested(record, "containers", "cna", "metrics")
    if isinstance(metrics, list):
        for metric in metrics:
            inspect_metric(metric)

    # Recursive fallback catches NVD and other feed shapes.
    for value in find_values_by_key(
        record,
        {
            "cvssv2_0",
            "cvssv3_0",
            "cvssv3_1",
            "cvssv4_0",
            "cvssmetricv2",
            "cvssmetricv30",
            "cvssmetricv31",
            "cvssmetricv40",
        },
    ):
        if isinstance(value, list):
            for item in value:
                inspect_metric({"cvss": item})
        else:
            inspect_metric({"cvss": value})

    # Generic scan for vector strings plus nearby score is difficult without
    # inventing associations, so only use structured metrics above.
    seen: set[tuple[str, str, str, str]] = set()
    deduped: list[dict[str, str]] = []
    for item in results:
        key = (
            item["version"],
            item["score"],
            item["severity"],
            item["vector"],
        )
        if key not in seen:
            seen.add(key)
            deduped.append(item)
    return deduped


def extract_credits(record: dict[str, Any]) -> list[str]:
    credits: list[str] = []
    cna_credits = get_nested(record, "containers", "cna", "credits")
    if isinstance(cna_credits, list):
        for credit in cna_credits:
            if isinstance(credit, str):
                credits.append(credit)
            elif isinstance(credit, dict):
                value = first_nonempty(
                    credit.get("value"),
                    credit.get("name"),
                    credit.get("user"),
                )
                if value:
                    credits.append(value)
    return unique(credits)


def extract_record_from_api(payload: Any, vulnerability_id: str) -> dict[str, Any]:
    """Best-effort unwrapping of API responses."""
    if isinstance(payload, dict):
        if vulnerability_id.lower() in {str(k).lower() for k in payload.keys()}:
            for key, value in payload.items():
                if str(key).lower() == vulnerability_id.lower() and isinstance(value, dict):
                    return value

        for wrapper in ("data", "vulnerability", "record"):
            value = payload.get(wrapper)
            if isinstance(value, dict):
                return value

        return payload

    if isinstance(payload, list):
        for item in payload:
            if isinstance(item, dict):
                item_id = extract_vulnerability_id(item)
                if item_id.lower() == vulnerability_id.lower():
                    return item
        if len(payload) == 1 and isinstance(payload[0], dict):
            return payload[0]

    raise ValueError(f"Unexpected API response for {vulnerability_id}")


class VulnerabilityLookupClient:
    def __init__(
        self,
        base_url: str,
        timeout: int = DEFAULT_TIMEOUT,
        delay: float = DEFAULT_DELAY,
        api_key: str | None = None,
        max_retries: int = DEFAULT_MAX_RETRIES,
        backoff: float = DEFAULT_BACKOFF,
        verbose: bool = False,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.delay = delay
        self.max_retries = max_retries
        self.backoff = backoff
        self.verbose = verbose
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": USER_AGENT,
                "Accept": "application/json, text/html;q=0.9, */*;q=0.8",
            }
        )
        if api_key:
            # Useful for private/premium instances. Harmlessly omitted by default.
            self.session.headers["Authorization"] = f"Bearer {api_key}"

    def _get(self, url: str, **kwargs: Any) -> requests.Response:
        for attempt in range(self.max_retries + 1):
            response = self.session.get(url, timeout=self.timeout, **kwargs)

            if response.status_code != 429:
                response.raise_for_status()
                if self.delay:
                    time.sleep(self.delay)
                return response

            if attempt >= self.max_retries:
                response.raise_for_status()

            if self.verbose:
                eprint(f"[429] response headers from {response.url}:")
                for header_name, header_value in response.headers.items():
                    eprint(f"  {header_name}: {header_value}")

            retry_after = response.headers.get("Retry-After")
            wait: float
            if retry_after:
                try:
                    wait = float(retry_after)
                except ValueError:
                    wait = self.backoff * (2 ** attempt)
            else:
                wait = self.backoff * (2 ** attempt)

            # Add the normal inter-request delay as well, so retries do not
            # immediately resume at the exact edge of the rate-limit window.
            wait += self.delay
            eprint(
                f"[429] rate limited; retry {attempt + 1}/{self.max_retries} "
                f"in {wait:.1f}s"
            )
            time.sleep(wait)

        raise RuntimeError("unreachable")

    def search_ids(self, params: list[tuple[str, str]], max_pages: int = 1000) -> list[str]:
        """
        Execute the same search as the web UI and collect vulnerability IDs.

        Pagination is followed by incrementing `page`; collection stops when a
        page contains no new vulnerability links.
        """
        found: list[str] = []
        seen: set[str] = set()

        for page in range(1, max_pages + 1):
            page_params = list(params)
            if page > 1:
                page_params.append(("page", str(page)))

            response = self._get(
                f"{self.base_url}/search",
                params=page_params,
                headers={"Accept": "text/html,application/xhtml+xml"},
            )
            soup = BeautifulSoup(response.text, "html.parser")

            page_ids: list[str] = []
            for link in soup.find_all("a", href=True):
                href = str(link["href"])
                match = re.search(r"/vuln/([A-Za-z0-9._:-]+)", href, re.IGNORECASE)
                if not match:
                    continue

                vuln_id = match.group(1).strip().upper()
                if not VULN_ID_RE.match(vuln_id):
                    # Keep unknown IDs if they at least look identifier-like.
                    if not re.match(r"^[A-Z0-9][A-Z0-9._:-]+$", vuln_id):
                        continue

                if vuln_id not in seen:
                    seen.add(vuln_id)
                    found.append(vuln_id)
                    page_ids.append(vuln_id)

            eprint(f"[search] page {page}: {len(page_ids)} new vulnerability ID(s)")

            if page == 1 and not page_ids:
                raise RuntimeError(
                    "The search page returned no vulnerability links. "
                    "Check the query or whether the instance HTML changed."
                )

            if not page_ids:
                break

            # If the page exposes pagination and explicitly says there is no next
            # page, stop without making one unnecessary request.
            next_link = soup.find("a", attrs={"rel": lambda value: value and "next" in value})
            if next_link is None:
                pagination = soup.select_one(".pagination")
                if pagination is not None:
                    next_candidate = pagination.find(
                        "a",
                        string=re.compile(r"next|›|»", re.IGNORECASE),
                    )
                    if next_candidate is None and page > 1:
                        break

        return found

    def fetch_record(self, vulnerability_id: str) -> dict[str, Any]:
        url = f"{self.base_url}/api/vulnerability/{vulnerability_id}"
        response = self._get(url, headers={"Accept": "application/json"})
        try:
            payload = response.json()
        except requests.JSONDecodeError as exc:
            raise RuntimeError(
                f"{url} did not return JSON (HTTP {response.status_code})"
            ) from exc
        return extract_record_from_api(payload, vulnerability_id)


def make_search_params(args: argparse.Namespace) -> list[tuple[str, str]]:
    params: list[tuple[str, str]] = [
        ("ft_q", args.query or ""),
        ("vendor", args.vendor or ""),
        ("product", args.product or ""),
        ("assigner", args.assigner or ""),
    ]

    for source in args.source:
        params.append(("sort_sources[]", source))

    params.extend(
        [
            ("date_sort", args.sort or ""),
            ("sort_order", args.order or ""),
            ("cvss_min", "" if args.cvss_min is None else str(args.cvss_min)),
            ("cvss_max", "" if args.cvss_max is None else str(args.cvss_max)),
        ]
    )

    # The web UI can use an apply-ordering switch in some versions. Supplying
    # date_sort/sort_order is enough for the linked query; this option is here
    # for instances that also require the explicit flag.
    if args.apply_ordering:
        params.append(("apply_ordering", "y"))

    return params


def build_search_url(base_url: str, params: list[tuple[str, str]]) -> str:
    return f"{base_url.rstrip('/')}/search?{urlencode(params, doseq=True)}"


def render_markdown(
    base_url: str,
    search_url: str,
    records: list[tuple[str, dict[str, Any]]],
) -> str:
    generated = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    deduped = deduplicate_records(records)

    out: list[str] = [
        "# Vulnerability report",
        "",
        f"_Generated from [Vulnerability-Lookup search]({search_url}) on {generated}._",
        "",
        f"**Records:** {len(deduped)} (deduplicated from {len(records)} fetched records)",
        "",
        "## Contents",
        "",
    ]

    for vuln_id, record, aliases in deduped:
        title = extract_title(record)
        label = f"{vuln_id} — {title}" if title else vuln_id
        anchor = re.sub(r"[^a-z0-9 -]", "", label.lower()).replace(" ", "-")
        anchor = re.sub(r"-+", "-", anchor)
        out.append(f"- [{md_escape(label)}](#{anchor})")

    out.append("")

    for vuln_id, record, aliases in deduped:
        title = extract_title(record)
        description = extract_description(record)
        published, modified = extract_dates(record)
        source = extract_source(record)
        cwes = extract_cwes(record)
        cpes = extract_cpes(record)
        affected = extract_affected(record)
        references = extract_references(record)
        cvss_entries = extract_cvss(record)
        credits = extract_credits(record)

        vuln_url = f"{base_url.rstrip('/')}/vuln/{vuln_id.lower()}"

        heading = f"## {vuln_id}"
        if title:
            heading += f" — {title}"
        out.extend([heading, "", f"**Vulnerability-Lookup:** [{vuln_id}]({vuln_url})", ""])

        metadata_rows: list[tuple[str, str]] = []
        if source:
            metadata_rows.append(("Source", source))
        if aliases:
            metadata_rows.append(("Aliases", ", ".join(aliases)))
        if published:
            metadata_rows.append(("Published", published))
        if modified:
            metadata_rows.append(("Updated", modified))
        if cwes:
            metadata_rows.append(("CWE", "<br>".join(md_escape(x) for x in cwes)))

        if metadata_rows:
            out.extend(["| Field | Value |", "|---|---|"])
            for key, value in metadata_rows:
                out.append(f"| {md_escape(key)} | {value if '<br>' in value else md_escape(value)} |")
            out.append("")

        if description:
            out.extend(["### Description", "", description.strip(), ""])

        if cvss_entries:
            out.extend(
                [
                    "### CVSS",
                    "",
                    "| Version | Score | Severity | Vector |",
                    "|---|---:|---|---|",
                ]
            )
            for metric in cvss_entries:
                vector = md_inline_code(metric["vector"]) if metric["vector"] else ""
                out.append(
                    "| {version} | {score} | {severity} | {vector} |".format(
                        version=md_escape(metric["version"]),
                        score=md_escape(metric["score"]),
                        severity=md_escape(metric["severity"]),
                        vector=vector,
                    )
                )
            out.append("")

        if affected:
            out.extend(
                [
                    "### Affected products",
                    "",
                    "| Vendor / ecosystem | Product | Versions / status | CPE |",
                    "|---|---|---|---|",
                ]
            )
            for row in affected:
                cpe_cell = "<br>".join(
                    md_inline_code(x)
                    for x in [c.strip() for c in row["cpes"].split(",") if c.strip()]
                )
                out.append(
                    "| {vendor} | {product} | {versions} | {cpes} |".format(
                        vendor=md_escape(row["vendor"]),
                        product=md_escape(row["product"]),
                        versions=md_escape(row["versions"]),
                        cpes=cpe_cell,
                    )
                )
            out.append("")

        if cpes:
            out.extend(["### CPE", ""])
            for cpe in cpes:
                out.append(f"- {md_inline_code(cpe)}")
            out.append("")

        if credits:
            out.extend(["### Credits", ""])
            for credit in credits:
                out.append(f"- {md_escape(credit)}")
            out.append("")

        if references:
            out.extend(["### References", ""])
            for ref in references:
                safe_label = md_escape(ref)
                out.append(f"- [{safe_label}]({ref})")
            out.append("")

        # Keep the page useful for uncommon/custom formats without dumping JSON
        # by default. The original record remains one click away.

    return "\n".join(out).rstrip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export a Vulnerability-Lookup search to one Markdown page."
    )
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--vendor", default="misp")
    parser.add_argument("--product", default="")
    parser.add_argument("--assigner", default="")
    parser.add_argument("--query", default="", help="Full-text query (ft_q).")
    parser.add_argument(
        "--source",
        action="append",
        default=None,
        help="Source to include; repeatable. Default: cvelistv5 and gna-1.",
    )
    parser.add_argument(
        "--sort",
        choices=("published", "updated", ""),
        default="published",
        help="Date field used by the search page.",
    )
    parser.add_argument(
        "--order",
        choices=("asc", "desc"),
        default="desc",
    )
    parser.add_argument("--cvss-min", type=float)
    parser.add_argument("--cvss-max", type=float)
    parser.add_argument("--apply-ordering", action="store_true")
    parser.add_argument(
        "--max-pages",
        type=int,
        default=1000,
        help="Safety limit for search-result pagination.",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=DEFAULT_DELAY,
        help=f"Delay in seconds between HTTP requests (default: {DEFAULT_DELAY}).",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=DEFAULT_TIMEOUT,
        help="HTTP timeout in seconds.",
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=DEFAULT_MAX_RETRIES,
        help=f"Maximum retries after HTTP 429 (default: {DEFAULT_MAX_RETRIES}).",
    )
    parser.add_argument(
        "--backoff",
        type=float,
        default=DEFAULT_BACKOFF,
        help=f"Initial exponential backoff in seconds for HTTP 429 (default: {DEFAULT_BACKOFF}).",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Show HTTP response headers when an HTTP 429 rate limit is encountered.",
    )
    parser.add_argument(
        "--api-key",
        default=None,
        help="Optional bearer token for an authenticated instance.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("vulnerabilities.md"),
    )

    args = parser.parse_args()
    if args.source is None:
        args.source = ["cvelistv5", "gna-1"]
    return args


def main() -> int:
    args = parse_args()
    base_url = args.base_url.rstrip("/")
    params = make_search_params(args)
    search_url = build_search_url(base_url, params)

    eprint(f"[query] {search_url}")

    client = VulnerabilityLookupClient(
        base_url=base_url,
        timeout=args.timeout,
        delay=args.delay,
        api_key=args.api_key,
        max_retries=args.max_retries,
        backoff=args.backoff,
        verbose=args.verbose,
    )

    try:
        vuln_ids = client.search_ids(params, max_pages=args.max_pages)
    except (requests.RequestException, RuntimeError) as exc:
        eprint(f"error: search failed: {exc}")
        return 1

    eprint(f"[search] total unique IDs: {len(vuln_ids)}")

    records: list[tuple[str, dict[str, Any]]] = []
    for index, vuln_id in enumerate(vuln_ids, start=1):
        eprint(f"[fetch] {index}/{len(vuln_ids)} {vuln_id}")
        try:
            record = client.fetch_record(vuln_id)
        except (requests.RequestException, RuntimeError, ValueError) as exc:
            eprint(f"warning: unable to fetch {vuln_id}: {exc}")
            continue
        records.append((vuln_id, record))

    deduped_count = len(deduplicate_records(records))
    markdown = render_markdown(base_url, search_url, records)
    args.output.write_text(markdown, encoding="utf-8")
    eprint(
        f"[done] wrote {deduped_count} unique record(s) "
        f"from {len(records)} fetched record(s) to {args.output}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
