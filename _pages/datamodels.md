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

|Category| Antivirus detection | Artifacts dropped | Attribution | External analysis | Financial fraud | Internal reference |
| --- |:---:|:---:|:---:|:---:|:---:|:---:|
|AS| | | | X | | |
|aba-rtn| | | | | X | |
|anonymised| X | X | X | X | X | X |
|attachment| X | X | | X | | |
|authentihash| | X | | | | |
|bank-account-nr| | | | | X | |
|bic| | | | | X | |
|bin| | | | | X | |
|boolean| | | | | | |
|bro| | | | X | | |
|btc| | | | | X | |
|campaign-id| | | X | | | |
|campaign-name| | | X | | | |
|cc-number| | | | | X | |
|cdhash| | X | | | | |
|chrome-extension-id| | | | | | |
|comment| X | X | X | X | X | X |
|community-id| | | | X | | |
|cookie| | X | | | | |
|cortex| | | | X | | |
|counter| | | | | | |
|country-of-residence| | | | | | |
|cpe| | | | | | |
|dash| | | | | X | |
|date-of-birth| | | | | | |
|datetime| | | | | | |
|dns-soa-email| | | X | | | |
|domain| | | | X | | |
|domain&#124;ip| | | | X | | |
|email| | | X | | | |
|email-attachment| | | | | | |
|email-body| | | | | | |
|email-dst| | | | | | |
|email-dst-display-name| | | | | | |
|email-header| | | | | | |
|email-message-id| | | | | | |
|email-mime-boundary| | | | | | |
|email-reply-to| | | | | | |
|email-src| | | | | | |
|email-src-display-name| | | | | | |
|email-subject| | | | | | |
|email-thread-index| | | | | | |
|email-x-mailer| | | | | | |
|eppn| | | | | | |
|filename| | X | | X | | |
|filename&#124;authentihash| | X | | | | |
|filename&#124;impfuzzy| | X | | | | |
|filename&#124;imphash| | X | | | | |
|filename&#124;md5| | X | | X | | |
|filename&#124;pehash| | X | | | | |
|filename&#124;sha1| | X | | X | | |
|filename&#124;sha224| | X | | | | |
|filename&#124;sha256| | X | | X | | |
|filename&#124;sha3-224| | X | | X | | |
|filename&#124;sha3-256| | X | | X | | |
|filename&#124;sha3-384| | X | | X | | |
|filename&#124;sha3-512| | X | | X | | |
|filename&#124;sha384| | X | | | | |
|filename&#124;sha512| | X | | | | |
|filename&#124;sha512/224| | X | | | | |
|filename&#124;sha512/256| | X | | | | |
|filename&#124;ssdeep| | X | | | | |
|filename&#124;tlsh| | X | | | | |
|filename&#124;vhash| | X | | | | |
|first-name| | | | | | |
|float| | | | | | |
|frequent-flyer-number| | | | | | |
|gender| | | | | | |
|gene| | X | | | | |
|git-commit-id| | | | | | X |
|github-organisation| | | | | | |
|github-repository| | | | X | | |
|github-username| | | | | | |
|hassh-md5| | | | X | | |
|hasshserver-md5| | | | X | | |
|hex| X | X | | | X | X |
|hostname| | | | X | | |
|hostname&#124;port| | | | | | |
|http-method| | | | | | |
|iban| | | | | X | |
|identity-card-number| | | | | | |
|impfuzzy| | X | | | | |
|imphash| | X | | | | |
|ip-dst| | | | X | | |
|ip-dst&#124;port| | | | X | | |
|ip-src| | | | X | | |
|ip-src&#124;port| | | | X | | |
|issue-date-of-the-visa| | | | | | |
|ja3-fingerprint-md5| | | | X | | |
|jabber-id| | | | | | |
|kusto-query| | X | | | | |
|last-name| | | | | | |
|link| X | | | X | | X |
|mac-address| | | | X | | |
|mac-eui-64| | | | X | | |
|malware-sample| | X | | X | | |
|malware-type| | | | | | |
|md5| | X | | X | | |
|middle-name| | | | | | |
|mime-type| | X | | | | |
|mobile-application-id| | | | | | |
|mutex| | X | | | | |
|named pipe| | X | | | | |
|nationality| | | | | | |
|other| X | X | X | X | X | X |
|passenger-name-record-locator-number| | | | | | |
|passport-country| | | | | | |
|passport-expiration| | | | | | |
|passport-number| | | | | | |
|pattern-in-file| | X | | X | | |
|pattern-in-memory| | X | | X | | |
|pattern-in-traffic| | | | X | | |
|payment-details| | | | | | |
|pdb| | X | | | | |
|pehash| | | | | | |
|pgp-private-key| | X | | | | |
|pgp-public-key| | X | | | | |
|phone-number| | | | | X | |
|place-of-birth| | | | | | |
|place-port-of-clearance| | | | | | |
|place-port-of-onward-foreign-destination| | | | | | |
|place-port-of-original-embarkation| | | | | | |
|port| | | | | | |
|primary-residence| | | | | | |
|prtn| | | | | X | |
|redress-number| | | | | | |
|regkey| | X | | X | | |
|regkey&#124;value| | X | | X | | |
|sha1| | X | | X | | |
|sha224| | X | | | | |
|sha256| | X | | X | | |
|sha3-224| | X | | X | | |
|sha3-256| | X | | X | | |
|sha3-384| | X | | X | | |
|sha3-512| | X | | X | | |
|sha384| | X | | | | |
|sha512| | X | | | | |
|sha512/224| | X | | | | |
|sha512/256| | X | | | | |
|sigma| | X | | | | |
|size-in-bytes| | | | | | |
|snort| | | | X | | |
|special-service-request| | | | | | |
|ssdeep| | X | | | | |
|stix2-pattern| | X | | | | |
|target-email| | | | | | |
|target-external| | | | | | |
|target-location| | | | | | |
|target-machine| | | | | | |
|target-org| | | | | | |
|target-user| | | | | | |
|text| X | X | X | X | X | X |
|threat-actor| | | X | | | |
|tlsh| | | | | | |
|travel-details| | | | | | |
|twitter-id| | | | | | |
|uri| | | | | | |
|url| | | | X | | |
|user-agent| | | | X | | |
|vhash| | X | | | | |
|visa-number| | | | | | |
|vulnerability| | | | X | | |
|weakness| | | | X | | |
|whois-creation-date| | | X | | | |
|whois-registrant-email| | | X | | | |
|whois-registrant-name| | | X | | | |
|whois-registrant-org| | | X | | | |
|whois-registrant-phone| | | X | | | |
|whois-registrar| | | X | | | |
|windows-scheduled-task| | X | | | | |
|windows-service-displayname| | X | | | | |
|windows-service-name| | X | | | | |
|x509-fingerprint-md5| | X | X | X | | |
|x509-fingerprint-sha1| | X | X | X | | |
|x509-fingerprint-sha256| | X | X | X | | |
|xmr| | | | | X | |
|yara| | X | | | | |
|zeek| | | | X | | |

