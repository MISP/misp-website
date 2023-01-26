---
layout: page
title: MISP data models - MISP core format - MISP taxonomies
permalink: /datamodels/
toc: true
---

MISP is not only a software but also a series of data models created by the MISP community. MISP includes a simple and practical information sharing format expressed in JSON that can be used with MISP software or by any other software. The MISP formats are now standards handled by the [MISP standard body](https://www.misp-standard.org).

## MISP Core Format

The MISP core format is a simple JSON format used by MISP and other tools to exchange events and attributes. The JSON schema 2.4 is described on the MISP core software and many sample files are available in the OSINT feed.

The MISP format is described as Internet-Draft in [misp-rfc](https://github.com/MISP/MISP-rfc). The MISP format are described to support the developer or organisation willing to build your own tool supporting the MISP format (as import or export). The standard is built from practical use-cases and the implementation references within the MISP project. The standard is quickly evolving following the MISP implementation.

### MISP default attributes and categories

### Attribute Categories vs. Types

|Category| Internal reference | Targeting data | Antivirus detection | Payload delivery | Artifacts dropped | Payload installation |
| --- |:---:|:---:|:---:|:---:|:---:|:---:|
|md5| | | | X | X | X |
|sha1| | | | X | X | X |
|sha256| | | | X | X | X |
|filename| | | | X | X | X |
|pdb| | | | | X | |
|filename&#124;md5| | | | X | X | X |
|filename&#124;sha1| | | | X | X | X |
|filename&#124;sha256| | | | X | X | X |
|ip-src| | | | X | | |
|ip-dst| | | | X | | |
|hostname| | | | X | | |
|domain| | | | X | | |
|domain&#124;ip| | | | | | |
|email| | | | X | | |
|email-src| | | | X | | |
|eppn| | | | | | |
|email-dst| | | | X | | |
|email-subject| | | | X | | |
|email-attachment| | | | X | | |
|email-body| | | | X | | |
|float| | | | | | |
|git-commit-id| X | | | | | |
|url| | | | X | | |
|http-method| | | | | | |
|user-agent| | | | X | | |
|ja3-fingerprint-md5| | | | X | | |
|jarm-fingerprint| | | | X | | |
|favicon-mmh3| | | | | | |
|hassh-md5| | | | X | | |
|hasshserver-md5| | | | X | | |
|regkey| | | | | X | |
|regkey&#124;value| | | | | X | |
|AS| | | | X | | |
|snort| | | | | | |
|bro| | | | | | |
|zeek| | | | | | |
|community-id| | | | | | |
|pattern-in-file| | | | X | X | X |
|pattern-in-traffic| | | | X | | X |
|pattern-in-memory| | | | | X | X |
|filename-pattern| | | | X | X | X |
|pgp-public-key| | | | | X | |
|pgp-private-key| | | | | X | |
|ssh-fingerprint| | | | | | |
|yara| | | | X | X | X |
|stix2-pattern| | | | X | X | X |
|sigma| | | | X | X | X |
|gene| | | | | X | |
|kusto-query| | | | | X | |
|mime-type| | | | X | X | X |
|identity-card-number| | | | | | |
|cookie| | | | | X | |
|vulnerability| | | | X | | X |
|cpe| | | | X | | X |
|weakness| | | | X | | X |
|attachment| | | X | X | X | X |
|malware-sample| | | | X | X | X |
|link| X | | X | X | | |
|comment| X | X | X | X | X | X |
|text| X | | X | X | X | X |
|hex| X | | X | X | X | X |
|other| X | | X | X | X | X |
|named pipe| | | | | X | |
|mutex| | | | | X | |
|process-state| | | | | X | |
|target-user| | X | | | | |
|target-email| | X | | | | |
|target-machine| | X | | | | |
|target-org| | X | | | | |
|target-location| | X | | | | |
|target-external| | X | | | | |
|btc| | | | | | |
|dash| | | | | | |
|xmr| | | | | | |
|iban| | | | | | |
|bic| | | | | | |
|bank-account-nr| | | | | | |
|aba-rtn| | | | | | |
|bin| | | | | | |
|cc-number| | | | | | |
|prtn| | | | | | |
|phone-number| | | | | | |
|threat-actor| | | | | | |
|campaign-name| | | | | | |
|campaign-id| | | | | | |
|malware-type| | | | X | | X |
|uri| | | | | | |
|authentihash| | | | X | X | X |
|vhash| | | | X | X | X |
|ssdeep| | | | X | X | X |
|imphash| | | | X | X | X |
|telfhash| | | | X | X | X |
|pehash| | | | X | | X |
|impfuzzy| | | | X | X | X |
|sha224| | | | X | X | X |
|sha384| | | | X | X | X |
|sha512| | | | X | X | X |
|sha512/224| | | | X | X | X |
|sha512/256| | | | X | X | X |
|sha3-224| | | | X | X | X |
|sha3-256| | | | X | X | X |
|sha3-384| | | | X | X | X |
|sha3-512| | | | X | X | X |
|tlsh| | | | X | | X |
|cdhash| | | | X | X | X |
|filename&#124;authentihash| | | | X | X | X |
|filename&#124;vhash| | | | X | X | X |
|filename&#124;ssdeep| | | | X | X | X |
|filename&#124;imphash| | | | X | X | X |
|filename&#124;impfuzzy| | | | X | X | X |
|filename&#124;pehash| | | | X | X | X |
|filename&#124;sha224| | | | X | X | X |
|filename&#124;sha384| | | | X | X | X |
|filename&#124;sha512| | | | X | X | X |
|filename&#124;sha512/224| | | | X | X | X |
|filename&#124;sha512/256| | | | X | X | X |
|filename&#124;sha3-224| | | | X | X | X |
|filename&#124;sha3-256| | | | X | X | X |
|filename&#124;sha3-384| | | | X | X | X |
|filename&#124;sha3-512| | | | X | X | X |
|filename&#124;tlsh| | | | X | X | X |
|windows-scheduled-task| | | | | X | |
|windows-service-name| | | | | X | |
|windows-service-displayname| | | | | X | |
|whois-registrant-email| | | | X | | |
|whois-registrant-phone| | | | | | |
|whois-registrant-name| | | | | | |
|whois-registrant-org| | | | | | |
|whois-registrar| | | | | | |
|whois-creation-date| | | | | | |
|x509-fingerprint-sha1| | | | X | X | X |
|x509-fingerprint-md5| | | | X | X | X |
|x509-fingerprint-sha256| | | | X | X | X |
|dns-soa-email| | | | | | |
|size-in-bytes| | | | | | |
|counter| | | | | | |
|datetime| | | | | | |
|port| | | | | | |
|ip-dst&#124;port| | | | X | | |
|ip-src&#124;port| | | | X | | |
|hostname&#124;port| | | | X | | |
|mac-address| | | | X | | |
|mac-eui-64| | | | X | | |
|email-dst-display-name| | | | X | | |
|email-src-display-name| | | | X | | |
|email-header| | | | X | | |
|email-reply-to| | | | X | | |
|email-x-mailer| | | | X | | |
|email-mime-boundary| | | | X | | |
|email-thread-index| | | | X | | |
|email-message-id| | | | X | | |
|github-username| | | | | | |
|github-repository| | | | | | |
|github-organisation| | | | | | |
|jabber-id| | | | | | |
|twitter-id| | | | | | |
|dkim| | | | | | |
|dkim-signature| | | | | | |
|first-name| | | | | | |
|middle-name| | | | | | |
|last-name| | | | | | |
|full-name| | | | | | |
|date-of-birth| | | | | | |
|place-of-birth| | | | | | |
|gender| | | | | | |
|passport-number| | | | | | |
|passport-country| | | | | | |
|passport-expiration| | | | | | |
|redress-number| | | | | | |
|nationality| | | | | | |
|visa-number| | | | | | |
|issue-date-of-the-visa| | | | | | |
|primary-residence| | | | | | |
|country-of-residence| | | | | | |
|special-service-request| | | | | | |
|frequent-flyer-number| | | | | | |
|travel-details| | | | | | |
|payment-details| | | | | | |
|place-port-of-original-embarkation| | | | | | |
|place-port-of-clearance| | | | | | |
|place-port-of-onward-foreign-destination| | | | | | |
|passenger-name-record-locator-number| | | | | | |
|mobile-application-id| | | | X | | X |
|azure-application-id| | | | X | | X |
|chrome-extension-id| | | | X | | X |
|cortex| | | | | | |
|boolean| | | | | | |
|anonymised| X | X | X | X | X | X |

|Category| Persistence mechanism | Network activity | Payload type | Attribution | External analysis | Financial fraud |
| --- |:---:|:---:|:---:|:---:|:---:|:---:|
|md5| | | | | X | |
|sha1| | | | | X | |
|sha256| | | | | X | |
|filename| X | | | | X | |
|pdb| | | | | | |
|filename&#124;md5| | | | | X | |
|filename&#124;sha1| | | | | X | |
|filename&#124;sha256| | | | | X | |
|ip-src| | X | | | X | |
|ip-dst| | X | | | X | |
|hostname| | X | | | X | |
|domain| | X | | | X | |
|domain&#124;ip| | X | | | X | |
|email| | X | | X | | |
|email-src| | X | | | | |
|eppn| | X | | | | |
|email-dst| | X | | | | |
|email-subject| | X | | | | |
|email-attachment| | | | | | |
|email-body| | | | | | |
|float| | | | | | |
|git-commit-id| | | | | | |
|url| | X | | | X | |
|http-method| | X | | | | |
|user-agent| | X | | | X | |
|ja3-fingerprint-md5| | X | | | X | |
|jarm-fingerprint| | X | | | X | |
|favicon-mmh3| | X | | | | |
|hassh-md5| | X | | | X | |
|hasshserver-md5| | X | | | X | |
|regkey| X | | | | X | |
|regkey&#124;value| X | | | | X | |
|AS| | X | | | X | |
|snort| | X | | | X | |
|bro| | X | | | X | |
|zeek| | X | | | X | |
|community-id| | X | | | X | |
|pattern-in-file| | X | | | X | |
|pattern-in-traffic| | X | | | X | |
|pattern-in-memory| | | | | X | |
|filename-pattern| | X | | | X | |
|pgp-public-key| | | | | | |
|pgp-private-key| | | | | | |
|ssh-fingerprint| | X | | | | |
|yara| | | | | | |
|stix2-pattern| | X | | | | |
|sigma| | | | | | |
|gene| | | | | | |
|kusto-query| | | | | | |
|mime-type| | | | | | |
|identity-card-number| | | | | | |
|cookie| | X | | | | |
|vulnerability| | | | | X | |
|cpe| | | | | X | |
|weakness| | | | | X | |
|attachment| | X | | | X | |
|malware-sample| | | | | X | |
|link| | | | | X | |
|comment| X | X | X | X | X | X |
|text| X | X | X | X | X | X |
|hex| X | X | | | | X |
|other| X | X | X | X | X | X |
|named pipe| | | | | | |
|mutex| | | | | | |
|process-state| | | | | | |
|target-user| | | | | | |
|target-email| | | | | | |
|target-machine| | | | | | |
|target-org| | | | | | |
|target-location| | | | | | |
|target-external| | | | | | |
|btc| | | | | | X |
|dash| | | | | | X |
|xmr| | | | | | X |
|iban| | | | | | X |
|bic| | | | | | X |
|bank-account-nr| | | | | | X |
|aba-rtn| | | | | | X |
|bin| | | | | | X |
|cc-number| | | | | | X |
|prtn| | | | | | X |
|phone-number| | | | | | X |
|threat-actor| | | | X | | |
|campaign-name| | | | X | | |
|campaign-id| | | | X | | |
|malware-type| | | | | | |
|uri| | X | | | | |
|authentihash| | | | | | |
|vhash| | | | | | |
|ssdeep| | | | | | |
|imphash| | | | | | |
|telfhash| | | | | | |
|pehash| | | | | | |
|impfuzzy| | | | | | |
|sha224| | | | | | |
|sha384| | | | | | |
|sha512| | | | | | |
|sha512/224| | | | | | |
|sha512/256| | | | | | |
|sha3-224| | | | | X | |
|sha3-256| | | | | X | |
|sha3-384| | | | | X | |
|sha3-512| | | | | X | |
|tlsh| | | | | | |
|cdhash| | | | | | |
|filename&#124;authentihash| | | | | | |
|filename&#124;vhash| | | | | | |
|filename&#124;ssdeep| | | | | | |
|filename&#124;imphash| | | | | | |
|filename&#124;impfuzzy| | | | | | |
|filename&#124;pehash| | | | | | |
|filename&#124;sha224| | | | | | |
|filename&#124;sha384| | | | | | |
|filename&#124;sha512| | | | | | |
|filename&#124;sha512/224| | | | | | |
|filename&#124;sha512/256| | | | | | |
|filename&#124;sha3-224| | | | | X | |
|filename&#124;sha3-256| | | | | X | |
|filename&#124;sha3-384| | | | | X | |
|filename&#124;sha3-512| | | | | X | |
|filename&#124;tlsh| | | | | | |
|windows-scheduled-task| | | | | | |
|windows-service-name| | | | | | |
|windows-service-displayname| | | | | | |
|whois-registrant-email| | | | X | | |
|whois-registrant-phone| | | | X | | |
|whois-registrant-name| | | | X | | |
|whois-registrant-org| | | | X | | |
|whois-registrar| | | | X | | |
|whois-creation-date| | | | X | | |
|x509-fingerprint-sha1| | X | | X | X | |
|x509-fingerprint-md5| | X | | X | X | |
|x509-fingerprint-sha256| | X | | X | X | |
|dns-soa-email| | | | X | | |
|size-in-bytes| | | | | | |
|counter| | | | | | |
|datetime| | | | | | |
|port| | X | | | | |
|ip-dst&#124;port| | X | | | X | |
|ip-src&#124;port| | X | | | X | |
|hostname&#124;port| | X | | | | |
|mac-address| | X | | | X | |
|mac-eui-64| | X | | | X | |
|email-dst-display-name| | | | | | |
|email-src-display-name| | | | | | |
|email-header| | | | | | |
|email-reply-to| | | | | | |
|email-x-mailer| | | | | | |
|email-mime-boundary| | | | | | |
|email-thread-index| | | | | | |
|email-message-id| | | | | | |
|github-username| | | | | | |
|github-repository| | | | | X | |
|github-organisation| | | | | | |
|jabber-id| | | | | | |
|twitter-id| | | | | | |
|dkim| | X | | | | |
|dkim-signature| | X | | | | |
|first-name| | | | | | |
|middle-name| | | | | | |
|last-name| | | | | | |
|full-name| | | | | | |
|date-of-birth| | | | | | |
|place-of-birth| | | | | | |
|gender| | | | | | |
|passport-number| | | | | | |
|passport-country| | | | | | |
|passport-expiration| | | | | | |
|redress-number| | | | | | |
|nationality| | | | | | |
|visa-number| | | | | | |
|issue-date-of-the-visa| | | | | | |
|primary-residence| | | | | | |
|country-of-residence| | | | | | |
|special-service-request| | | | | | |
|frequent-flyer-number| | | | | | |
|travel-details| | | | | | |
|payment-details| | | | | | |
|place-port-of-original-embarkation| | | | | | |
|place-port-of-clearance| | | | | | |
|place-port-of-onward-foreign-destination| | | | | | |
|passenger-name-record-locator-number| | | | | | |
|mobile-application-id| | | | | | |
|azure-application-id| | | | | | |
|chrome-extension-id| | | | | | |
|cortex| | | | | X | |
|boolean| | | | | | |
|anonymised| X | X | X | X | X | X |

|Category| Support Tool | Social network | Person | Other |
| --- |:---:|:---:|:---:|:---:|
|md5| | | | |
|sha1| | | | |
|sha256| | | | |
|filename| | | | |
|pdb| | | | |
|filename&#124;md5| | | | |
|filename&#124;sha1| | | | |
|filename&#124;sha256| | | | |
|ip-src| | | | |
|ip-dst| | | | |
|hostname| | | | |
|domain| | | | |
|domain&#124;ip| | | | |
|email| | X | X | |
|email-src| | X | | |
|eppn| | X | | |
|email-dst| | X | | |
|email-subject| | | | |
|email-attachment| | | | |
|email-body| | | | |
|float| | | | X |
|git-commit-id| | | | |
|url| | | | |
|http-method| | | | |
|user-agent| | | | |
|ja3-fingerprint-md5| | | | |
|jarm-fingerprint| | | | |
|favicon-mmh3| | | | |
|hassh-md5| | | | |
|hasshserver-md5| | | | |
|regkey| | | | |
|regkey&#124;value| | | | |
|AS| | | | |
|snort| | | | |
|bro| | | | |
|zeek| | | | |
|community-id| | | | |
|pattern-in-file| | | | |
|pattern-in-traffic| | | | |
|pattern-in-memory| | | | |
|filename-pattern| | | | |
|pgp-public-key| | X | X | X |
|pgp-private-key| | X | X | X |
|ssh-fingerprint| | | | |
|yara| | | | |
|stix2-pattern| | | | |
|sigma| | | | |
|gene| | | | |
|kusto-query| | | | |
|mime-type| | | | |
|identity-card-number| | | X | |
|cookie| | | | |
|vulnerability| | | | |
|cpe| | | | X |
|weakness| | | | |
|attachment| X | | | |
|malware-sample| | | | |
|link| X | | | |
|comment| X | X | X | X |
|text| X | X | X | X |
|hex| X | | | X |
|other| X | X | X | X |
|named pipe| | | | |
|mutex| | | | |
|process-state| | | | |
|target-user| | | | |
|target-email| | | | |
|target-machine| | | | |
|target-org| | | | |
|target-location| | | | |
|target-external| | | | |
|btc| | | | |
|dash| | | | |
|xmr| | | | |
|iban| | | | |
|bic| | | | |
|bank-account-nr| | | | |
|aba-rtn| | | | |
|bin| | | | |
|cc-number| | | | |
|prtn| | | | |
|phone-number| | | X | X |
|threat-actor| | | | |
|campaign-name| | | | |
|campaign-id| | | | |
|malware-type| | | | |
|uri| | | | |
|authentihash| | | | |
|vhash| | | | |
|ssdeep| | | | |
|imphash| | | | |
|telfhash| | | | |
|pehash| | | | |
|impfuzzy| | | | |
|sha224| | | | |
|sha384| | | | |
|sha512| | | | |
|sha512/224| | | | |
|sha512/256| | | | |
|sha3-224| | | | |
|sha3-256| | | | |
|sha3-384| | | | |
|sha3-512| | | | |
|tlsh| | | | |
|cdhash| | | | |
|filename&#124;authentihash| | | | |
|filename&#124;vhash| | | | |
|filename&#124;ssdeep| | | | |
|filename&#124;imphash| | | | |
|filename&#124;impfuzzy| | | | |
|filename&#124;pehash| | | | |
|filename&#124;sha224| | | | |
|filename&#124;sha384| | | | |
|filename&#124;sha512| | | | |
|filename&#124;sha512/224| | | | |
|filename&#124;sha512/256| | | | |
|filename&#124;sha3-224| | | | |
|filename&#124;sha3-256| | | | |
|filename&#124;sha3-384| | | | |
|filename&#124;sha3-512| | | | |
|filename&#124;tlsh| | | | |
|windows-scheduled-task| | | | |
|windows-service-name| | | | |
|windows-service-displayname| | | | |
|whois-registrant-email| | X | | |
|whois-registrant-phone| | | | |
|whois-registrant-name| | | | |
|whois-registrant-org| | | | |
|whois-registrar| | | | |
|whois-creation-date| | | | |
|x509-fingerprint-sha1| | | | |
|x509-fingerprint-md5| | | | |
|x509-fingerprint-sha256| | | | |
|dns-soa-email| | | | |
|size-in-bytes| | | | X |
|counter| | | | X |
|datetime| | | | X |
|port| | | | X |
|ip-dst&#124;port| | | | |
|ip-src&#124;port| | | | |
|hostname&#124;port| | | | |
|mac-address| | | | |
|mac-eui-64| | | | |
|email-dst-display-name| | | | |
|email-src-display-name| | | | |
|email-header| | | | |
|email-reply-to| | | | |
|email-x-mailer| | | | |
|email-mime-boundary| | | | |
|email-thread-index| | | | |
|email-message-id| | | | |
|github-username| | X | | |
|github-repository| | X | | |
|github-organisation| | X | | |
|jabber-id| | X | | |
|twitter-id| | X | | |
|dkim| | | | |
|dkim-signature| | | | |
|first-name| | | X | |
|middle-name| | | X | |
|last-name| | | X | |
|full-name| | | X | |
|date-of-birth| | | X | |
|place-of-birth| | | X | |
|gender| | | X | |
|passport-number| | | X | |
|passport-country| | | X | |
|passport-expiration| | | X | |
|redress-number| | | X | |
|nationality| | | X | |
|visa-number| | | X | |
|issue-date-of-the-visa| | | X | |
|primary-residence| | | X | |
|country-of-residence| | | X | |
|special-service-request| | | X | |
|frequent-flyer-number| | | X | |
|travel-details| | | X | |
|payment-details| | | X | |
|place-port-of-original-embarkation| | | X | |
|place-port-of-clearance| | | X | |
|place-port-of-onward-foreign-destination| | | X | |
|passenger-name-record-locator-number| | | X | |
|mobile-application-id| | | | |
|azure-application-id| | | | |
|chrome-extension-id| | | | |
|cortex| | | | |
|boolean| | | | X |
|anonymised| X | X | X | X |

### Categories

*   **Internal reference**: Reference used by the publishing party (e.g. ticket number)
*   **Targeting data**: Targeting information to include recipient email, infected machines, department, and or locations.
*   **Antivirus detection**: List of anti-virus vendors detecting the malware or information on detection performance (e.g. 13/43 or 67%). Attachment with list of detection or link to VirusTotal could be placed here as well.
*   **Payload delivery**: Information about the way the malware payload is initially delivered, for example information about the email or web-site, vulnerability used, originating IP etc. Malware sample itself should be attached here.
*   **Artifacts dropped**: Any artifact (files, registry keys etc.) dropped by the malware or other modifications to the system
*   **Payload installation**: Location where the payload was placed in the system and the way it was installed. For example, a filename|md5 type attribute can be added here like this: c:\windows\system32\malicious.exe|41d8cd98f00b204e9800998ecf8427e.
*   **Persistence mechanism**: Mechanisms used by the malware to start at boot. This could be a registry key, legitimate driver modification, LNK file in startup
*   **Network activity**: Information about network traffic generated by the malware
*   **Payload type**: Information about the final payload(s). Can contain a function of the payload, e.g. keylogger, RAT, or a name if identified, such as Poison Ivy.
*   **Attribution**: Identification of the group, organisation, or country behind the attack
*   **External analysis**: Any other result from additional analysis of the malware like tools output Examples: pdf-parser output, automated sandbox analysis, reverse engineering report.
*   **Financial fraud**: Financial Fraud indicators, for example: IBAN Numbers, BIC codes, Credit card numbers, etc.
*   **Support Tool**: Tools supporting analysis or detection of the event
*   **Social network**: Social networks and platforms
*   **Person**: A human being - natural person
*   **Other**: Attributes that are not part of any other category or are meant to be used as a component in MISP objects in the future

### Types

*   **md5**: You are encouraged to use filename|md5 instead. A checksum in md5 format, only use this if you don't know the correct filename
*   **sha1**: You are encouraged to use filename|sha1 instead. A checksum in sha1 format, only use this if you don't know the correct filename
*   **sha256**: You are encouraged to use filename|sha256 instead. A checksum in sha256 format, only use this if you don't know the correct filename
*   **filename**: Filename
*   **pdb**: Microsoft Program database (PDB) path information
*   **filename|md5**: A filename and an md5 hash separated by a | (no spaces)
*   **filename|sha1**: A filename and an sha1 hash separated by a | (no spaces)
*   **filename|sha256**: A filename and an sha256 hash separated by a | (no spaces)
*   **ip-src**: A source IP address of the attacker
*   **ip-dst**: A destination IP address of the attacker or C&C server. Also set the IDS flag on when this IP is hardcoded in malware
*   **hostname**: A full host/dnsname of an attacker. Also set the IDS flag on when this hostname is hardcoded in malware
*   **domain**: A domain name used in the malware. Use this instead of hostname when the upper domain is important or can be used to create links between events.
*   **domain|ip**: A domain name and its IP address (as found in DNS lookup) separated by a | (no spaces)
*   **email**: An e-mail address
*   **email-src**: The source email address. Used to describe the sender when describing an e-mail.
*   **eppn**: eduPersonPrincipalName - eppn - the NetId of the person for the purposes of inter-institutional authentication. Should be stored in the form of user@univ.edu, where univ.edu is the name of the local security domain.
*   **email-dst**: The destination email address. Used to describe the recipient when describing an e-mail.
*   **email-subject**: The subject of the email
*   **email-attachment**: File name of the email attachment.
*   **email-body**: Email body
*   **float**: A floating point value.
*   **git-commit-id**: A git commit ID.
*   **url**: url
*   **http-method**: HTTP method used by the malware (e.g. POST, GET, ...).
*   **user-agent**: The user-agent used by the malware in the HTTP request.
*   **ja3-fingerprint-md5**: JA3 is a method for creating SSL/TLS client fingerprints that should be easy to produce on any platform and can be easily shared for threat intelligence.
*   **jarm-fingerprint**: JARM is a method for creating SSL/TLS server fingerprints.
*   **favicon-mmh3**: favicon-mmh3 is the murmur3 hash of a favicon as used in Shodan.
*   **hassh-md5**: hassh is a network fingerprinting standard which can be used to identify specific Client SSH implementations. The fingerprints can be easily stored, searched and shared in the form of an MD5 fingerprint.
*   **hasshserver-md5**: hasshServer is a network fingerprinting standard which can be used to identify specific Server SSH implementations. The fingerprints can be easily stored, searched and shared in the form of an MD5 fingerprint.
*   **regkey**: Registry key or value
*   **regkey|value**: Registry value + data separated by |
*   **AS**: Autonomous system
*   **snort**: An IDS rule in Snort rule-format. This rule will be automatically rewritten in the NIDS exports.
*   **bro**: An NIDS rule in the Bro rule-format.
*   **zeek**: An NIDS rule in the Zeek rule-format.
*   **community-id**: a community ID flow hashing algorithm to map multiple traffic monitors into common flow id
*   **pattern-in-file**: Pattern in file that identifies the malware
*   **pattern-in-traffic**: Pattern in network traffic that identifies the malware
*   **pattern-in-memory**: Pattern in memory dump that identifies the malware
*   **filename-pattern**: A pattern in the name of a file
*   **pgp-public-key**: A PGP public key
*   **pgp-private-key**: A PGP private key
*   **ssh-fingerprint**: A fingerprint of SSH key material
*   **yara**: Yara signature
*   **stix2-pattern**: STIX 2 pattern
*   **sigma**: Sigma - Generic Signature Format for SIEM Systems
*   **gene**: GENE - Go Evtx sigNature Engine
*   **kusto-query**: Kusto query - Kusto from Microsoft Azure is a service for storing and running interactive analytics over Big Data.
*   **mime-type**: A media type (also MIME type and content type) is a two-part identifier for file formats and format contents transmitted on the Internet
*   **identity-card-number**: Identity card number
*   **cookie**: HTTP cookie as often stored on the user web client. This can include authentication cookie or session cookie.
*   **vulnerability**: A reference to the vulnerability used in the exploit
*   **cpe**: Common Platform Enumeration - structured naming scheme for information technology systems, software, and packages.
*   **weakness**: A reference to the weakness used in the exploit
*   **attachment**: Please upload files using the <em>Upload Attachment</em> button.
*   **malware-sample**: Please upload files using the <em>Upload Attachment</em> button.
*   **link**: Link to an external information
*   **comment**: Comment or description in a human language. This will not be correlated with other attributes
*   **text**: Name, ID or a reference
*   **hex**: A value in hexadecimal format
*   **other**: Other attribute
*   **named pipe**: Named pipe, use the format \.\pipe\<PipeName>
*   **mutex**: Mutex, use the format \BaseNamedObjects\<Mutex>
*   **process-state**: State of a process
*   **target-user**: Attack Targets Username(s)
*   **target-email**: Attack Targets Email(s)
*   **target-machine**: Attack Targets Machine Name(s)
*   **target-org**: Attack Targets Department or Organization(s)
*   **target-location**: Attack Targets Physical Location(s)
*   **target-external**: External Target Organizations Affected by this Attack
*   **btc**: Bitcoin Address
*   **dash**: Dash Address
*   **xmr**: Monero Address
*   **iban**: International Bank Account Number
*   **bic**: Bank Identifier Code Number also known as SWIFT-BIC, SWIFT code or ISO 9362 code
*   **bank-account-nr**: Bank account number without any routing number
*   **aba-rtn**: ABA routing transit number
*   **bin**: Bank Identification Number
*   **cc-number**: Credit-Card Number
*   **prtn**: Premium-Rate Telephone Number
*   **phone-number**: Telephone Number
*   **threat-actor**: A string identifying the threat actor
*   **campaign-name**: Associated campaign name
*   **campaign-id**: Associated campaign ID
*   **malware-type**:
*   **uri**: Uniform Resource Identifier
*   **authentihash**: You are encouraged to use filename|authentihash instead. Authenticode executable signature hash, only use this if you don't know the correct filename
*   **vhash**: You are encouraged to use filename|vhash instead. A checksum from VirusTotal, only use this if you don't know the correct filename
*   **ssdeep**: You are encouraged to use filename|ssdeep instead. A checksum in the SSDeep format, only use this if you don't know the correct filename
*   **imphash**: You are encouraged to use filename|imphash instead. A hash created based on the imports in the sample, only use this if you don't know the correct filename
*   **telfhash**: You are encouraged to use a file object with telfash
*   **pehash**: PEhash - a hash calculated based of certain pieces of a PE executable file
*   **impfuzzy**: You are encouraged to use filename|impfuzzy instead. A fuzzy hash created based on the imports in the sample, only use this if you don't know the correct filename
*   **sha224**: You are encouraged to use filename|sha224 instead. A checksum in sha224 format, only use this if you don't know the correct filename
*   **sha384**: You are encouraged to use filename|sha384 instead. A checksum in sha384 format, only use this if you don't know the correct filename
*   **sha512**: You are encouraged to use filename|sha512 instead. A checksum in sha512 format, only use this if you don't know the correct filename
*   **sha512/224**: You are encouraged to use filename|sha512/224 instead. A checksum in sha512/224 format, only use this if you don't know the correct filename
*   **sha512/256**: You are encouraged to use filename|sha512/256 instead. A checksum in sha512/256 format, only use this if you don't know the correct filename
*   **sha3-224**: You are encouraged to use filename|sha3-224 instead. A checksum in sha3-224 format, only use this if you don't know the correct filename
*   **sha3-256**: You are encouraged to use filename|sha3-256 instead. A checksum in sha3-256 format, only use this if you don't know the correct filename
*   **sha3-384**: You are encouraged to use filename|sha3-384 instead. A checksum in sha3-384 format, only use this if you don't know the correct filename
*   **sha3-512**: You are encouraged to use filename|sha3-512 instead. A checksum in sha3-512 format, only use this if you don't know the correct filename
*   **tlsh**: You are encouraged to use filename|tlsh instead. A checksum in the Trend Micro Locality Sensitive Hash format, only use this if you don't know the correct filename
*   **cdhash**: An Apple Code Directory Hash, identifying a code-signed Mach-O executable file
*   **filename|authentihash**: A checksum in md5 format
*   **filename|vhash**: A filename and a VirusTotal hash separated by a |
*   **filename|ssdeep**: A checksum in ssdeep format
*   **filename|imphash**: Import hash - a hash created based on the imports in the sample.
*   **filename|impfuzzy**: Import fuzzy hash - a fuzzy hash created based on the imports in the sample.
*   **filename|pehash**: A filename and a PEhash separated by a |
*   **filename|sha224**: A filename and a sha-224 hash separated by a |
*   **filename|sha384**: A filename and a sha-384 hash separated by a |
*   **filename|sha512**: A filename and a sha-512 hash separated by a |
*   **filename|sha512/224**: A filename and a sha-512/224 hash separated by a |
*   **filename|sha512/256**: A filename and a sha-512/256 hash separated by a |
*   **filename|sha3-224**: A filename and an sha3-224 hash separated by a |
*   **filename|sha3-256**: A filename and an sha3-256 hash separated by a |
*   **filename|sha3-384**: A filename and an sha3-384 hash separated by a |
*   **filename|sha3-512**: A filename and an sha3-512 hash separated by a |
*   **filename|tlsh**: A filename and a Trend Micro Locality Sensitive Hash separated by a |
*   **windows-scheduled-task**: A scheduled task in windows
*   **windows-service-name**: A windows service name. This is the name used internally by windows. Not to be confused with the windows-service-displayname.
*   **windows-service-displayname**: A windows service's displayname, not to be confused with the windows-service-name. This is the name that applications will generally display as the service's name in applications.
*   **whois-registrant-email**: The e-mail of a domain's registrant, obtained from the WHOIS information.
*   **whois-registrant-phone**: The phone number of a domain's registrant, obtained from the WHOIS information.
*   **whois-registrant-name**: The name of a domain's registrant, obtained from the WHOIS information.
*   **whois-registrant-org**: The org of a domain's registrant, obtained from the WHOIS information.
*   **whois-registrar**: The registrar of the domain, obtained from the WHOIS information.
*   **whois-creation-date**: The date of domain's creation, obtained from the WHOIS information.
*   **x509-fingerprint-sha1**: X509 fingerprint in SHA-1 format
*   **x509-fingerprint-md5**: X509 fingerprint in MD5 format
*   **x509-fingerprint-sha256**: X509 fingerprint in SHA-256 format
*   **dns-soa-email**: RFC1035 mandates that DNS zones should have a SOA (Statement Of Authority) record that contains an email address where a PoC for the domain could be contacted. This can sometimes be used for attribution/linkage between different domains even if protected by whois privacy
*   **size-in-bytes**: Size expressed in bytes
*   **counter**: An integer counter, generally to be used in objects
*   **datetime**: Datetime in the ISO 8601 format
*   **port**: Port number
*   **ip-dst|port**: IP destination and port number separated by a |
*   **ip-src|port**: IP source and port number separated by a |
*   **hostname|port**: Hostname and port number separated by a |
*   **mac-address**: Mac address
*   **mac-eui-64**: Mac EUI-64 address
*   **email-dst-display-name**: Email destination display name
*   **email-src-display-name**: Email source display name
*   **email-header**: Email header
*   **email-reply-to**: Email reply to header
*   **email-x-mailer**: Email x-mailer header
*   **email-mime-boundary**: The email mime boundary separating parts in a multipart email
*   **email-thread-index**: The email thread index header
*   **email-message-id**: The email message ID
*   **github-username**: A github user name
*   **github-repository**: A github repository
*   **github-organisation**: A github organisation
*   **jabber-id**: Jabber ID
*   **twitter-id**: Twitter ID
*   **dkim**: DKIM public key
*   **dkim-signature**: DKIM signature
*   **first-name**: First name of a natural person
*   **middle-name**: Middle name of a natural person
*   **last-name**: Last name of a natural person
*   **full-name**: Full name of a natural person
*   **date-of-birth**: Date of birth of a natural person (in YYYY-MM-DD format)
*   **place-of-birth**: Place of birth of a natural person
*   **gender**: The gender of a natural person (Male, Female, Other, Prefer not to say)
*   **passport-number**: The passport number of a natural person
*   **passport-country**: The country in which the passport was issued
*   **passport-expiration**: The expiration date of a passport
*   **redress-number**: The Redress Control Number is the record identifier for people who apply for redress through the DHS Travel Redress Inquiry Program (DHS TRIP). DHS TRIP is for travelers who have been repeatedly identified for additional screening and who want to file an inquiry to have erroneous information corrected in DHS systems
*   **nationality**: The nationality of a natural person
*   **visa-number**: Visa number
*   **issue-date-of-the-visa**: The date on which the visa was issued
*   **primary-residence**: The primary residence of a natural person
*   **country-of-residence**: The country of residence of a natural person
*   **special-service-request**: A Special Service Request is a function to an airline to provide a particular facility for A Passenger or passengers.
*   **frequent-flyer-number**: The frequent flyer number of a passenger
*   **travel-details**: Travel details
*   **payment-details**: Payment details
*   **place-port-of-original-embarkation**: The original port of embarkation
*   **place-port-of-clearance**: The port of clearance
*   **place-port-of-onward-foreign-destination**: A Port where the passenger is transiting to
*   **passenger-name-record-locator-number**: The Passenger Name Record Locator is a key under which the reservation for a trip is stored in the system. The PNR contains, among other data, the name, flight segments and address of the passenger. It is defined by a combination of five or six letters and numbers.
*   **mobile-application-id**: The application id of a mobile application
*   **azure-application-id**: Azure Application ID.
*   **chrome-extension-id**: Chrome extension id
*   **cortex**: Cortex analysis result
*   **boolean**: Boolean value - to be used in objects
*   **anonymised**: Anonymised value - described with the anonymisation object via a relationship.

## MISP objects

MISP objects are in addition to MISP attributes to allow advanced combinations of attributes. The creation of these objects
and their associated attributes are based on real cyber security use-cases and existing practices in information sharing.
MISP objects are standardised under a simple templating format and are automatically available in MISP. A series of relationships
are also defined along with the objects which can be used to create relationships between objects.

The objects available can be [browsed via the web site](/objects.html) or downloaded as [PDF](/objects.pdf) or directly via the MISP software.

## MISP Taxonomies

Along with the core format, [MISP taxonomies](https://www.github.com/MISP/misp-taxonomies/) provide a set of already defined classifications modeling estimative language, CSIRTs/CERTs classifications, national classifications or threat model classification. The fixed taxonomies provide a practical method to tag efficiently events and attributes within a set of MISP instances where taxonomies can be easily cherry-picked or extended to meet the local requirements of an organization or a specific sharing community. When using MISP, the MISP taxonomies are available and can be freely used based on the community practises.

The taxonomies can be [browsed via the web site](/taxonomies.html) or downloaded as [PDF](/taxonomies.pdf) or via the MISP software.

### CERT-XLM

[CERT-XLM](https://github.com/MISP/misp-taxonomies/tree/main/CERT-XLM) :
CERT-XLM Security Incident Classification. [Overview](/taxonomies.html#_cert_xlm)

### DFRLab-dichotomies-of-disinformation

[DFRLab-dichotomies-of-disinformation](https://github.com/MISP/misp-taxonomies/tree/main/DFRLab-dichotomies-of-disinformation) :
DFRLab Dichotomies of Disinformation. [Overview](/taxonomies.html#_dfrlab_dichotomies_of_disinformation)

### DML

[DML](https://github.com/MISP/misp-taxonomies/tree/main/DML) :
The Detection Maturity Level (DML) model is a capability maturity model for referencing ones maturity in detecting cyber attacks.  It's designed for organizations who perform intel-driven detection and response and who put an emphasis on having a mature detection program. [Overview](/taxonomies.html#_dml)

### PAP

[PAP](https://github.com/MISP/misp-taxonomies/tree/main/PAP) :
The Permissible Actions Protocol - or short: PAP - was designed to indicate how the received information can be used. [Overview](/taxonomies.html#_pap)

### access-method

[access-method](https://github.com/MISP/misp-taxonomies/tree/main/access-method) :
The access method used to remotely access a system. [Overview](/taxonomies.html#_access_method)

### accessnow

[accessnow](https://github.com/MISP/misp-taxonomies/tree/main/accessnow) :
Access Now classification to classify an issue (such as security, human rights, youth rights). [Overview](/taxonomies.html#_accessnow)

### action-taken

[action-taken](https://github.com/MISP/misp-taxonomies/tree/main/action-taken) :
Action taken in the case of a security incident (CSIRT perspective). [Overview](/taxonomies.html#_action_taken)

### admiralty-scale

[admiralty-scale](https://github.com/MISP/misp-taxonomies/tree/main/admiralty-scale) :
The Admiralty Scale or Ranking (also called the NATO System) is used to rank the reliability of a source and the credibility of an information. Reference based on FM 2-22.3 (FM 34-52) HUMAN INTELLIGENCE COLLECTOR OPERATIONS and NATO documents. [Overview](/taxonomies.html#_admiralty_scale)

### adversary

[adversary](https://github.com/MISP/misp-taxonomies/tree/main/adversary) :
An overview and description of the adversary infrastructure [Overview](/taxonomies.html#_adversary)

### ais-marking

[ais-marking](https://github.com/MISP/misp-taxonomies/tree/main/ais-marking) :
The AIS Marking Schema implementation is maintained by the National Cybersecurity and Communication Integration Center (NCCIC) of the U.S. Department of Homeland Security (DHS) [Overview](/taxonomies.html#_ais_marking)

### analyst-assessment

[analyst-assessment](https://github.com/MISP/misp-taxonomies/tree/main/analyst-assessment) :
A series of assessment predicates describing the analyst capabilities to perform analysis. These assessment can be assigned by the analyst him/herself or by another party evaluating the analyst. [Overview](/taxonomies.html#_analyst_assessment)

### approved-category-of-action

[approved-category-of-action](https://github.com/MISP/misp-taxonomies/tree/main/approved-category-of-action) :
A pre-approved category of action for indicators being shared with partners (MIMIC). [Overview](/taxonomies.html#_approved_category_of_action)

### binary-class

[binary-class](https://github.com/MISP/misp-taxonomies/tree/main/binary-class) :
Custom taxonomy for types of binary file. [Overview](/taxonomies.html#_binary_class)

### cccs

[cccs](https://github.com/MISP/misp-taxonomies/tree/main/cccs) :
Internal taxonomy for CCCS. [Overview](/taxonomies.html#_cccs)

### circl

[circl](https://github.com/MISP/misp-taxonomies/tree/main/circl) :
CIRCL Taxonomy - Schemes of Classification in Incident Response and Detection [Overview](/taxonomies.html#_circl)

### coa

[coa](https://github.com/MISP/misp-taxonomies/tree/main/coa) :
Course of action taken within organization to discover, detect, deny, disrupt, degrade, deceive and/or destroy an attack. [Overview](/taxonomies.html#_coa)

### collaborative-intelligence

[collaborative-intelligence](https://github.com/MISP/misp-taxonomies/tree/main/collaborative-intelligence) :
Collaborative intelligence support language is a common language to support analysts to perform their analysis to get crowdsourced support when using threat intelligence sharing platform like MISP. The objective of this language is to advance collaborative analysis and to share earlier than later. [Overview](/taxonomies.html#_collaborative_intelligence)

### common-taxonomy

[common-taxonomy](https://github.com/MISP/misp-taxonomies/tree/main/common-taxonomy) :
Common Taxonomy for Law enforcement and CSIRTs [Overview](/taxonomies.html#_common_taxonomy)

### copine-scale

[copine-scale](https://github.com/MISP/misp-taxonomies/tree/main/copine-scale) :
The COPINE Scale is a rating system created in Ireland and used in the United Kingdom to categorise the severity of images of child sex abuse. The scale was developed by staff at the COPINE (Combating Paedophile Information Networks in Europe) project. The COPINE Project was founded in 1997, and is based in the Department of Applied Psychology, University College Cork, Ireland. [Overview](/taxonomies.html#_copine_scale)

### course-of-action

[course-of-action](https://github.com/MISP/misp-taxonomies/tree/main/course-of-action) :
A Course Of Action analysis considers six potential courses of action for the development of a cyber security capability. [Overview](/taxonomies.html#_course_of_action)

### cryptocurrency-threat

[cryptocurrency-threat](https://github.com/MISP/misp-taxonomies/tree/main/cryptocurrency-threat) :
Threats targetting cryptocurrency, based on CipherTrace report. [Overview](/taxonomies.html#_cryptocurrency_threat)

### csirt-americas

[csirt-americas](https://github.com/MISP/misp-taxonomies/tree/main/csirt-americas) :
Taxonomía CSIRT Américas. [Overview](/taxonomies.html#_csirt_americas)

### csirt_case_classification

[csirt_case_classification](https://github.com/MISP/misp-taxonomies/tree/main/csirt_case_classification) :
It is critical that the CSIRT provide consistent and timely response to the customer, and that sensitive information is handled appropriately.  This document provides the guidelines needed for CSIRT Incident Managers (IM) to classify the case category, criticality level, and sensitivity level for each CSIRT case.  This information will be entered into the Incident Tracking System (ITS) when a case is created.  Consistent case classification is required for the CSIRT to provide accurate reporting to management on a regular basis.  In addition, the classifications will provide CSIRT IM’s with proper case handling procedures and will form the basis of SLA’s between the CSIRT and other Company departments. [Overview](/taxonomies.html#_csirt_case_classification)

### cssa

[cssa](https://github.com/MISP/misp-taxonomies/tree/main/cssa) :
The CSSA agreed sharing taxonomy. [Overview](/taxonomies.html#_cssa)

### cti

[cti](https://github.com/MISP/misp-taxonomies/tree/main/cti) :
Cyber Threat Intelligence cycle to control workflow state of your process. [Overview](/taxonomies.html#_cti)

### current-event

[current-event](https://github.com/MISP/misp-taxonomies/tree/main/current-event) :
Current events - Schemes of Classification in Incident Response and Detection [Overview](/taxonomies.html#_current_event)

### cyber-threat-framework

[cyber-threat-framework](https://github.com/MISP/misp-taxonomies/tree/main/cyber-threat-framework) :
Cyber Threat Framework was developed by the US Government to enable consistent characterization and categorization of cyber threat events, and to identify trends or changes in the activities of cyber adversaries. https://www.dni.gov/index.php/cyber-threat-framework [Overview](/taxonomies.html#_cyber_threat_framework)

### cycat

[cycat](https://github.com/MISP/misp-taxonomies/tree/main/cycat) :
Taxonomy used by CyCAT, the Universal Cybersecurity Resource Catalogue, to categorize the namespaces it supports and uses. [Overview](/taxonomies.html#_cycat)

### cytomic-orion

[cytomic-orion](https://github.com/MISP/misp-taxonomies/tree/main/cytomic-orion) :
Taxonomy to describe desired actions for Cytomic Orion [Overview](/taxonomies.html#_cytomic_orion)

### dark-web

[dark-web](https://github.com/MISP/misp-taxonomies/tree/main/dark-web) :
Criminal motivation on the dark web: A categorisation model for law enforcement. ref: Janis Dalins, Campbell Wilson, Mark Carman. Taxonomy updated by MISP Project [Overview](/taxonomies.html#_dark_web)

### data-classification

[data-classification](https://github.com/MISP/misp-taxonomies/tree/main/data-classification) :
Data classification for data potentially at risk of exfiltration based on table 2.1 of Solving Cyber Risk book. [Overview](/taxonomies.html#_data_classification)

### dcso-sharing

[dcso-sharing](https://github.com/MISP/misp-taxonomies/tree/main/dcso-sharing) :
Taxonomy defined in the DCSO MISP Event Guide. It provides guidance for the creation and consumption of MISP events in a way that minimises the extra effort for the sending party, while enhancing the usefulness for receiving parties. [Overview](/taxonomies.html#_dcso_sharing)

### ddos

[ddos](https://github.com/MISP/misp-taxonomies/tree/main/ddos) :
Distributed Denial of Service - or short: DDoS - taxonomy supports the description of Denial of Service attacks and especially the types they belong too. [Overview](/taxonomies.html#_ddos)

### de-vs

[de-vs](https://github.com/MISP/misp-taxonomies/tree/main/de-vs) :
German (DE) Government classification markings (VS). [Overview](/taxonomies.html#_de_vs)

### deception

[deception](https://github.com/MISP/misp-taxonomies/tree/main/deception) :
Deception is an important component of information operations, valuable for both offense and defense.  [Overview](/taxonomies.html#_deception)

### dhs-ciip-sectors

[dhs-ciip-sectors](https://github.com/MISP/misp-taxonomies/tree/main/dhs-ciip-sectors) :
DHS critical sectors as in https://www.dhs.gov/critical-infrastructure-sectors [Overview](/taxonomies.html#_dhs_ciip_sectors)

### diamond-model

[diamond-model](https://github.com/MISP/misp-taxonomies/tree/main/diamond-model) :
The Diamond Model for Intrusion Analysis establishes the basic atomic element of any intrusion activity, the event, composed of four core features: adversary, infrastructure, capability, and victim. [Overview](/taxonomies.html#_diamond_model)

### dni-ism

[dni-ism](https://github.com/MISP/misp-taxonomies/tree/main/dni-ism) :
A subset of Information Security Marking Metadata ISM as required by Executive Order (EO) 13526. As described by DNI.gov as Data Encoding Specifications for Information Security Marking Metadata in Controlled Vocabulary Enumeration Values for ISM [Overview](/taxonomies.html#_dni_ism)

### domain-abuse

[domain-abuse](https://github.com/MISP/misp-taxonomies/tree/main/domain-abuse) :
Domain Name Abuse - taxonomy to tag domain names used for cybercrime. [Overview](/taxonomies.html#_domain_abuse)

### drugs

[drugs](https://github.com/MISP/misp-taxonomies/tree/main/drugs) :
A taxonomy based on the superclass and class of drugs. Based on https://www.drugbank.ca/releases/latest [Overview](/taxonomies.html#_drugs)

### economical-impact

[economical-impact](https://github.com/MISP/misp-taxonomies/tree/main/economical-impact) :
Economical impact is a taxonomy to describe the financial impact as positive or negative gain to the tagged information (e.g. data exfiltration loss, a positive gain for an adversary). [Overview](/taxonomies.html#_economical_impact)

### ecsirt

[ecsirt](https://github.com/MISP/misp-taxonomies/tree/main/ecsirt) :
Incident Classification by the ecsirt.net version mkVI of 31 March 2015 enriched with IntelMQ taxonomy-type mapping. [Overview](/taxonomies.html#_ecsirt)

### enisa

[enisa](https://github.com/MISP/misp-taxonomies/tree/main/enisa) :
The present threat taxonomy is an initial version that has been developed on the basis of available ENISA material. This material has been used as an ENISA-internal structuring aid for information collection and threat consolidation purposes. It emerged in the time period 2012-2015. [Overview](/taxonomies.html#_enisa)

### estimative-language

[estimative-language](https://github.com/MISP/misp-taxonomies/tree/main/estimative-language) :
Estimative language to describe quality and credibility of underlying sources, data, and methodologies based Intelligence Community Directive 203 (ICD 203) and JP 2-0, Joint Intelligence [Overview](/taxonomies.html#_estimative_language)

### eu-marketop-and-publicadmin

[eu-marketop-and-publicadmin](https://github.com/MISP/misp-taxonomies/tree/main/eu-marketop-and-publicadmin) :
Market operators and public administrations that must comply to some notifications requirements under EU NIS directive [Overview](/taxonomies.html#_eu_marketop_and_publicadmin)

### eu-nis-sector-and-subsectors

[eu-nis-sector-and-subsectors](https://github.com/MISP/misp-taxonomies/tree/main/eu-nis-sector-and-subsectors) :
Sectors, subsectors, and digital services as identified by the NIS Directive [Overview](/taxonomies.html#_eu_nis_sector_and_subsectors)

### euci

[euci](https://github.com/MISP/misp-taxonomies/tree/main/euci) :
EU classified information (EUCI) means any information or material designated by a EU security classification, the unauthorised disclosure of which could cause varying degrees of prejudice to the interests of the European Union or of one or more of the Member States. [Overview](/taxonomies.html#_euci)

### europol-event

[europol-event](https://github.com/MISP/misp-taxonomies/tree/main/europol-event) :
This taxonomy was designed to describe the type of events [Overview](/taxonomies.html#_europol_event)

### europol-incident

[europol-incident](https://github.com/MISP/misp-taxonomies/tree/main/europol-incident) :
This taxonomy was designed to describe the type of incidents by class. [Overview](/taxonomies.html#_europol_incident)

### event-assessment

[event-assessment](https://github.com/MISP/misp-taxonomies/tree/main/event-assessment) :
A series of assessment predicates describing the event assessment performed to make judgement(s) under a certain level of uncertainty. [Overview](/taxonomies.html#_event_assessment)

### event-classification

[event-classification](https://github.com/MISP/misp-taxonomies/tree/main/event-classification) :
Classification of events as seen in tools such as RT/IR, MISP and other [Overview](/taxonomies.html#_event_classification)

### exercise

[exercise](https://github.com/MISP/misp-taxonomies/tree/main/exercise) :
Exercise is a taxonomy to describe if the information is part of one or more cyber or crisis exercise. [Overview](/taxonomies.html#_exercise)

### extended-event

[extended-event](https://github.com/MISP/misp-taxonomies/tree/main/extended-event) :
Reasons why an event has been extended.  [Overview](/taxonomies.html#_extended_event)

### failure-mode-in-machine-learning

[failure-mode-in-machine-learning](https://github.com/MISP/misp-taxonomies/tree/main/failure-mode-in-machine-learning) :
The purpose of this taxonomy is to jointly tabulate both the of these failure modes in a single place. Intentional failures wherein the failure is caused by an active adversary attempting to subvert the system to attain her goals – either to misclassify the result, infer private training data, or to steal the underlying algorithm. Unintentional failures wherein the failure is because an ML system produces a formally correct but completely unsafe outcome. [Overview](/taxonomies.html#_failure_mode_in_machine_learning)

### false-positive

[false-positive](https://github.com/MISP/misp-taxonomies/tree/main/false-positive) :
This taxonomy aims to ballpark the expected amount of false positives. [Overview](/taxonomies.html#_false_positive)

### file-type

[file-type](https://github.com/MISP/misp-taxonomies/tree/main/file-type) :
List of known file types. [Overview](/taxonomies.html#_file_type)

### flesch-reading-ease

[flesch-reading-ease](https://github.com/MISP/misp-taxonomies/tree/main/flesch-reading-ease) :
Flesch Reading Ease is a revised system for determining the comprehension difficulty of written material. The scoring of the flesh score can have a maximum of 121.22 and there is no limit on how low a score can be (negative score are valid). [Overview](/taxonomies.html#_flesch_reading_ease)

### fpf

[fpf](https://github.com/MISP/misp-taxonomies/tree/main/fpf) :
The Future of Privacy Forum (FPF) [visual guide to practical de-identification](https://fpf.org/2016/04/25/a-visual-guide-to-practical-data-de-identification/) taxonomy is used to evaluate the degree of identifiability of personal data and the types of pseudonymous data, de-identified data and anonymous data. The work of FPF is licensed under a creative commons attribution 4.0 international license. [Overview](/taxonomies.html#_fpf)

### fr-classif

[fr-classif](https://github.com/MISP/misp-taxonomies/tree/main/fr-classif) :
French gov information classification system [Overview](/taxonomies.html#_fr_classif)

### gdpr

[gdpr](https://github.com/MISP/misp-taxonomies/tree/main/gdpr) :
Taxonomy related to the REGULATION (EU) 2016/679 OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL on the protection of natural persons with regard to the processing of personal data and on the free movement of such data, and repealing Directive 95/46/EC (General Data Protection Regulation) [Overview](/taxonomies.html#_gdpr)

### gea-nz-activities

[gea-nz-activities](https://github.com/MISP/misp-taxonomies/tree/main/gea-nz-activities) :
Information needed to track or monitor moments, periods or events that occur over time. This type of information is focused on occurrences that must be tracked for business reasons or represent a specific point in the evolution of ‘The Business’. [Overview](/taxonomies.html#_gea_nz_activities)

### gea-nz-entities

[gea-nz-entities](https://github.com/MISP/misp-taxonomies/tree/main/gea-nz-entities) :
Information relating to instances of entities or things. [Overview](/taxonomies.html#_gea_nz_entities)

### gea-nz-motivators

[gea-nz-motivators](https://github.com/MISP/misp-taxonomies/tree/main/gea-nz-motivators) :
Information relating to authority or governance. [Overview](/taxonomies.html#_gea_nz_motivators)

### gsma-attack-category

[gsma-attack-category](https://github.com/MISP/misp-taxonomies/tree/main/gsma-attack-category) :
Taxonomy used by GSMA for their information sharing program with telco describing the attack categories [Overview](/taxonomies.html#_gsma_attack_category)

### gsma-fraud

[gsma-fraud](https://github.com/MISP/misp-taxonomies/tree/main/gsma-fraud) :
Taxonomy used by GSMA for their information sharing program with telco describing the various aspects of fraud [Overview](/taxonomies.html#_gsma_fraud)

### gsma-network-technology

[gsma-network-technology](https://github.com/MISP/misp-taxonomies/tree/main/gsma-network-technology) :
Taxonomy used by GSMA for their information sharing program with telco describing the types of infrastructure. WiP [Overview](/taxonomies.html#_gsma_network_technology)

### honeypot-basic

[honeypot-basic](https://github.com/MISP/misp-taxonomies/tree/main/honeypot-basic) :
Updated (CIRCL, Seamus Dowling and EURECOM) from Christian Seifert, Ian Welch, Peter Komisarczuk, ‘Taxonomy of Honeypots’, Technical Report CS-TR-06/12, VICTORIA UNIVERSITY OF WELLINGTON, School of Mathematical and Computing Sciences, June 2006, http://www.mcs.vuw.ac.nz/comp/Publications/archive/CS-TR-06/CS-TR-06-12.pdf [Overview](/taxonomies.html#_honeypot_basic)

### ics

[ics](https://github.com/MISP/misp-taxonomies/tree/main/ics) :
FIRST.ORG CTI SIG - MISP Proposal for ICS/OT Threat Attribution (IOC) Project [Overview](/taxonomies.html#_ics)

### iep

[iep](https://github.com/MISP/misp-taxonomies/tree/main/iep) :
Forum of Incident Response and Security Teams (FIRST) Information Exchange Policy (IEP) framework [Overview](/taxonomies.html#_iep)

### iep2-policy

[iep2-policy](https://github.com/MISP/misp-taxonomies/tree/main/iep2-policy) :
Forum of Incident Response and Security Teams (FIRST) Information Exchange Policy (IEP) v2.0 Policy [Overview](/taxonomies.html#_iep2_policy)

### iep2-reference

[iep2-reference](https://github.com/MISP/misp-taxonomies/tree/main/iep2-reference) :
Forum of Incident Response and Security Teams (FIRST) Information Exchange Policy (IEP) v2.0 Reference [Overview](/taxonomies.html#_iep2_reference)

### ifx-vetting

[ifx-vetting](https://github.com/MISP/misp-taxonomies/tree/main/ifx-vetting) :
The IFX taxonomy is used to categorise information (MISP events and attributes) to aid in the intelligence vetting process [Overview](/taxonomies.html#_ifx_vetting)

### incident-disposition

[incident-disposition](https://github.com/MISP/misp-taxonomies/tree/main/incident-disposition) :
How an incident is classified in its process to be resolved. The taxonomy is inspired from NASA Incident Response and Management Handbook. https://www.nasa.gov/pdf/589502main_ITS-HBK-2810.09-02%20%5bNASA%20Information%20Security%20Incident%20Management%5d.pdf#page=9 [Overview](/taxonomies.html#_incident_disposition)

### infoleak

[infoleak](https://github.com/MISP/misp-taxonomies/tree/main/infoleak) :
A taxonomy describing information leaks and especially information classified as being potentially leaked. The taxonomy is based on the work by CIRCL on the AIL framework. The taxonomy aim is to be used at large to improve classification of leaked information. [Overview](/taxonomies.html#_infoleak)

### information-security-data-source

[information-security-data-source](https://github.com/MISP/misp-taxonomies/tree/main/information-security-data-source) :
Taxonomy to classify the information security data sources. [Overview](/taxonomies.html#_information_security_data_source)

### information-security-indicators

[information-security-indicators](https://github.com/MISP/misp-taxonomies/tree/main/information-security-indicators) :
A full set of operational indicators for organizations to use to benchmark their security posture. [Overview](/taxonomies.html#_information_security_indicators)

### interactive-cyber-training-audience

[interactive-cyber-training-audience](https://github.com/MISP/misp-taxonomies/tree/main/interactive-cyber-training-audience) :
Describes the target of cyber training and education. [Overview](/taxonomies.html#_interactive_cyber_training_audience)

### interactive-cyber-training-technical-setup

[interactive-cyber-training-technical-setup](https://github.com/MISP/misp-taxonomies/tree/main/interactive-cyber-training-technical-setup) :
The technical setup consists of environment structure, deployment, and orchestration. [Overview](/taxonomies.html#_interactive_cyber_training_technical_setup)

### interactive-cyber-training-training-environment

[interactive-cyber-training-training-environment](https://github.com/MISP/misp-taxonomies/tree/main/interactive-cyber-training-training-environment) :
The training environment details the environment around the training, consisting of training type and scenario. [Overview](/taxonomies.html#_interactive_cyber_training_training_environment)

### interactive-cyber-training-training-setup

[interactive-cyber-training-training-setup](https://github.com/MISP/misp-taxonomies/tree/main/interactive-cyber-training-training-setup) :
The training setup further describes the training itself with the scoring, roles, the training mode as well as the customization level. [Overview](/taxonomies.html#_interactive_cyber_training_training_setup)

### interception-method

[interception-method](https://github.com/MISP/misp-taxonomies/tree/main/interception-method) :
The interception method used to intercept traffic. [Overview](/taxonomies.html#_interception_method)

### ioc

[ioc](https://github.com/MISP/misp-taxonomies/tree/main/ioc) :
An IOC classification to facilitate automation of malicious and non malicious artifacts [Overview](/taxonomies.html#_ioc)

### iot

[iot](https://github.com/MISP/misp-taxonomies/tree/main/iot) :
Internet of Things taxonomy, based on IOT UK report https://iotuk.org.uk/wp-content/uploads/2017/01/IOT-Taxonomy-Report.pdf [Overview](/taxonomies.html#_iot)

### kill-chain

[kill-chain](https://github.com/MISP/misp-taxonomies/tree/main/kill-chain) :
The Cyber Kill Chain, a phase-based model developed by Lockheed Martin, aims to help categorise and identify the stage of an attack. [Overview](/taxonomies.html#_kill_chain)

### maec-delivery-vectors

[maec-delivery-vectors](https://github.com/MISP/misp-taxonomies/tree/main/maec-delivery-vectors) :
Vectors used to deliver malware based on MAEC 5.0 [Overview](/taxonomies.html#_maec_delivery_vectors)

### maec-malware-behavior

[maec-malware-behavior](https://github.com/MISP/misp-taxonomies/tree/main/maec-malware-behavior) :
Malware behaviours based on MAEC 5.0 [Overview](/taxonomies.html#_maec_malware_behavior)

### maec-malware-capabilities

[maec-malware-capabilities](https://github.com/MISP/misp-taxonomies/tree/main/maec-malware-capabilities) :
Malware Capabilities based on MAEC 5.0 [Overview](/taxonomies.html#_maec_malware_capabilities)

### maec-malware-obfuscation-methods

[maec-malware-obfuscation-methods](https://github.com/MISP/misp-taxonomies/tree/main/maec-malware-obfuscation-methods) :
Obfuscation methods used by malware based on MAEC 5.0 [Overview](/taxonomies.html#_maec_malware_obfuscation_methods)

### malware_classification

[malware_classification](https://github.com/MISP/misp-taxonomies/tree/main/malware_classification) :
Classification based on different categories. Based on https://www.sans.org/reading-room/whitepapers/incident/malware-101-viruses-32848 [Overview](/taxonomies.html#_malware_classification)

### misinformation-website-label

[misinformation-website-label](https://github.com/MISP/misp-taxonomies/tree/main/misinformation-website-label) :
classification for the identification of type of misinformation among websites. Source:False, Misleading, Clickbait-y, and/or Satirical News Sources by Melissa Zimdars 2019 [Overview](/taxonomies.html#_misinformation_website_label)

### misp

[misp](https://github.com/MISP/misp-taxonomies/tree/main/misp) :
MISP taxonomy to infer with MISP behavior or operation. [Overview](/taxonomies.html#_misp)

### monarc-threat

[monarc-threat](https://github.com/MISP/misp-taxonomies/tree/main/monarc-threat) :
MONARC Threats Taxonomy [Overview](/taxonomies.html#_monarc_threat)

### ms-caro-malware

[ms-caro-malware](https://github.com/MISP/misp-taxonomies/tree/main/ms-caro-malware) :
Malware Type and Platform classification based on Microsoft's implementation of the Computer Antivirus Research Organization (CARO) Naming Scheme and Malware Terminology. Based on https://www.microsoft.com/en-us/security/portal/mmpc/shared/malwarenaming.aspx, https://www.microsoft.com/security/portal/mmpc/shared/glossary.aspx, https://www.microsoft.com/security/portal/mmpc/shared/objectivecriteria.aspx, and http://www.caro.org/definitions/index.html. Malware families are extracted from Microsoft SIRs since 2008 based on https://www.microsoft.com/security/sir/archive/default.aspx and https://www.microsoft.com/en-us/security/portal/threat/threats.aspx. Note that SIRs do NOT include all Microsoft malware families. [Overview](/taxonomies.html#_ms_caro_malware)

### ms-caro-malware-full

[ms-caro-malware-full](https://github.com/MISP/misp-taxonomies/tree/main/ms-caro-malware-full) :
Malware Type and Platform classification based on Microsoft's implementation of the Computer Antivirus Research Organization (CARO) Naming Scheme and Malware Terminology. Based on https://www.microsoft.com/en-us/security/portal/mmpc/shared/malwarenaming.aspx, https://www.microsoft.com/security/portal/mmpc/shared/glossary.aspx, https://www.microsoft.com/security/portal/mmpc/shared/objectivecriteria.aspx, and http://www.caro.org/definitions/index.html. Malware families are extracted from Microsoft SIRs since 2008 based on https://www.microsoft.com/security/sir/archive/default.aspx and https://www.microsoft.com/en-us/security/portal/threat/threats.aspx. Note that SIRs do NOT include all Microsoft malware families. [Overview](/taxonomies.html#_ms_caro_malware_full)

### mwdb

[mwdb](https://github.com/MISP/misp-taxonomies/tree/main/mwdb) :
Malware Database (mwdb) Taxonomy - Tags used across the platform [Overview](/taxonomies.html#_mwdb)

### nato

[nato](https://github.com/MISP/misp-taxonomies/tree/main/nato) :
NATO classification markings. [Overview](/taxonomies.html#_nato)

### nis

[nis](https://github.com/MISP/misp-taxonomies/tree/main/nis) :
The taxonomy is meant for large scale cybersecurity incidents, as mentioned in the Commission Recommendation of 13 September 2017, also known as the blueprint. It has two core parts: The nature of the incident, i.e. the underlying cause, that triggered the incident, and the impact of the incident, i.e. the impact on services, in which sector(s) of economy and society. [Overview](/taxonomies.html#_nis)

### open_threat

[open_threat](https://github.com/MISP/misp-taxonomies/tree/main/open_threat) :
Open Threat Taxonomy v1.1 base on James Tarala of SANS http://www.auditscripts.com/resources/open_threat_taxonomy_v1.1a.pdf, https://files.sans.org/summit/Threat_Hunting_Incident_Response_Summit_2016/PDFs/Using-Open-Tools-to-Convert-Threat-Intelligence-into-Practical-Defenses-James-Tarala-SANS-Institute.pdf, https://www.youtube.com/watch?v=5rdGOOFC_yE, and https://www.rsaconference.com/writable/presentations/file_upload/str-r04_using-an-open-source-threat-model-for-prioritized-defense-final.pdf [Overview](/taxonomies.html#_open_threat)

### osint

[osint](https://github.com/MISP/misp-taxonomies/tree/main/osint) :
Open Source Intelligence - Classification (MISP taxonomies) [Overview](/taxonomies.html#_osint)

### pandemic

[pandemic](https://github.com/MISP/misp-taxonomies/tree/main/pandemic) :
Pandemic [Overview](/taxonomies.html#_pandemic)

### passivetotal

[passivetotal](https://github.com/MISP/misp-taxonomies/tree/main/passivetotal) :
Tags from RiskIQ's PassiveTotal service [Overview](/taxonomies.html#_passivetotal)

### pentest

[pentest](https://github.com/MISP/misp-taxonomies/tree/main/pentest) :
Penetration test (pentest) classification. [Overview](/taxonomies.html#_pentest)

### phishing

[phishing](https://github.com/MISP/misp-taxonomies/tree/main/phishing) :
Taxonomy to classify phishing attacks including techniques, collection mechanisms and analysis status. [Overview](/taxonomies.html#_phishing)

### political-spectrum

[political-spectrum](https://github.com/MISP/misp-taxonomies/tree/main/political-spectrum) :
political spectrum is a system to characterize and classify different political positions [Overview](/taxonomies.html#_political_spectrum)

### priority-level

[priority-level](https://github.com/MISP/misp-taxonomies/tree/main/priority-level) :
After an incident is scored, it is assigned a priority level. The six levels listed below are aligned with NCCIC, DHS, and the CISS to help provide a common lexicon when discussing incidents. This priority assignment drives NCCIC urgency, pre-approved incident response offerings, reporting requirements, and recommendations for leadership escalation. Generally, incident priority distribution should follow a similar pattern to the graph below. Based on https://www.us-cert.gov/NCCIC-Cyber-Incident-Scoring-System. [Overview](/taxonomies.html#_priority_level)

### ransomware

[ransomware](https://github.com/MISP/misp-taxonomies/tree/main/ransomware) :
Ransomware is used to define ransomware types and the elements that compose them. [Overview](/taxonomies.html#_ransomware)

### retention

[retention](https://github.com/MISP/misp-taxonomies/tree/main/retention) :
Add a retenion time to events to automatically remove the IDS-flag on ip-dst or ip-src attributes. We calculate the time elapsed based on the date of the event. Supported time units are: d(ays), w(eeks), m(onths), y(ears). The numerical_value is just for sorting in the web-interface and is not used for calculations. [Overview](/taxonomies.html#_retention)

### rsit

[rsit](https://github.com/MISP/misp-taxonomies/tree/main/rsit) :
Reference Security Incident Classification Taxonomy [Overview](/taxonomies.html#_rsit)

### rt_event_status

[rt_event_status](https://github.com/MISP/misp-taxonomies/tree/main/rt_event_status) :
Status of events used in Request Tracker. [Overview](/taxonomies.html#_rt_event_status)

### runtime-packer

[runtime-packer](https://github.com/MISP/misp-taxonomies/tree/main/runtime-packer) :
Runtime or software packer used to combine compressed data with the decompression code. The decompression code can add additional obfuscations mechanisms including polymorphic-packer or other obfuscation techniques. This taxonomy lists all the known or official packer used for legitimate use or for packing malicious binaries. [Overview](/taxonomies.html#_runtime_packer)

### scrippsco2-fgc

[scrippsco2-fgc](https://github.com/MISP/misp-taxonomies/tree/main/scrippsco2-fgc) :
Flags describing the sample [Overview](/taxonomies.html#_scrippsco2_fgc)

### scrippsco2-fgi

[scrippsco2-fgi](https://github.com/MISP/misp-taxonomies/tree/main/scrippsco2-fgi) :
Flags describing the sample for isotopic data (C14, O18) [Overview](/taxonomies.html#_scrippsco2_fgi)

### scrippsco2-sampling-stations

[scrippsco2-sampling-stations](https://github.com/MISP/misp-taxonomies/tree/main/scrippsco2-sampling-stations) :
Sampling stations of the Scripps CO2 Program [Overview](/taxonomies.html#_scrippsco2_sampling_stations)

### smart-airports-threats

[smart-airports-threats](https://github.com/MISP/misp-taxonomies/tree/main/smart-airports-threats) :
Threat taxonomy in the scope of securing smart airports by ENISA. https://www.enisa.europa.eu/publications/securing-smart-airports [Overview](/taxonomies.html#_smart_airports_threats)

### stealth_malware

[stealth_malware](https://github.com/MISP/misp-taxonomies/tree/main/stealth_malware) :
Classification based on malware stealth techniques. Described in https://vxheaven.org/lib/pdf/Introducing%20Stealth%20Malware%20Taxonomy.pdf [Overview](/taxonomies.html#_stealth_malware)

### stix-ttp

[stix-ttp](https://github.com/MISP/misp-taxonomies/tree/main/stix-ttp) :
TTPs are representations of the behavior or modus operandi of cyber adversaries. [Overview](/taxonomies.html#_stix_ttp)

### targeted-threat-index

[targeted-threat-index](https://github.com/MISP/misp-taxonomies/tree/main/targeted-threat-index) :
The Targeted Threat Index is a metric for assigning an overall threat ranking score to email messages that deliver malware to a victim’s computer. The TTI metric was first introduced at SecTor 2013 by Seth Hardy as part of the talk “RATastrophe: Monitoring a Malware Menagerie” along with Katie Kleemola and Greg Wiseman. [Overview](/taxonomies.html#_targeted_threat_index)

### thales_group

[thales_group](https://github.com/MISP/misp-taxonomies/tree/main/thales_group) :
Thales Group Taxonomy - was designed with the aim of enabling desired sharing and preventing unwanted sharing between Thales Group security communities. [Overview](/taxonomies.html#_thales_group)

### threatmatch

[threatmatch](https://github.com/MISP/misp-taxonomies/tree/main/threatmatch) :
The ThreatMatch Sectors, Incident types, Malware types and Alert types are applicable for any ThreatMatch instances and should be used for all CIISI and TIBER Projects. [Overview](/taxonomies.html#_threatmatch)

### threats-to-dns

[threats-to-dns](https://github.com/MISP/misp-taxonomies/tree/main/threats-to-dns) :
An overview of some of the known attacks related to DNS as described by Torabi, S., Boukhtouta, A., Assi, C., & Debbabi, M. (2018) in Detecting Internet Abuse by Analyzing Passive DNS Traffic: A Survey of Implemented Systems. IEEE Communications Surveys & Tutorials, 1–1. doi:10.1109/comst.2018.2849614 [Overview](/taxonomies.html#_threats_to_dns)

### tlp

[tlp](https://github.com/MISP/misp-taxonomies/tree/main/tlp) :
The Traffic Light Protocol - or short: TLP - was designed with the objective to create a favorable classification scheme for sharing sensitive information while keeping the control over its distribution at the same time. [Overview](/taxonomies.html#_tlp)

### tor

[tor](https://github.com/MISP/misp-taxonomies/tree/main/tor) :
Taxonomy to describe Tor network infrastructure [Overview](/taxonomies.html#_tor)

### trust

[trust](https://github.com/MISP/misp-taxonomies/tree/main/trust) :
The Indicator of Trust provides insight about data on what can be trusted and known as a good actor. Similar to a whitelist but on steroids, reusing features one would use with Indicators of Compromise, but to filter out what is known to be good. [Overview](/taxonomies.html#_trust)

### type

[type](https://github.com/MISP/misp-taxonomies/tree/main/type) :
Taxonomy to describe different types of intelligence gathering discipline which can be described the origin of intelligence. [Overview](/taxonomies.html#_type)

### unified-kill-chain

[unified-kill-chain](https://github.com/MISP/misp-taxonomies/tree/main/unified-kill-chain) :
The Unified Kill Chain is a refinement to the Kill Chain. [Overview](/taxonomies.html#_unified_kill_chain)

### use-case-applicability

[use-case-applicability](https://github.com/MISP/misp-taxonomies/tree/main/use-case-applicability) :
The Use Case Applicability categories reflect standard resolution categories, to clearly display alerting rule configuration problems. [Overview](/taxonomies.html#_use_case_applicability)

### veris

[veris](https://github.com/MISP/misp-taxonomies/tree/main/veris) :
Vocabulary for Event Recording and Incident Sharing (VERIS) [Overview](/taxonomies.html#_veris)

### vmray

[vmray](https://github.com/MISP/misp-taxonomies/tree/main/vmray) :
VMRay taxonomies to map VMRay Thread Identifier scores and artifacts. [Overview](/taxonomies.html#_vmray)

### vocabulaire-des-probabilites-estimatives

[vocabulaire-des-probabilites-estimatives](https://github.com/MISP/misp-taxonomies/tree/main/vocabulaire-des-probabilites-estimatives) :
Ce vocabulaire attribue des valeurs en pourcentage à certains énoncés de probabilité [Overview](/taxonomies.html#_vocabulaire_des_probabilites_estimatives)

### workflow

[workflow](https://github.com/MISP/misp-taxonomies/tree/main/workflow) :
Workflow support language is a common language to support intelligence analysts to perform their analysis on data and information. [Overview](/taxonomies.html#_workflow)

## MISP Galaxy

MISP galaxy is a simple method to express a large object called cluster that can be attached to MISP events or attributes. A cluster can be composed of one or more elements. Elements are expressed as key-values. There are default vocabularies available in MISP galaxy but those can be overwritten, replaced or updated as you wish. Existing clusters and vocabularies can be used as-is or as a template. MISP distribution can be applied to each cluster to permit a limited or broader distribution scheme. Many MISP galaxy clusters are already available like Exploit-Kit, Microsoft Activity Group actor, Preventive Measure, 
Ransomware, TDS, Threat actor or Tool used by adversaries.

The galaxy can be [browsed via the web site](/galaxy.html) or downloaded as [PDF](/galaxy.pdf) or directly via the MISP software.
