---
layout: page
title: MISP Default Feeds
permalink: /feeds/
toc: true
---

MISP includes a set of public OSINT feeds in its default configuration. The feeds can
be used as a source of correlations for all of your events and attributes without the need to
import them directly into your system. The MISP feed system allows for fast correlation but also
a for quick comparisons of the feeds against one another.

The feeds can be in three different formats:

- [MISP standardized format](https://github.com/MISP/misp-rfc/blob/master/misp-core-format/raw.md.txt) which is the preferred format to benefit from all the MISP functionalities.
- CSV format, allowing you to pick the columns that are to be imported.
- freetext format which allows automatic ingestion and detection of indicator/attribute by parsing any unstructured text.

and located in different input transports:

- Network (URL)
- Local (file)

## Default feeds available in MISP

The default feeds are described in a [simple JSON format](https://github.com/MISP/MISP/blob/2.4/app/files/feed-metadata/defaults.json). The default feeds and the current version of MISP are the following:

- [abuse.ch SSL IPBL](https://sslbl.abuse.ch/blacklist/sslblacklist.csv) - abuse.ch - feed format: csv
- [alienvault reputation generic](https://reputation.alienvault.com/reputation.generic) - .alienvault.com - feed format: csv
- [All current domains belonging to known malicious DGAs](https://osint.bambenekconsulting.com/feeds/dga-feed-high.csv) - osint.bambenekconsulting.com - feed format: csv
- [blocklist.de/lists/all.txt](https://lists.blocklist.de/lists/all.txt) - blocklist.de - feed format: freetext
- [blocklist.greensnow.co](https://blocklist.greensnow.co/greensnow.txt) - greensnow.co - feed format: csv
- [blockrules of rules.emergingthreats.net](https://rules.emergingthreats.net/blockrules/compromised-ips.txt) - rules.emergingthreats.net - feed format: csv
- [ci-badguys.txt](https://cinsscore.com/list/ci-badguys.txt) - cinsscore.com - feed format: freetext
- [CIRCL OSINT Feed](https://www.circl.lu/doc/misp/feed-osint) - CIRCL - feed format: misp
- [cybercrime-tracker.net - all](https://cybercrime-tracker.net/all.php) - cybercrime-tracker.net - feed format: freetext
- [CyberCure - Blocked URL Feed](https://api.cybercure.ai/feed/get_url?type=csv) - www.cybercure.ai - feed format: csv
- [CyberCure - Hash Feed](https://api.cybercure.ai/feed/get_hash?type=csv) - www.cybercure.ai - feed format: csv
- [CyberCure - IP Feed](https://api.cybercure.ai/feed/get_ips?type=csv) - www.cybercure.ai - feed format: csv
- [diamondfox_panels](https://raw.githubusercontent.com/pan-unit42/iocs/master/diamondfox/diamondfox_panels.txt) - pan-unit42 - feed format: freetext
- [DigitalSide Threat-Intel OSINT Feed](https://osint.digitalside.it/Threat-Intel/digitalside-misp-feed/) - osint.digitalside.it - feed format: misp
- [DNS CH TXT version.bind](https://dataplane.org/dnsversion.txt) - dataplane.org - feed format: csv
- [DNS recursion desired IN ANY](https://dataplane.org/dnsrdany.txt) - dataplane.org - feed format: csv
- [DNS recursion desired](https://dataplane.org/dnsrd.txt) - dataplane.org - feed format: csv
- [Domains from High-Confidence DGA-based C&C Domains Actively Resolving](https://osint.bambenekconsulting.com/feeds/c2-dommasterlist-high.txt) - osint.bambenekconsulting.com - feed format: csv
- [ELLIO: IP Feed (Community version)](https://cdn.ellio.tech/community-feed) - ellio.tech - feed format: freetext
- [Feodo IP Blocklist](https://feodotracker.abuse.ch/downloads/ipblocklist.csv) - abuse.ch - feed format: csv
- [firehol_level1](https://raw.githubusercontent.com/ktsaou/blocklist-ipsets/master/firehol_level1.netset) - iplists.firehol.org - feed format: freetext
- [http://cybercrime-tracker.net gatelist](https://cybercrime-tracker.net/ccamgate.php) - http://cybercrime-tracker.net gatelist - feed format: freetext
- [http://cybercrime-tracker.net hashlist](https://cybercrime-tracker.net/ccamlist.php) - http://cybercrime-tracker.net hashlist - feed format: freetext
- [IP protocol 41](https://dataplane.org/proto41.txt) - dataplane.org - feed format: csv
- [ip-block-list - snort.org](https://snort.org/downloads/ip-block-list) - https://snort.org - feed format: freetext
- [IPs from High-Confidence DGA-Based C&Cs Actively Resolving - requires a valid license](https://osint.bambenekconsulting.com/feeds/c2-ipmasterlist-high.txt) - osint.bambenekconsulting.com - feed format: csv
- [ipspamlist](http://www.ipspamlist.com/public_feeds.csv) - ipspamlist - feed format: csv
- [IPsum (aggregation of all feeds) - level 1 - lot of false positives](https://raw.githubusercontent.com/stamparm/ipsum/master/levels/1.txt) - IPsum - feed format: freetext
- [IPsum (aggregation of all feeds) - level 2 - medium false positives](https://raw.githubusercontent.com/stamparm/ipsum/master/levels/2.txt) - IPsum - feed format: freetext
- [IPsum (aggregation of all feeds) - level 3 - low false positives](https://raw.githubusercontent.com/stamparm/ipsum/master/levels/3.txt) - IPsum - feed format: freetext
- [IPsum (aggregation of all feeds) - level 4 - very low false positives](https://raw.githubusercontent.com/stamparm/ipsum/master/levels/4.txt) - IPsum - feed format: freetext
- [IPsum (aggregation of all feeds) - level 5 - ultra false positives](https://raw.githubusercontent.com/stamparm/ipsum/master/levels/5.txt) - IPsum - feed format: freetext
- [IPsum (aggregation of all feeds) - level 6 - no false positives](https://raw.githubusercontent.com/stamparm/ipsum/master/levels/6.txt) - IPsum - feed format: freetext
- [IPsum (aggregation of all feeds) - level 7 - no false positives](https://raw.githubusercontent.com/stamparm/ipsum/master/levels/7.txt) - IPsum - feed format: freetext
- [IPsum (aggregation of all feeds) - level 8 - no false positives](https://raw.githubusercontent.com/stamparm/ipsum/master/levels/8.txt) - IPsum - feed format: freetext
- [James Brine Bruteforce IPs](https://jamesbrine.com.au/csv) - jamesbrine.com.au - feed format: csv
- [List of malicious domains in Poland](https://hole.cert.pl/domains/domains.txt) - CERT-PL - feed format: freetext
- [List of malicious hashes](https://cti.bb.com.br:8443/hash-list.csv) - Banco do Brasil S.A - feed format: csv
- [malshare.com - current all](https://malshare.com/daily/malshare.current.all.txt) - malshare.com - feed format: freetext
- [malsilo.domain](https://malsilo.gitlab.io/feeds/dumps/domain_list.txt) - MalSilo - feed format: csv
- [malsilo.ipv4](https://malsilo.gitlab.io/feeds/dumps/ip_list.txt) - MalSilo - feed format: csv
- [malsilo.url](https://malsilo.gitlab.io/feeds/dumps/url_list.txt) - MalSilo - feed format: csv
- [Malware Bazaar](https://bazaar.abuse.ch/export/txt/md5/recent/) - abuse.ch - feed format: csv
- [MalwareBazaar](https://bazaar.abuse.ch/downloads/misp/) - abuse.ch - feed format: misp
- [Metasploit exploits with CVE assigned](https://feeds.ecrimelabs.net/data/metasploit-cve) - eCrimeLabs - feed format: csv
- [mirai.security.gives](https://mirai.security.gives/data/ip_list.txt) - security.gives - feed format: freetext
- [OpenPhish url list](https://openphish.com/feed.txt) - openphish.com - feed format: freetext
- [Panels Tracker](https://benkow.cc/export.php) - Benkow.cc - feed format: csv
- [PhishScore](https://phishstats.info/phish_score.csv) - PhishStats - feed format: csv
- [Phishtank online valid phishing](https://data.phishtank.com/data/online-valid.csv) - Phishtank - feed format: csv
- [pop3gropers](https://home.nuug.no/~peter/pop3gropers.txt) - home.nuug.no - feed format: csv
- [Shreshta: Newly Registered domain names (NRD) - 1 month (Community policy feed)](https://shreshtait.com/newly-registered-domains/nrd-1m) - shreshtait.com - feed format: freetext
- [Shreshta: Newly Registered domain names(NRD) - 1 week (Community policy feed)](https://shreshtait.com/newly-registered-domains/nrd-1w) - shreshtait.com - feed format: freetext
- [sipinvitation](https://dataplane.org/sipinvitation.txt) - dataplane.org - feed format: csv
- [sipquery](https://dataplane.org/sipquery.txt) - dataplane.org - feed format: csv
- [sipregistration](https://dataplane.org/sipregistration.txt) - dataplane.org - feed format: csv
- [SMTP data](https://dataplane.org/smtpdata.txt) - dataplane.org - feed format: csv
- [SMTP greet](https://dataplane.org/smtpgreet.txt) - dataplane.org - feed format: csv
- [SSH Bruteforce IPs](https://feeds.honeynet.asia/bruteforce/latest-sshbruteforce-unique.csv) - APNIC Community Honeynet Project - feed format: csv
- [sshpwauth.txt](https://dataplane.org/sshpwauth.txt) - dataplane.org - feed format: csv
- [Telnet Bruteforce IPs](https://feeds.honeynet.asia/bruteforce/latest-telnetbruteforce-unique.csv) - APNIC Community Honeynet Project - feed format: csv
- [TELNET login](https://dataplane.org/telnetlogin.txt) - dataplane.org - feed format: csv
- [The Botvrij.eu Data](https://www.botvrij.eu/data/feed-osint) - Botvrij.eu - feed format: misp
- [This list contains all browser mining domains - A list to prevent browser mining only](https://gitlab.com/ZeroDot1/CoinBlockerLists/raw/master/list_browser.txt?inline=false) - ZeroDot1 - CoinBlockerLists - feed format: freetext
- [This list contains all domains - A list for administrators to prevent mining in networks](https://gitlab.com/ZeroDot1/CoinBlockerLists/raw/master/list.txt?inline=false) - ZeroDot1 - CoinBlockerLists - feed format: freetext
- [This list contains all optional domains - An additional list for administrators](https://gitlab.com/ZeroDot1/CoinBlockerLists/raw/master/list_optional.txt?inline=false) - ZeroDot1 - CoinBlockerLists - feed format: freetext
- [threatfox indicators of compromise](https://threatfox.abuse.ch/export/csv/recent/) - abuse.ch - feed format: csv
- [Threatfox](https://threatfox.abuse.ch/downloads/misp/) - abuse.ch - feed format: misp
- [Tor ALL nodes](https://www.dan.me.uk/torlist/) - TOR Node List from dan.me.uk - careful, this feed applies a lock-out after each pull. This is shared with the "Tor exit nodes" feed. - feed format: csv
- [Tor exit nodes](https://www.dan.me.uk/torlist/?exit) - TOR Node List from dan.me.uk - careful, this feed applies a lock-out after each pull. This is shared with the "Tor ALL nodes" feed. - feed format: csv
- [URL Seen in honeypots](https://feeds.honeynet.asia/url/latest-url-unique.csv) - APNIC Community Honeynet Project - feed format: freetext
- [URLHaus Malware URLs](https://urlhaus.abuse.ch/downloads/csv_recent/) - abuse.ch - feed format: csv
- [URLhaus](https://urlhaus.abuse.ch/downloads/misp/) - abuse.ch - feed format: misp
- [VNC RFB](https://dataplane.org/vncrfb.txt) - dataplane.org - feed format: csv
- [VXvault - URL List](http://vxvault.net/URL_List.php) - VXvault - feed format: freetext

To enable a feed for caching, you just need to check the enabled field to benefit automatically of the feeds in your local MISP instance. To allow other users of your MISP instance to benefit from this functionality, simply check the "lookup visible" checkbox.

## Feed overlap analysis matrix

![feed overlap analysis matrix](/img/blog/feed-overlap-analys-matrix.png)

## How to have my feed published in the default MISP OSINT feed

- Fork the [MISP project](https://github.com/MISP/MISP) on GitHub.
- Update the [default MISP feed](https://github.com/MISP/MISP/blob/2.4/app/files/feed-metadata/defaults.json) to add your feed(s).
- Make a pull-request with the updated JSON file.