|Category| Network activity | Other | Payload delivery | Payload installation | Payload type | Persistence mechanism |
| --- |:---:|:---:|:---:|:---:|:---:|:---:|
|AS| X | | X | | | |
|aba-rtn| | | | | | |
|anonymised| X | X | X | X | X | X |
|attachment| X | | X | X | | |
|authentihash| | | X | X | | |
|bank-account-nr| | | | | | |
|bic| | | | | | |
|bin| | | | | | |
|boolean| | X | | | | |
|bro| X | | | | | |
|btc| | | | | | |
|campaign-id| | | | | | |
|campaign-name| | | | | | |
|cc-number| | | | | | |
|cdhash| | | X | X | | |
|chrome-extension-id| | | X | X | | |
|comment| X | X | X | X | X | X |
|community-id| X | | | | | |
|cookie| X | | | | | |
|cortex| | | | | | |
|counter| | X | | | | |
|country-of-residence| | | | | | |
|cpe| | X | | | | |
|dash| | | | | | |
|date-of-birth| | | | | | |
|datetime| | X | | | | |
|dns-soa-email| | | | | | |
|domain| X | | X | | | |
|domain&#124;ip| X | | | | | |
|email| X | | X | | | |
|email-attachment| | | X | | | |
|email-body| | | X | | | |
|email-dst| X | | X | | | |
|email-dst-display-name| | | X | | | |
|email-header| | | X | | | |
|email-message-id| | | X | | | |
|email-mime-boundary| | | X | | | |
|email-reply-to| | | X | | | |
|email-src| X | | X | | | |
|email-src-display-name| | | X | | | |
|email-subject| X | | X | | | |
|email-thread-index| | | X | | | |
|email-x-mailer| | | X | | | |
|eppn| X | | | | | |
|filename| | | X | X | | X |
|filename&#124;authentihash| | | X | X | | |
|filename&#124;impfuzzy| | | X | X | | |
|filename&#124;imphash| | | X | X | | |
|filename&#124;md5| | | X | X | | |
|filename&#124;pehash| | | X | X | | |
|filename&#124;sha1| | | X | X | | |
|filename&#124;sha224| | | X | X | | |
|filename&#124;sha256| | | X | X | | |
|filename&#124;sha3-224| | | X | X | | |
|filename&#124;sha3-256| | | X | X | | |
|filename&#124;sha3-384| | | X | X | | |
|filename&#124;sha3-512| | | X | X | | |
|filename&#124;sha384| | | X | X | | |
|filename&#124;sha512| | | X | X | | |
|filename&#124;sha512/224| | | X | X | | |
|filename&#124;sha512/256| | | X | X | | |
|filename&#124;ssdeep| | | X | X | | |
|filename&#124;tlsh| | | X | X | | |
|filename&#124;vhash| | | X | X | | |
|first-name| | | | | | |
|float| | X | | | | |
|frequent-flyer-number| | | | | | |
|gender| | | | | | |
|gene| | | | | | |
|git-commit-id| | | | | | |
|github-organisation| | | | | | |
|github-repository| | | | | | |
|github-username| | | | | | |
|hassh-md5| X | | X | | | |
|hasshserver-md5| X | | X | | | |
|hex| X | X | X | X | | X |
|hostname| X | | X | | | |
|hostname&#124;port| X | | X | | | |
|http-method| X | | | | | |
|iban| | | | | | |
|identity-card-number| | | | | | |
|impfuzzy| | | X | X | | |
|imphash| | | X | X | | |
|ip-dst| X | | X | | | |
|ip-dst&#124;port| X | | X | | | |
|ip-src| X | | X | | | |
|ip-src&#124;port| X | | X | | | |
|issue-date-of-the-visa| | | | | | |
|ja3-fingerprint-md5| X | | X | | | |
|jabber-id| | | | | | |
|kusto-query| | | | | | |
|last-name| | | | | | |
|link| | | X | | | |
|mac-address| X | | X | | | |
|mac-eui-64| X | | X | | | |
|malware-sample| | | X | X | | |
|malware-type| | | X | X | | |
|md5| | | X | X | | |
|middle-name| | | | | | |
|mime-type| | | X | X | | |
|mobile-application-id| | | X | X | | |
|mutex| | | | | | |
|named pipe| | | | | | |
|nationality| | | | | | |
|other| X | X | X | X | X | X |
|passenger-name-record-locator-number| | | | | | |
|passport-country| | | | | | |
|passport-expiration| | | | | | |
|passport-number| | | | | | |
|pattern-in-file| X | | X | X | | |
|pattern-in-memory| | | | X | | |
|pattern-in-traffic| X | | X | X | | |
|payment-details| | | | | | |
|pdb| | | | | | |
|pehash| | | X | X | | |
|pgp-private-key| | X | | | | |
|pgp-public-key| | X | | | | |
|phone-number| | X | | | | |
|place-of-birth| | | | | | |
|place-port-of-clearance| | | | | | |
|place-port-of-onward-foreign-destination| | | | | | |
|place-port-of-original-embarkation| | | | | | |
|port| X | X | | | | |
|primary-residence| | | | | | |
|prtn| | | | | | |
|redress-number| | | | | | |
|regkey| | | | | | X |
|regkey&#124;value| | | | | | X |
|sha1| | | X | X | | |
|sha224| | | X | X | | |
|sha256| | | X | X | | |
|sha3-224| | | X | X | | |
|sha3-256| | | X | X | | |
|sha3-384| | | X | X | | |
|sha3-512| | | X | X | | |
|sha384| | | X | X | | |
|sha512| | | X | X | | |
|sha512/224| | | X | X | | |
|sha512/256| | | X | X | | |
|sigma| | | X | X | | |
|size-in-bytes| | X | | | | |
|snort| X | | | | | |
|special-service-request| | | | | | |
|ssdeep| | | X | X | | |
|stix2-pattern| X | | X | X | | |
|target-email| | | | | | |
|target-external| | | | | | |
|target-location| | | | | | |
|target-machine| | | | | | |
|target-org| | | | | | |
|target-user| | | | | | |
|text| X | X | X | X | X | X |
|threat-actor| | | | | | |
|tlsh| | | X | X | | |
|travel-details| | | | | | |
|twitter-id| | | | | | |
|uri| X | | | | | |
|url| X | | X | | | |
|user-agent| X | | X | | | |
|vhash| | | X | X | | |
|visa-number| | | | | | |
|vulnerability| | | X | X | | |
|weakness| | | X | X | | |
|whois-creation-date| | | | | | |
|whois-registrant-email| | | X | | | |
|whois-registrant-name| | | | | | |
|whois-registrant-org| | | | | | |
|whois-registrant-phone| | | | | | |
|whois-registrar| | | | | | |
|windows-scheduled-task| | | | | | |
|windows-service-displayname| | | | | | |
|windows-service-name| | | | | | |
|x509-fingerprint-md5| X | | X | X | | |
|x509-fingerprint-sha1| X | | X | X | | |
|x509-fingerprint-sha256| X | | X | X | | |
|xmr| | | | | | |
|yara| | | X | X | | |
|zeek| X | | | | | |

|Category| Person | Social network | Support Tool | Targeting data |
| --- |:---:|:---:|:---:|:---:|
|AS| | | | |
|aba-rtn| | | | |
|anonymised| X | X | X | X |
|attachment| | | X | |
|authentihash| | | | |
|bank-account-nr| | | | |
|bic| | | | |
|bin| | | | |
|boolean| | | | |
|bro| | | | |
|btc| | | | |
|campaign-id| | | | |
|campaign-name| | | | |
|cc-number| | | | |
|cdhash| | | | |
|chrome-extension-id| | | | |
|comment| X | X | X | X |
|community-id| | | | |
|cookie| | | | |
|cortex| | | | |
|counter| | | | |
|country-of-residence| X | | | |
|cpe| | | | |
|dash| | | | |
|date-of-birth| X | | | |
|datetime| | | | |
|dns-soa-email| | | | |
|domain| | | | |
|domain&#124;ip| | | | |
|email| X | X | | |
|email-attachment| | | | |
|email-body| | | | |
|email-dst| | X | | |
|email-dst-display-name| | | | |
|email-header| | | | |
|email-message-id| | | | |
|email-mime-boundary| | | | |
|email-reply-to| | | | |
|email-src| | X | | |
|email-src-display-name| | | | |
|email-subject| | | | |
|email-thread-index| | | | |
|email-x-mailer| | | | |
|eppn| | X | | |
|filename| | | | |
|filename&#124;authentihash| | | | |
|filename&#124;impfuzzy| | | | |
|filename&#124;imphash| | | | |
|filename&#124;md5| | | | |
|filename&#124;pehash| | | | |
|filename&#124;sha1| | | | |
|filename&#124;sha224| | | | |
|filename&#124;sha256| | | | |
|filename&#124;sha3-224| | | | |
|filename&#124;sha3-256| | | | |
|filename&#124;sha3-384| | | | |
|filename&#124;sha3-512| | | | |
|filename&#124;sha384| | | | |
|filename&#124;sha512| | | | |
|filename&#124;sha512/224| | | | |
|filename&#124;sha512/256| | | | |
|filename&#124;ssdeep| | | | |
|filename&#124;tlsh| | | | |
|filename&#124;vhash| | | | |
|first-name| X | | | |
|float| | | | |
|frequent-flyer-number| X | | | |
|gender| X | | | |
|gene| | | | |
|git-commit-id| | | | |
|github-organisation| | X | | |
|github-repository| | X | | |
|github-username| | X | | |
|hassh-md5| | | | |
|hasshserver-md5| | | | |
|hex| | | X | |
|hostname| | | | |
|hostname&#124;port| | | | |
|http-method| | | | |
|iban| | | | |
|identity-card-number| X | | | |
|impfuzzy| | | | |
|imphash| | | | |
|ip-dst| | | | |
|ip-dst&#124;port| | | | |
|ip-src| | | | |
|ip-src&#124;port| | | | |
|issue-date-of-the-visa| X | | | |
|ja3-fingerprint-md5| | | | |
|jabber-id| | X | | |
|kusto-query| | | | |
|last-name| X | | | |
|link| | | X | |
|mac-address| | | | |
|mac-eui-64| | | | |
|malware-sample| | | | |
|malware-type| | | | |
|md5| | | | |
|middle-name| X | | | |
|mime-type| | | | |
|mobile-application-id| | | | |
|mutex| | | | |
|named pipe| | | | |
|nationality| X | | | |
|other| X | X | X | |
|passenger-name-record-locator-number| X | | | |
|passport-country| X | | | |
|passport-expiration| X | | | |
|passport-number| X | | | |
|pattern-in-file| | | | |
|pattern-in-memory| | | | |
|pattern-in-traffic| | | | |
|payment-details| X | | | |
|pdb| | | | |
|pehash| | | | |
|pgp-private-key| X | X | | |
|pgp-public-key| X | X | | |
|phone-number| X | | | |
|place-of-birth| X | | | |
|place-port-of-clearance| X | | | |
|place-port-of-onward-foreign-destination| X | | | |
|place-port-of-original-embarkation| X | | | |
|port| | | | |
|primary-residence| X | | | |
|prtn| | | | |
|redress-number| X | | | |
|regkey| | | | |
|regkey&#124;value| | | | |
|sha1| | | | |
|sha224| | | | |
|sha256| | | | |
|sha3-224| | | | |
|sha3-256| | | | |
|sha3-384| | | | |
|sha3-512| | | | |
|sha384| | | | |
|sha512| | | | |
|sha512/224| | | | |
|sha512/256| | | | |
|sigma| | | | |
|size-in-bytes| | | | |
|snort| | | | |
|special-service-request| X | | | |
|ssdeep| | | | |
|stix2-pattern| | | | |
|target-email| | | | X |
|target-external| | | | X |
|target-location| | | | X |
|target-machine| | | | X |
|target-org| | | | X |
|target-user| | | | X |
|text| X | X | X | |
|threat-actor| | | | |
|tlsh| | | | |
|travel-details| X | | | |
|twitter-id| | X | | |
|uri| | | | |
|url| | | | |
|user-agent| | | | |
|vhash| | | | |
|visa-number| X | | | |
|vulnerability| | | | |
|weakness| | | | |
|whois-creation-date| | | | |
|whois-registrant-email| | X | | |
|whois-registrant-name| | | | |
|whois-registrant-org| | | | |
|whois-registrant-phone| | | | |
|whois-registrar| | | | |
|windows-scheduled-task| | | | |
|windows-service-displayname| | | | |
|windows-service-name| | | | |
|x509-fingerprint-md5| | | | |
|x509-fingerprint-sha1| | | | |
|x509-fingerprint-sha256| | | | |
|xmr| | | | |
|yara| | | | |
|zeek| | | | |


### Categories

*   **Antivirus detection**: All the info about how the malware is detected by the antivirus products
*   **Artifacts dropped**: Any artifact (files, registry keys etc.) dropped by the malware or other modifications to the system
*   **Attribution**: Identification of the group, organisation, or country behind the attack
*   **External analysis**: Any other result from additional analysis of the malware like tools output
*   **Financial fraud**: Financial Fraud indicators
*   **Internal reference**: Reference used by the publishing party (e.g. ticket number)
*   **Network activity**: Information about network traffic generated by the malware
*   **Other**: Attributes that are not part of any other category or are meant to be used as a component in MISP objects in the future
*   **Payload delivery**: Information about how the malware is delivered
*   **Payload installation**: Info on where the malware gets installed in the system
*   **Payload type**: Information about the final payload(s)
*   **Persistence mechanism**: Mechanisms used by the malware to start at boot
*   **Person**: A human being - natural person
*   **Social network**: Social networks and platforms
*   **Support Tool**: Tools supporting analysis or detection of the event
*   **Targeting data**: Internal Attack Targeting and Compromise Information

### Types

*   **AS**: Autonomous system
*   **aba-rtn**: ABA routing transit number
*   **anonymised**: Anonymised value - described with the anonymisation object via a relationship
*   **attachment**: Attachment with external information
*   **authentihash**: Authenticode executable signature hash
*   **bank-account-nr**: Bank account number without any routing number
*   **bic**: Bank Identifier Code Number also known as SWIFT-BIC, SWIFT code or ISO 9362 code
*   **bin**: Bank Identification Number
*   **boolean**: Boolean value - to be used in objects
*   **bro**: An NIDS rule in the Bro rule-format
*   **btc**: Bitcoin Address
*   **campaign-id**: Associated campaign ID
*   **campaign-name**: Associated campaign name
*   **cc-number**: Credit-Card Number
*   **cdhash**: An Apple Code Directory Hash, identifying a code-signed Mach-O executable file
*   **chrome-extension-id**: Chrome extension id
*   **comment**: Comment or description in a human language
*   **community-id**: a community ID flow hashing algorithm to map multiple traffic monitors into common flow id
*   **cookie**: HTTP cookie as often stored on the user web client. This can include authentication cookie or session cookie.
*   **cortex**: Cortex analysis result
*   **counter**: An integer counter, generally to be used in objects
*   **country-of-residence**: The country of residence of a natural person
*   **cpe**: Common platform enumeration
*   **dash**: Dash Address
*   **date-of-birth**: Date of birth of a natural person (in YYYY-MM-DD format)
*   **datetime**: Datetime in the ISO 8601 format
*   **dns-soa-email**: RFC1035 mandates that DNS zones should have a SOA (Statement Of Authority) record that contains an email address where a PoC for the domain could be contacted. This can sometimes be used for attribution/linkage between different domains even if protected by whois privacy
*   **domain**: A domain name used in the malware
*   **domain&#124;ip**: A domain name and its IP address (as found in DNS lookup) separated by a &#124;
*   **email**: An e-mail address
*   **email-attachment**: File name of the email attachment.
*   **email-body**: Email body
*   **email-dst**: The destination email address. Used to describe the recipient when describing an e-mail.
*   **email-dst-display-name**: Email destination display name
*   **email-header**: Email header
*   **email-message-id**: The email message ID
*   **email-mime-boundary**: The email mime boundary separating parts in a multipart email
*   **email-reply-to**: Email reply to header
*   **email-src**: The source email address. Used to describe the sender when describing an e-mail.
*   **email-src-display-name**: Email source display name
*   **email-subject**: The subject of the email
*   **email-thread-index**: The email thread index header
*   **email-x-mailer**: Email x-mailer header
*   **eppn**: eduPersonPrincipalName - eppn - the NetId of the person for the purposes of inter-institutional authentication. Should be stored in the form of user@univ.edu, where univ.edu is the name of the local security domain.
*   **filename**: Filename
*   **filename&#124;authentihash**: A checksum in md5 format
*   **filename&#124;impfuzzy**: Import fuzzy hash - a fuzzy hash created based on the imports in the sample.
*   **filename&#124;imphash**: Import hash - a hash created based on the imports in the sample.
*   **filename&#124;md5**: A filename and an md5 hash separated by a &#124;
*   **filename&#124;pehash**: A filename and a PEhash separated by a &#124;
*   **filename&#124;sha1**: A filename and an sha1 hash separated by a &#124;
*   **filename&#124;sha224**: A filename and a sha-224 hash separated by a &#124;
*   **filename&#124;sha256**: A filename and an sha256 hash separated by a &#124;
*   **filename&#124;sha3-224**: A filename and an sha3-224 hash separated by a &#124;
*   **filename&#124;sha3-256**: A filename and an sha3-256 hash separated by a &#124;
*   **filename&#124;sha3-384**: A filename and an sha3-384 hash separated by a &#124;
*   **filename&#124;sha3-512**: A filename and an sha3-512 hash separated by a &#124;
*   **filename&#124;sha384**: A filename and a sha-384 hash separated by a &#124;
*   **filename&#124;sha512**: A filename and a sha-512 hash separated by a &#124;
*   **filename&#124;sha512/224**: A filename and a sha-512/224 hash separated by a &#124;
*   **filename&#124;sha512/256**: A filename and a sha-512/256 hash separated by a &#124;
*   **filename&#124;ssdeep**: A checksum in ssdeep format
*   **filename&#124;tlsh**: A filename and a Trend Micro Locality Sensitive Hash separated by a &#124;
*   **filename&#124;vhash**: A filename and a VirusTotal hash separated by a &#124;
*   **first-name**: First name of a natural person
*   **float**: A floating point value.
*   **frequent-flyer-number**: The frequent flyer number of a passenger
*   **gender**: The gender of a natural person (Male, Female, Other, Prefer not to say)
*   **gene**: GENE - Go Evtx sigNature Engine
*   **git-commit-id**: A git commit ID.
*   **github-organisation**: A github organisation
*   **github-repository**: A github repository
*   **github-username**: A github user name
*   **hassh-md5**: hassh is a network fingerprinting standard which can be used to identify specific Client SSH implementations. The fingerprints can be easily stored, searched and shared in the form of an MD5 fingerprint.
*   **hasshserver-md5**: hasshServer is a network fingerprinting standard which can be used to identify specific Server SSH implementations. The fingerprints can be easily stored, searched and shared in the form of an MD5 fingerprint.
*   **hex**: A value in hexadecimal format
*   **hostname**: A full host/dnsname of an attacker
*   **hostname&#124;port**: Hostname and port number separated by a &#124;
*   **http-method**: HTTP method used by the malware (e.g. POST, GET, ...).
*   **iban**: International Bank Account Number
*   **identity-card-number**: Identity card number
*   **impfuzzy**: A fuzzy hash of import table of Portable Executable format
*   **imphash**: Import hash - a hash created based on the imports in the sample.
*   **ip-dst**: A destination IP address of the attacker or C&C server
*   **ip-dst&#124;port**: IP destination and port number separated by a &#124;
*   **ip-src**: A source IP address of the attacker
*   **ip-src&#124;port**: IP source and port number separated by a &#124;
*   **issue-date-of-the-visa**: The date on which the visa was issued
*   **ja3-fingerprint-md5**: JA3 is a method for creating SSL/TLS client fingerprints that should be easy to produce on any platform and can be easily shared for threat intelligence.
*   **jabber-id**: Jabber ID
*   **kusto-query**: Kusto query - Kusto from Microsoft Azure is a service for storing and running interactive analytics over Big Data.
*   **last-name**: Last name of a natural person
*   **link**: Link to an external information
*   **mac-address**: Mac address
*   **mac-eui-64**: Mac EUI-64 address
*   **malware-sample**: Attachment containing encrypted malware sample
*   **malware-type**: 
*   **md5**: A checksum in md5 format
*   **middle-name**: Middle name of a natural person
*   **mime-type**: A media type (also MIME type and content type) is a two-part identifier for file formats and format contents transmitted on the Internet
*   **mobile-application-id**: The application id of a mobile application
*   **mutex**: Mutex, use the format \BaseNamedObjects\<Mutex>
*   **named pipe**: Named pipe, use the format \.\pipe\<PipeName>
*   **nationality**: The nationality of a natural person
*   **other**: Other attribute
*   **passenger-name-record-locator-number**: The Passenger Name Record Locator is a key under which the reservation for a trip is stored in the system. The PNR contains, among other data, the name, flight segments and address of the passenger. It is defined by a combination of five or six letters and numbers.
*   **passport-country**: The country in which the passport was issued
*   **passport-expiration**: The expiration date of a passport
*   **passport-number**: The passport number of a natural person
*   **pattern-in-file**: Pattern in file that identifies the malware
*   **pattern-in-memory**: Pattern in memory dump that identifies the malware
*   **pattern-in-traffic**: Pattern in network traffic that identifies the malware
*   **payment-details**: Payment details
*   **pdb**: Microsoft Program database (PDB) path information
*   **pehash**: PEhash - a hash calculated based of certain pieces of a PE executable file
*   **pgp-private-key**: A PGP private key
*   **pgp-public-key**: A PGP public key
*   **phone-number**: Telephone Number
*   **place-of-birth**: Place of birth of a natural person
*   **place-port-of-clearance**: The port of clearance
*   **place-port-of-onward-foreign-destination**: A Port where the passenger is transiting to
*   **place-port-of-original-embarkation**: The orignal port of embarkation
*   **port**: Port number
*   **primary-residence**: The primary residence of a natural person
*   **prtn**: Premium-Rate Telephone Number
*   **redress-number**: The Redress Control Number is the record identifier for people who apply for redress through the DHS Travel Redress Inquiry Program (DHS TRIP). DHS TRIP is for travelers who have been repeatedly identified for additional screening and who want to file an inquiry to have erroneous information corrected in DHS systems
*   **regkey**: Registry key or value
*   **regkey&#124;value**: Registry value + data separated by &#124;
*   **sha1**: A checksum in sha1 format
*   **sha224**: A checksum in sha-224 format
*   **sha256**: A checksum in sha256 format
*   **sha3-224**: A checksum in sha3-224 format
*   **sha3-256**: A checksum in sha3-256 format
*   **sha3-384**: A checksum in sha3-384 format
*   **sha3-512**: A checksum in sha3-512 format
*   **sha384**: A checksum in sha-384 format
*   **sha512**: A checksum in sha-512 format
*   **sha512/224**: A checksum in the sha-512/224 format
*   **sha512/256**: A checksum in the sha-512/256 format
*   **sigma**: Sigma - Generic Signature Format for SIEM Systems
*   **size-in-bytes**: Size expressed in bytes
*   **snort**: An IDS rule in Snort rule-format
*   **special-service-request**: A Special Service Request is a function to an airline to provide a particular facility for A Passenger or passengers. 
*   **ssdeep**: A checksum in ssdeep format
*   **stix2-pattern**: STIX 2 pattern
*   **target-email**: Attack Targets Email(s)
*   **target-external**: External Target Organizations Affected by this Attack
*   **target-location**: Attack Targets Physical Location(s)
*   **target-machine**: Attack Targets Machine Name(s)
*   **target-org**: Attack Targets Department or Organization(s)
*   **target-user**: Attack Targets Username(s)
*   **text**: Name, ID or a reference
*   **threat-actor**: A string identifying the threat actor
*   **tlsh**: A checksum in the Trend Micro Locality Sensitive Hash format
*   **travel-details**: Travel details
*   **twitter-id**: Twitter ID
*   **uri**: Uniform Resource Identifier
*   **url**: url
*   **user-agent**: The user-agent used by the malware in the HTTP request.
*   **vhash**: A VirusTotal checksum
*   **visa-number**: Visa number
*   **vulnerability**: A reference to the vulnerability used in the exploit
*   **weakness**: A reference to the weakness used in the exploit
*   **whois-creation-date**: The date of domain's creation, obtained from the WHOIS information.
*   **whois-registrant-email**: The e-mail of a domain's registrant, obtained from the WHOIS information.
*   **whois-registrant-name**: The name of a domain's registrant, obtained from the WHOIS information.
*   **whois-registrant-org**: The org of a domain's registrant, obtained from the WHOIS information.
*   **whois-registrant-phone**: The phone number of a domain's registrant, obtained from the WHOIS information.
*   **whois-registrar**: The registrar of the domain, obtained from the WHOIS information.
*   **windows-scheduled-task**: A scheduled task in windows
*   **windows-service-displayname**: A windows service's displayname, not to be confused with the windows-service-name. This is the name that applications will generally display as the service's name in applications.
*   **windows-service-name**: A windows service name. This is the name used internally by windows. Not to be confused with the windows-service-displayname.
*   **x509-fingerprint-md5**: X509 fingerprint in MD5 format
*   **x509-fingerprint-sha1**: X509 fingerprint in SHA-1 format
*   **x509-fingerprint-sha256**: X509 fingerprint in SHA-256 format
*   **xmr**: Monero Address
*   **yara**: Yara signature
*   **zeek**: An NIDS rule in the Zeek rule-format

## MISP objects

MISP objects are in addition to MISP attributes to allow advanced combinations of attributes. The creation of these objects
and their associated attributes are based on real cyber security use-cases and existing practices in information sharing.
MISP objects are standardised under a simple templating format and are automatically available in MISP. A series of relationships
are also defined along with the objects which can be used to create relationships between objects.

The objects available can be [browsed via the web site](/objects.html) or downloaded as [PDF](/objects.pdf) or directly via the MISP software.

## MISP Taxonomies

Along with the core format, [MISP taxonomies](https://www.github.com/MISP/misp-taxonomies/) provide a set of already defined classifications modeling estimative language, CSIRTs/CERTs classifications, national classifications or threat model classification. The fixed taxonomies provide a practical method to tag efficiently events and attributes within a set of MISP instances where taxonomies can be easily cherry-picked or extended to meet the local requirements of an organization or a specific sharing community. When using MISP, the MISP taxonomies are available and can be freely used based on the community practises.

The taxonomies can be [browsed via the web site](/taxonomies.html) or downloaded as [PDF](/taxonomies.pdf) or via the MISP software.

[CERT-XLM](https://github.com/MISP/misp-taxonomies/tree/master/CERT-XLM):
: CERT-XLM Security Incident Classification.[HTML](https://www.misp-project.org/taxonomies.html#_CERT_XLM)

[DML](https://github.com/MISP/misp-taxonomies/tree/master/DML):
: The Detection Maturity Level (DML) model is a capability maturity model for referencing ones maturity in detecting cyber attacks.  It's designed for organizations who perform intel-driven detection and response and who put an emphasis on having a mature detection program.[HTML](https://www.misp-project.org/taxonomies.html#_DML)

[PAP](https://github.com/MISP/misp-taxonomies/tree/master/PAP):
: The Permissible Actions Protocol - or short: PAP - was designed to indicate how the received information can be used.[HTML](https://www.misp-project.org/taxonomies.html#_PAP)

[access-method](https://github.com/MISP/misp-taxonomies/tree/master/access-method):
: The access method used to remotely access a system.[HTML](https://www.misp-project.org/taxonomies.html#_access_method)

[accessnow](https://github.com/MISP/misp-taxonomies/tree/master/accessnow):
: Access Now classification to classify an issue (such as security, human rights, youth rights).[HTML](https://www.misp-project.org/taxonomies.html#_accessnow)

[action-taken](https://github.com/MISP/misp-taxonomies/tree/master/action-taken):
: Action taken in the case of a security incident (CSIRT perspective).[HTML](https://www.misp-project.org/taxonomies.html#_action_taken)

[admiralty-scale](https://github.com/MISP/misp-taxonomies/tree/master/admiralty-scale):
: The Admiralty Scale (also called the NATO System) is used to rank the reliability of a source and the credibility of an information.[HTML](https://www.misp-project.org/taxonomies.html#_admiralty_scale)

[adversary](https://github.com/MISP/misp-taxonomies/tree/master/adversary):
: An overview and description of the adversary infrastructure.[HTML](https://www.misp-project.org/taxonomies.html#_adversary)

[ais-marking](https://github.com/MISP/misp-taxonomies/tree/master/ais-marking):
: AIS Marking Schema implementation is maintained by the National Cybersecurity and Communication Integration Center (NCCIC) of the U.S. Department of Homeland Security (DHS)[HTML](https://www.misp-project.org/taxonomies.html#_ais_marking)

[analyst-assessment](https://github.com/MISP/misp-taxonomies/tree/master/analyst-assessment):
: A series of assessment predicates describing the analyst capabilities to perform analysis. These assessment can be assigned by the analyst him/herself or by another party evaluating the analyst.[HTML](https://www.misp-project.org/taxonomies.html#_analyst_assessment)

[approved-category-of-action](https://github.com/MISP/misp-taxonomies/tree/master/approved-category-of-action):
: A pre-approved category of action for indicators being shared with partners (MIMIC).[HTML](https://www.misp-project.org/taxonomies.html#_approved_category_of_action)

[binary-class](https://github.com/MISP/misp-taxonomies/tree/master/binary-class):
: Custom taxonomy for types of binary file.[HTML](https://www.misp-project.org/taxonomies.html#_binary_class)

[cccs](https://github.com/MISP/misp-taxonomies/tree/master/cccs):
: Internal taxonomy for CCCS.[HTML](https://www.misp-project.org/taxonomies.html#_cccs)

[circl](https://github.com/MISP/misp-taxonomies/tree/master/circl):
: CIRCL Taxonomy is a simple scheme for incident classification and area topic where the incident took place.[HTML](https://www.misp-project.org/taxonomies.html#_circl)

[collaborative-intelligence](https://github.com/MISP/misp-taxonomies/tree/master/collaborative-intelligence):
: Collaborative intelligence support language is a common language to support analysts to perform their analysis to get crowdsourced support when using threat intelligence sharing platform like MISP.[HTML](https://www.misp-project.org/taxonomies.html#_collaborative_intelligence)

[common-taxonomy](https://github.com/MISP/misp-taxonomies/tree/master/common-taxonomy):
: The Common Taxonomy for Law Enforcement and The National Network of CSIRTs bridges the gap between the CSIRTs and international Law Enforcement communities by adding a legislative framework to facilitate the harmonisation of incident reporting to competent authorities, the development of useful statistics and sharing information within the entire cybercrime ecosystem.[HTML](https://www.misp-project.org/taxonomies.html#_common_taxonomy)

[copine-scale](https://github.com/MISP/misp-taxonomies/tree/master/copine-scale):
: The COPINE Scale is a rating system created in Ireland and used in the United Kingdom to categorise the severity of images of child sex abuse.[HTML](https://www.misp-project.org/taxonomies.html#_copine_scale)

[cryptocurrency-threat](https://github.com/MISP/misp-taxonomies/tree/master/cryptocurrency-threat):
: Threats targetting cryptocurrency, based on CipherTrace report.[HTML](https://www.misp-project.org/taxonomies.html#_cryptocurrency_threat)

[csirt-americas](https://github.com/MISP/misp-taxonomies/tree/master/csirt-americas):
: Taxonomy from CSIRTAmericas.org.[HTML](https://www.misp-project.org/taxonomies.html#_csirt_americas)

[csirt_case_classification](https://github.com/MISP/misp-taxonomies/tree/master/csirt_case_classification):
: FIRST CSIRT Case Classification.[HTML](https://www.misp-project.org/taxonomies.html#_csirt_case_classification)

[cssa](https://github.com/MISP/misp-taxonomies/tree/master/cssa):
: The CSSA agreed sharing taxonomy.[HTML](https://www.misp-project.org/taxonomies.html#_cssa)

[cyber-threat-framework](https://github.com/MISP/misp-taxonomies/tree/master/cyber-threat-framework):
: Cyber Threat Framework was developed by the US Government to enable consistent characterization and categorization of cyber threat events, and to identify trends or changes in the activities of cyber adversaries. https://www.dni.gov/index.php/cyber-threat-framework[HTML](https://www.misp-project.org/taxonomies.html#_cyber_threat_framework)

[dark-web](https://github.com/MISP/misp-taxonomies/tree/master/dark-web):
: Criminal motivation on the dark web: A categorisation model for law enforcement. ref: Janis Dalins, Campbell Wilson, Mark Carman. Taxonomy updated by MISP Project.[HTML](https://www.misp-project.org/taxonomies.html#_dark_web)

[data-classification](https://github.com/MISP/misp-taxonomies/tree/master/data-classification):
: Data classification for data potentially at risk of exfiltration based on table 2.1 of Solving Cyber Risk book.[HTML](https://www.misp-project.org/taxonomies.html#_data_classification)

[dcso-sharing](https://github.com/MISP/misp-taxonomies/tree/master/dcso-sharing):
: DCSO Sharing Taxonomy to classify certain types of MISP events using the DCSO Event Guide[HTML](https://www.misp-project.org/taxonomies.html#_dcso_sharing)

[ddos](https://github.com/MISP/misp-taxonomies/tree/master/ddos):
: Distributed Denial of Service - or short: DDoS - taxonomy supports the description of Denial of Service attacks and especially the types they belong too.[HTML](https://www.misp-project.org/taxonomies.html#_ddos)

[de-vs](https://github.com/MISP/misp-taxonomies/tree/master/de-vs):
: Taxonomy for the handling of protectively marked information in MISP with German (DE) Government classification markings (VS)[HTML](https://www.misp-project.org/taxonomies.html#_de_vs)

[dhs-ciip-sectors](https://github.com/MISP/misp-taxonomies/tree/master/dhs-ciip-sectors):
: DHS critical sectors as described in https://www.dhs.gov/critical-infrastructure-sectors.[HTML](https://www.misp-project.org/taxonomies.html#_dhs_ciip_sectors)

[diamond-model](https://github.com/MISP/misp-taxonomies/tree/master/diamond-model):
: The Diamond Model for Intrusion Analysis, a phase-based model developed by Lockheed Martin, aims to help categorise and identify the stage of an attack.[HTML](https://www.misp-project.org/taxonomies.html#_diamond_model)

[dni-ism](https://github.com/MISP/misp-taxonomies/tree/master/dni-ism):
: ISM (Information Security Marking Metadata) V13 as described by DNI.gov (Director of National Intelligence - US).[HTML](https://www.misp-project.org/taxonomies.html#_dni_ism)

[domain-abuse](https://github.com/MISP/misp-taxonomies/tree/master/domain-abuse):
: Taxonomy to tag domain names used for cybercrime.[HTML](https://www.misp-project.org/taxonomies.html#_domain_abuse)

[drugs](https://github.com/MISP/misp-taxonomies/tree/master/drugs):
: A taxonomy based on the superclass and class of drugs, based on https://www.drugbank.ca/releases/latest[HTML](https://www.misp-project.org/taxonomies.html#_drugs)

[economical-impact](https://github.com/MISP/misp-taxonomies/tree/master/economical-impact):
: Economical impact is a taxonomy to describe the financial impact as positive or negative gain to the tagged information.[HTML](https://www.misp-project.org/taxonomies.html#_economical_impact)

[ecsirt](https://github.com/MISP/misp-taxonomies/tree/master/ecsirt):
: eCSIRT incident classification Appendix C of the eCSIRT EU project including IntelMQ updates.[HTML](https://www.misp-project.org/taxonomies.html#_ecsirt)

[enisa](https://github.com/MISP/misp-taxonomies/tree/master/enisa):
: ENISA Threat Taxonomy - A tool for structuring threat information as published in https://www.enisa.europa.eu/topics/threat-risk-management/threats-and-trends/enisa-threat-landscape/etl2015/enisa-threat-taxonomy-a-tool-for-structuring-threat-information[HTML](https://www.misp-project.org/taxonomies.html#_enisa)

[estimative-language](https://github.com/MISP/misp-taxonomies/tree/master/estimative-language):
: Estimative language - including likelihood or probability of event based on the Intelligence Community Directive 203 (ICD 203) (6.2.(a)) and JP 2-0, Joint Intelligence.[HTML](https://www.misp-project.org/taxonomies.html#_estimative_language)

[eu-marketop-and-publicadmin](https://github.com/MISP/misp-taxonomies/tree/master/eu-marketop-and-publicadmin):
: Market operators and public administrations that must comply to some notifications requirements under EU NIS directive.[HTML](https://www.misp-project.org/taxonomies.html#_eu_marketop_and_publicadmin)

[eu-nis-sector-and-subsectors](https://github.com/MISP/misp-taxonomies/tree/master/eu-nis-sector-and-subsectors):
: Sectors and sub sectors as identified by the NIS Directive.[HTML](https://www.misp-project.org/taxonomies.html#_eu_nis_sector_and_subsectors)

[euci](https://github.com/MISP/misp-taxonomies/tree/master/euci):
: EU classified information (EUCI) means any information or material designated by a EU security classification, the unauthorised disclosure of which could cause varying degrees of prejudice to the interests of the European Union or of one or more of the Member States as described in COUNCIL DECISION of 23 September 2013 on the security rules for protecting EU classified information[HTML](https://www.misp-project.org/taxonomies.html#_euci)

[europol-event](https://github.com/MISP/misp-taxonomies/tree/master/europol-event):
: EUROPOL type of events taxonomy.[HTML](https://www.misp-project.org/taxonomies.html#_europol_event)

[europol-incident](https://github.com/MISP/misp-taxonomies/tree/master/europol-incident):
: EUROPOL class of incident taxonomy.[HTML](https://www.misp-project.org/taxonomies.html#_europol_incident)

[event-assessment](https://github.com/MISP/misp-taxonomies/tree/master/event-assessment):
: A series of assessment predicates describing the event assessment performed to make judgement(s) under a certain level of uncertainty.[HTML](https://www.misp-project.org/taxonomies.html#_event_assessment)

[event-classification](https://github.com/MISP/misp-taxonomies/tree/master/event-classification):
: Event Classification.[HTML](https://www.misp-project.org/taxonomies.html#_event_classification)

[exercise](https://github.com/MISP/misp-taxonomies/tree/master/exercise):
: Exercise is a taxonomy to describe if the information is part of one or more cyber or crisis exercise.[HTML](https://www.misp-project.org/taxonomies.html#_exercise)

[false-positive](https://github.com/MISP/misp-taxonomies/tree/master/false-positive):
: This taxonomy aims to ballpark the expected amount of false positives.[HTML](https://www.misp-project.org/taxonomies.html#_false_positive)

[file-type](https://github.com/MISP/misp-taxonomies/tree/master/file-type):
: List of known file types.[HTML](https://www.misp-project.org/taxonomies.html#_file_type)

[flesch-reading-ease](https://github.com/MISP/misp-taxonomies/tree/master/flesch-reading-ease):
: Flesch Reading Ease is a revised system for determining the comprehension difficulty of written material. The scoring of the flesh score can have a maximum of 121.22 and there is no limit on how low a score can be (negative score are valid).[HTML](https://www.misp-project.org/taxonomies.html#_flesch_reading_ease)

[fpf](https://github.com/MISP/misp-taxonomies/tree/master/fpf):
: The Future of Privacy Forum (FPF) [visual guide to practical de-identification](https://fpf.org/2016/04/25/a-visual-guide-to-practical-data-de-identification/) taxonomy is used to evaluate the degree of identifiability of personal data and the types of pseudonymous data, de-identified data and anonymous data. The work of FPF is licensed under a creative commons attribution 4.0 international license.[HTML](https://www.misp-project.org/taxonomies.html#_fpf)

[fr-classif](https://github.com/MISP/misp-taxonomies/tree/master/fr-classif):
: French gov information classification system.[HTML](https://www.misp-project.org/taxonomies.html#_fr_classif)

[gdpr](https://github.com/MISP/misp-taxonomies/tree/master/gdpr):
: Taxonomy related to the REGULATION (EU) 2016/679 OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL on the protection of natural persons with regard to the processing of personal data and on the free movement of such data, and repealing Directive 95/46/EC (General Data Protection Regulation)[HTML](https://www.misp-project.org/taxonomies.html#_gdpr)

[gsma-attack-category](https://github.com/MISP/misp-taxonomies/tree/master/gsma-attack-category):
: Taxonomy used by GSMA for their information sharing program with telco describing the attack categories[HTML](https://www.misp-project.org/taxonomies.html#_gsma_attack_category)

[gsma-fraud](https://github.com/MISP/misp-taxonomies/tree/master/gsma-fraud):
: Taxonomy used by GSMA for their information sharing program with telco describing the various aspects of fraud[HTML](https://www.misp-project.org/taxonomies.html#_gsma_fraud)

[gsma-network-technology](https://github.com/MISP/misp-taxonomies/tree/master/gsma-network-technology):
: Taxonomy used by GSMA for their information sharing program with telco describing the types of infrastructure. WiP[HTML](https://www.misp-project.org/taxonomies.html#_gsma_network_technology)

[honeypot-basic](https://github.com/MISP/misp-taxonomies/tree/master/honeypot-basic):
: Christian Seifert, Ian Welch, Peter Komisarczuk, ‘Taxonomy of Honeypots’, Technical Report CS-TR-06/12, VICTORIA UNIVERSITY OF WELLINGTON, School of Mathematical and Computing Sciences, June 2006, http://www.mcs.vuw.ac.nz/comp/Publications/archive/CS-TR-06/CS-TR-06-12.pdf[HTML](https://www.misp-project.org/taxonomies.html#_honeypot_basic)

[iep](https://github.com/MISP/misp-taxonomies/tree/master/iep):
: Forum of Incident Response and Security Teams (FIRST) Information Exchange Policy (IEP) framework.[HTML](https://www.misp-project.org/taxonomies.html#_iep)

[ifx-vetting](https://github.com/MISP/misp-taxonomies/tree/master/ifx-vetting):
: The IFX taxonomy is used to categorise information (MISP events and attributes) to aid in the intelligence vetting process[HTML](https://www.misp-project.org/taxonomies.html#_ifx_vetting)

[incident-disposition](https://github.com/MISP/misp-taxonomies/tree/master/incident-disposition):
: How an incident is classified in its process to be resolved. The taxonomy is inspired from NASA Incident Response and Management Handbook.[HTML](https://www.misp-project.org/taxonomies.html#_incident_disposition)

[infoleak](https://github.com/MISP/misp-taxonomies/tree/master/infoleak):
: A taxonomy describing information leaks and especially information classified as being potentially leaked.[HTML](https://www.misp-project.org/taxonomies.html#_infoleak)

[information-security-data-source](https://github.com/MISP/misp-taxonomies/tree/master/information-security-data-source):
: Taxonomy to classify the information security data sources[HTML](https://www.misp-project.org/taxonomies.html#_information_security_data_source)

[information-security-indicators](https://github.com/MISP/misp-taxonomies/tree/master/information-security-indicators):
: Information security indicators have been standardized by the ETSI Industrial Specification Group (ISG) ISI. These indicators provide the basis to switch from a qualitative to a quantitative culture in IT Security Scope of measurements: External and internal threats (attempt and success), user's deviant behaviours, nonconformities and/or vulnerabilities (software, configuration, behavioural, general security framework). ETSI GS ISI 001-1 (V1.1.2): ISI Indicators[HTML](https://www.misp-project.org/taxonomies.html#_information_security_indicators)

[interception-method](https://github.com/MISP/misp-taxonomies/tree/master/interception-method):
: The interception method used to intercept traffic.[HTML](https://www.misp-project.org/taxonomies.html#_interception_method)

[kill-chain](https://github.com/MISP/misp-taxonomies/tree/master/kill-chain):
: Cyber Kill Chain from Lockheed Martin as described in Intelligence-Driven Computer Network Defense Informed by Analysis of Adversary Campaigns and Intrusion Kill Chains.[HTML](https://www.misp-project.org/taxonomies.html#_kill_chain)

[maec-delivery-vectors](https://github.com/MISP/misp-taxonomies/tree/master/maec-delivery-vectors):
: Vectors used to deliver malware based on MAEC 5.0[HTML](https://www.misp-project.org/taxonomies.html#_maec_delivery_vectors)

[maec-malware-behavior](https://github.com/MISP/misp-taxonomies/tree/master/maec-malware-behavior):
: Malware behaviours based on MAEC 5.0[HTML](https://www.misp-project.org/taxonomies.html#_maec_malware_behavior)

[maec-malware-capabilities](https://github.com/MISP/misp-taxonomies/tree/master/maec-malware-capabilities):
: Malware Capabilities based on MAEC 5.0[HTML](https://www.misp-project.org/taxonomies.html#_maec_malware_capabilities)

[maec-malware-obfuscation-methods](https://github.com/MISP/misp-taxonomies/tree/master/maec-malware-obfuscation-methods):
: Obfuscation methods used by malware based on MAEC 5.0[HTML](https://www.misp-project.org/taxonomies.html#_maec_malware_obfuscation_methods)

[malware_classification](https://github.com/MISP/misp-taxonomies/tree/master/malware_classification):
: Malware classification based on a SANS whitepaper about malware.[HTML](https://www.misp-project.org/taxonomies.html#_malware_classification)

[misp](https://github.com/MISP/misp-taxonomies/tree/master/misp):
: Internal MISP taxonomy.[HTML](https://www.misp-project.org/taxonomies.html#_misp)

[monarc-threat](https://github.com/MISP/misp-taxonomies/tree/master/monarc-threat):
: MONARC threat taxonomy.[HTML](https://www.misp-project.org/taxonomies.html#_monarc_threat)

[ms-caro-malware](https://github.com/MISP/misp-taxonomies/tree/master/ms-caro-malware):
: Malware Type and Platform classification based on Microsoft's implementation of the Computer Antivirus Research Organization (CARO) Naming Scheme and Malware Terminology.[HTML](https://www.misp-project.org/taxonomies.html#_ms_caro_malware)

[ms-caro-malware-full](https://github.com/MISP/misp-taxonomies/tree/master/ms-caro-malware-full):
: Malware Type and Platform classification based on Microsoft's implementation of the Computer Antivirus Research Organization (CARO) Naming Scheme and Malware Terminology.[HTML](https://www.misp-project.org/taxonomies.html#_ms_caro_malware_full)

[nato](https://github.com/MISP/misp-taxonomies/tree/master/nato):
: Marking of Classified and Unclassified materials as described by the North Atlantic Treaty Organization, NATO.[HTML](https://www.misp-project.org/taxonomies.html#_nato)

[nis](https://github.com/MISP/misp-taxonomies/tree/master/nis):
: NIS Cybersecurity Incident Taxonomy.[HTML](https://www.misp-project.org/taxonomies.html#_nis)

[open_threat](https://github.com/MISP/misp-taxonomies/tree/master/open_threat):
: Open Threat Taxonomy v1.1 base on James Tarala of SANS ref. - http://www.auditscripts.com/resources/open_threat_taxonomy_v1.1a.pdf[HTML](https://www.misp-project.org/taxonomies.html#_open_threat)

[osint](https://github.com/MISP/misp-taxonomies/tree/master/osint):
: Open Source Intelligence - Classification (MISP taxonomies).[HTML](https://www.misp-project.org/taxonomies.html#_osint)

[passivetotal](https://github.com/MISP/misp-taxonomies/tree/master/passivetotal):
: Tags for RiskIQ's passivetotal service[HTML](https://www.misp-project.org/taxonomies.html#_passivetotal)

[pentest](https://github.com/MISP/misp-taxonomies/tree/master/pentest):
: Penetration test (pentest) classification.[HTML](https://www.misp-project.org/taxonomies.html#_pentest)

[priority-level](https://github.com/MISP/misp-taxonomies/tree/master/priority-level):
: After an incident is scored, it is assigned a priority level. The six levels listed below are aligned with NCCIC, DHS, and the CISS to help provide a common lexicon when discussing incidents. This priority assignment drives NCCIC urgency, pre-approved incident response offerings, reporting requirements, and recommendations for leadership escalation. Generally, incident priority distribution should follow a similar pattern to the graph below. Based on https://www.us-cert.gov/NCCIC-Cyber-Incident-Scoring-System.[HTML](https://www.misp-project.org/taxonomies.html#_priority_level)

[ransomware](https://github.com/MISP/misp-taxonomies/tree/master/ransomware):
: Ransomware is used to define ransomware types and the elements that compose them.[HTML](https://www.misp-project.org/taxonomies.html#_ransomware)

[retention](https://github.com/MISP/misp-taxonomies/tree/master/retention):
: Retention taxonomy to describe the retention period of the tagged information.[HTML](https://www.misp-project.org/taxonomies.html#_retention)

[rsit](https://github.com/MISP/misp-taxonomies/tree/master/rsit):
: Reference Security Incident Classification Taxonomy.[HTML](https://www.misp-project.org/taxonomies.html#_rsit)

[rt_event_status](https://github.com/MISP/misp-taxonomies/tree/master/rt_event_status):
: Status of events used in Request Tracker.[HTML](https://www.misp-project.org/taxonomies.html#_rt_event_status)

[runtime-packer](https://github.com/MISP/misp-taxonomies/tree/master/runtime-packer):
: Runtime or software packer used to combine compressed data with the decompression code. The decompression code can add additional obfuscations mechanisms including polymorphic-packer or other obfuscation techniques. This taxonomy lists all the known or official packer used for legitimate use or for packing malicious binaries.[HTML](https://www.misp-project.org/taxonomies.html#_runtime_packer)

[smart-airports-threats](https://github.com/MISP/misp-taxonomies/tree/master/smart-airports-threats):
: Threat taxonomy in the scope of securing smart airports by ENISA.[HTML](https://www.misp-project.org/taxonomies.html#_smart_airports_threats)

[stealth_malware](https://github.com/MISP/misp-taxonomies/tree/master/stealth_malware):
: Classification based on malware stealth techniques.[HTML](https://www.misp-project.org/taxonomies.html#_stealth_malware)

[stix-ttp](https://github.com/MISP/misp-taxonomies/tree/master/stix-ttp):
: Representation of the behavior or modus operandi of cyber adversaries (a.k.a TTP) as normalized in STIX[HTML](https://www.misp-project.org/taxonomies.html#_stix_ttp)

[targeted-threat-index](https://github.com/MISP/misp-taxonomies/tree/master/targeted-threat-index):
: The Targeted Threat Index is a metric for assigning an overall threat ranking score to email messages that deliver malware to a victim’s computer. The TTI metric was first introduced at SecTor 2013 by Seth Hardy as part of the talk “RATastrophe: Monitoring a Malware Menagerie” along with Katie Kleemola and Greg Wiseman.[HTML](https://www.misp-project.org/taxonomies.html#_targeted_threat_index)

[threats-to-dns](https://github.com/MISP/misp-taxonomies/tree/master/threats-to-dns):
: An overview of some of the known attacks related to DNS as described by Torabi, S., Boukhtouta, A., Assi, C., & Debbabi, M. (2018) in Detecting Internet Abuse by Analyzing Passive DNS Traffic: A Survey of Implemented Systems. IEEE Communications Surveys & Tutorials, 1–1. doi:10.1109/comst.2018.2849614[HTML](https://www.misp-project.org/taxonomies.html#_threats_to_dns)

[tlp](https://github.com/MISP/misp-taxonomies/tree/master/tlp):
: The Traffic Light Protocol - or short: TLP - was designed with the objective to create a favorable classification scheme for sharing sensitive information while keeping the control over its distribution at the same time. Extended with TLP:EX:CHR.[HTML](https://www.misp-project.org/taxonomies.html#_tlp)

[tor](https://github.com/MISP/misp-taxonomies/tree/master/tor):
: Taxonomy to describe Tor network infrastructure[HTML](https://www.misp-project.org/taxonomies.html#_tor)

[type](https://github.com/MISP/misp-taxonomies/tree/master/type):
: Taxonomy to describe different types of intelligence gathering discipline which can be described the origin of intelligence.[HTML](https://www.misp-project.org/taxonomies.html#_type)

[use-case-applicability](https://github.com/MISP/misp-taxonomies/tree/master/use-case-applicability):
: The Use Case Applicability categories reflect standard resolution categories, to clearly display alerting rule configuration problems.[HTML](https://www.misp-project.org/taxonomies.html#_use_case_applicability)

[veris](https://github.com/MISP/misp-taxonomies/tree/master/veris):
: Vocabulary for Event Recording and Incident Sharing (VERIS).[HTML](https://www.misp-project.org/taxonomies.html#_veris)

[vocabulaire-des-probabilites-estimatives](https://github.com/MISP/misp-taxonomies/tree/master/vocabulaire-des-probabilites-estimatives):
: Vocabulaire des probabilités estimatives[HTML](https://www.misp-project.org/taxonomies.html#_vocabulaire_des_probabilites_estimatives)

[workflow](https://github.com/MISP/misp-taxonomies/tree/master/workflow):
: Workflow support language is a common language to support intelligence analysts to perform their analysis on data and information.[HTML](https://www.misp-project.org/taxonomies.html#_workflow)



## MISP Galaxy

MISP galaxy is a simple method to express a large object called cluster that can be attached to MISP events or attributes. A cluster can be composed of one or more elements. Elements are expressed as key-values. There are default vocabularies available in MISP galaxy but those can be overwritten, replaced or updated as you wish. Existing clusters and vocabularies can be used as-is or as a template. MISP distribution can be applied to each cluster to permit a limited or broader distribution scheme. Many MISP galaxy clusters are already available like Exploit-Kit, Microsoft Activity Group actor, Preventive Measure, 
Ransomware, TDS, Threat actor or Tool used by adversaries.

The galaxy can be [browsed via the web site](/galaxy.html) or downloaded as [PDF](/galaxy.pdf) or directly via the MISP software.
