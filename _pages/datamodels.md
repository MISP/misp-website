---
layout: page
title: MISP data models - MISP core format - MISP taxonomies
permalink: /datamodels/
toc: true
---

MISP is not only a software but also a series of data models created by the MISP community. MISP includes a simple and practical information sharing format expressed in JSON that can be used with MISP software or by any other software.

## MISP Core Format

The MISP core format is a simple JSON format used by MISP and other tools to exchange events and attributes. The JSON schema 2.4 is described on the MISP core software and many sample files are available in the OSINT feed.

The MISP format is described as Internet-Draft in [misp-rfc](https://github.com/MISP/MISP-rfc). The MISP format are described to support the developer or organisation willing to build your own tool supporting the MISP format (as import or export). The standard is built from practical use-cases and the implementation references within the MISP project. The standard is quickly evolving following the MISP implementation.

### MISP default attributes and categories

### Attribute Categories vs. Types

|Category| Antivirus detection | Artifacts dropped | Attribution | External analysis | Financial fraud | Internal reference |
| --- |:---:|:---:|:---:|:---:|:---:|:---:|
|AS| | | | X | | |
|aba-rtn| | | | | X | |
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
|comment| X | X | X | X | X | X |
|cookie| | X | | | | |
|cortex| | | | X | | |
|counter| | | | | | |
|country-of-residence| | | | | | |
|cpe| | | | | | |
|date-of-birth| | | | | | |
|datetime| | | | | | |
|dns-soa-email| | | X | | | |
|domain| | | | X | | |
|domain&#124;ip| | | | X | | |
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
|filename| | X | | X | | |
|filename&#124;authentihash| | X | | | | |
|filename&#124;impfuzzy| | X | | | | |
|filename&#124;imphash| | X | | | | |
|filename&#124;md5| | X | | X | | |
|filename&#124;pehash| | X | | | | |
|filename&#124;sha1| | X | | X | | |
|filename&#124;sha224| | X | | | | |
|filename&#124;sha256| | X | | X | | |
|filename&#124;sha384| | X | | | | |
|filename&#124;sha512| | X | | | | |
|filename&#124;sha512/224| | X | | | | |
|filename&#124;sha512/256| | X | | | | |
|filename&#124;ssdeep| | X | | | | |
|filename&#124;tlsh| | X | | | | |
|first-name| | | | | | |
|float| | | | | | |
|frequent-flyer-number| | | | | | |
|gender| | | | | | |
|gene| | X | | | | |
|github-organisation| | | | | | |
|github-repository| | | | X | | |
|github-username| | | | | | |
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
|visa-number| | | | | | |
|vulnerability| | | | X | | |
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

|Category| Network activity | Other | Payload delivery | Payload installation | Payload type | Persistence mechanism |
| --- |:---:|:---:|:---:|:---:|:---:|:---:|
|AS| X | | X | | | |
|aba-rtn| | | | | | |
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
|comment| X | X | X | X | X | X |
|cookie| X | | | | | |
|cortex| | | | | | |
|counter| | X | | | | |
|country-of-residence| | | | | | |
|cpe| | X | | | | |
|date-of-birth| | | | | | |
|datetime| | X | | | | |
|dns-soa-email| | | | | | |
|domain| X | | X | | | |
|domain&#124;ip| X | | | | | |
|email-attachment| | | X | | | |
|email-body| | | X | | | |
|email-dst| X | | X | | | |
|email-dst-display-name| | | X | | | |
|email-header| | | X | | | |
|email-message-id| | | X | | | |
|email-mime-boundary| | | X | | | |
|email-reply-to| | | X | | | |
|email-src| | | X | | | |
|email-src-display-name| | | X | | | |
|email-subject| | | X | | | |
|email-thread-index| | | X | | | |
|email-x-mailer| | | X | | | |
|filename| | | X | X | | X |
|filename&#124;authentihash| | | X | X | | |
|filename&#124;impfuzzy| | | X | X | | |
|filename&#124;imphash| | | X | X | | |
|filename&#124;md5| | | X | X | | |
|filename&#124;pehash| | | X | X | | |
|filename&#124;sha1| | | X | X | | |
|filename&#124;sha224| | | X | X | | |
|filename&#124;sha256| | | X | X | | |
|filename&#124;sha384| | | X | X | | |
|filename&#124;sha512| | | X | X | | |
|filename&#124;sha512/224| | | X | X | | |
|filename&#124;sha512/256| | | X | X | | |
|filename&#124;ssdeep| | | X | X | | |
|filename&#124;tlsh| | | X | X | | |
|first-name| | | | | | |
|float| | X | | | | |
|frequent-flyer-number| | | | | | |
|gender| | | | | | |
|gene| | | | | | |
|github-organisation| | | | | | |
|github-repository| | | | | | |
|github-username| | | | | | |
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
|visa-number| | | | | | |
|vulnerability| | | X | X | | |
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

|Category| Person | Social network | Support Tool | Targeting data |
| --- |:---:|:---:|:---:|:---:|
|AS| | | | |
|aba-rtn| | | | |
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
|comment| X | X | X | X |
|cookie| | | | |
|cortex| | | | |
|counter| | | | |
|country-of-residence| X | | | |
|cpe| | | | |
|date-of-birth| X | | | |
|datetime| | | | |
|dns-soa-email| | | | |
|domain| | | | |
|domain&#124;ip| | | | |
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
|filename| | | | |
|filename&#124;authentihash| | | | |
|filename&#124;impfuzzy| | | | |
|filename&#124;imphash| | | | |
|filename&#124;md5| | | | |
|filename&#124;pehash| | | | |
|filename&#124;sha1| | | | |
|filename&#124;sha224| | | | |
|filename&#124;sha256| | | | |
|filename&#124;sha384| | | | |
|filename&#124;sha512| | | | |
|filename&#124;sha512/224| | | | |
|filename&#124;sha512/256| | | | |
|filename&#124;ssdeep| | | | |
|filename&#124;tlsh| | | | |
|first-name| X | | | |
|float| | | | |
|frequent-flyer-number| X | | | |
|gender| X | | | |
|gene| | | | |
|github-organisation| | X | | |
|github-repository| | X | | |
|github-username| | X | | |
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
|visa-number| X | | | |
|vulnerability| | | | |
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
*   **comment**: Comment or description in a human language
*   **cookie**: HTTP cookie as often stored on the user web client. This can include authentication cookie or session cookie.
*   **cortex**: Cortex analysis result
*   **counter**: An integer counter, generally to be used in objects
*   **country-of-residence**: The country of residence of a natural person
*   **cpe**: Common platform enumeration
*   **date-of-birth**: Date of birth of a natural person (in YYYY-MM-DD format)
*   **datetime**: Datetime in the ISO 8601 format
*   **dns-soa-email**: RFC1035 mandates that DNS zones should have a SOA (Statement Of Authority) record that contains an email address where a PoC for the domain could be contacted. This can sometimes be used for attribution/linkage between different domains even if protected by whois privacy
*   **domain**: A domain name used in the malware
*   **domain&#124;ip**: A domain name and its IP address (as found in DNS lookup) separated by a &#124;
*   **email-attachment**: File name of the email attachment.
*   **email-body**: Email body
*   **email-dst**: A recipient email address
*   **email-dst-display-name**: Email destination display name
*   **email-header**: Email header
*   **email-message-id**: The email message ID
*   **email-mime-boundary**: The email mime boundary separating parts in a multipart email
*   **email-reply-to**: Email reply to header
*   **email-src**: The email address used to send the malware.
*   **email-src-display-name**: Email source display name
*   **email-subject**: The subject of the email
*   **email-thread-index**: The email thread index header
*   **email-x-mailer**: Email x-mailer header
*   **filename**: Filename
*   **filename&#124;authentihash**: A checksum in md5 format
*   **filename&#124;impfuzzy**: Import fuzzy hash - a fuzzy hash created based on the imports in the sample.
*   **filename&#124;imphash**: Import hash - a hash created based on the imports in the sample.
*   **filename&#124;md5**: A filename and an md5 hash separated by a &#124;
*   **filename&#124;pehash**: A filename and a PEhash separated by a &#124;
*   **filename&#124;sha1**: A filename and an sha1 hash separated by a &#124;
*   **filename&#124;sha224**: A filename and a sha-224 hash separated by a &#124;
*   **filename&#124;sha256**: A filename and an sha256 hash separated by a &#124;
*   **filename&#124;sha384**: A filename and a sha-384 hash separated by a &#124;
*   **filename&#124;sha512**: A filename and a sha-512 hash separated by a &#124;
*   **filename&#124;sha512/224**: A filename and a sha-512/224 hash separated by a &#124;
*   **filename&#124;sha512/256**: A filename and a sha-512/256 hash separated by a &#124;
*   **filename&#124;ssdeep**: A checksum in ssdeep format
*   **filename&#124;tlsh**: A filename and a Trend Micro Locality Sensitive Hash separated by a &#124;
*   **first-name**: First name of a natural person
*   **float**: A floating point value.
*   **frequent-flyer-number**: The frequent flyer number of a passenger
*   **gender**: The gender of a natural person (Male, Female, Other, Prefer not to say)
*   **gene**: GENE - Go Evtx sigNature Engine
*   **github-organisation**: A github organisation
*   **github-repository**: A github repository
*   **github-username**: A github user name
*   **hex**: A value in hexadecimal format
*   **hostname**: A full host/dnsname of an attacker
*   **hostname&#124;port**: Hostname and port number seperated by a &#124;
*   **http-method**: HTTP method used by the malware (e.g. POST, GET, ...).
*   **iban**: International Bank Account Number
*   **identity-card-number**: Identity card number
*   **impfuzzy**: A fuzzy hash of import table of Portable Executable format
*   **imphash**: Import hash - a hash created based on the imports in the sample.
*   **ip-dst**: A destination IP address of the attacker or C&C server
*   **ip-dst&#124;port**: IP destination and port number seperated by a &#124;
*   **ip-src**: A source IP address of the attacker
*   **ip-src&#124;port**: IP source and port number seperated by a &#124;
*   **issue-date-of-the-visa**: The date on which the visa was issued
*   **ja3-fingerprint-md5**: JA3 is a method for creating SSL/TLS client fingerprints that should be easy to produce on any platform and can be easily shared for threat intelligence.
*   **jabber-id**: Jabber ID
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
*   **visa-number**: Visa number
*   **vulnerability**: A reference to the vulnerability used in the exploit
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
:   CERT-XLM Security Incident Classification.

[DML](https://github.com/MISP/misp-taxonomies/tree/master/DML):
:   The Detection Maturity Level (DML) model is a capability maturity model for referencing ones maturity in detecting cyber attacks.  It's designed for organizations who perform intel-driven detection and response and who put an emphasis on having a mature detection program.

[PAP](https://github.com/MISP/misp-taxonomies/tree/master/PAP):
:   The Permissible Actions Protocol - or short: PAP - was designed to indicate how the received information can be used.

[access-method](https://github.com/MISP/misp-taxonomies/tree/master/access-method):
:   The access method used to remotely access a system.

[accessnow](https://github.com/MISP/misp-taxonomies/tree/master/accessnow):
:   Access Now classification to classify an issue (such as security, human rights, youth rights).

[action-taken](https://github.com/MISP/misp-taxonomies/tree/master/action-taken):
:   Action taken in the case of a security incident (CSIRT perspective).

[admiralty-scale](https://github.com/MISP/misp-taxonomies/tree/master/admiralty-scale):
:   The Admiralty Scale (also called the NATO System) is used to rank the reliability of a source and the credibility of an information.

[adversary](https://github.com/MISP/misp-taxonomies/tree/master/adversary):
:   An overview and description of the adversary infrastructure.

[ais-marking](https://github.com/MISP/misp-taxonomies/tree/master/ais-marking):
:   AIS Marking Schema implementation is maintained by the National Cybersecurity and Communication Integration Center (NCCIC) of the U.S. Department of Homeland Security (DHS)

[analyst-assessment](https://github.com/MISP/misp-taxonomies/tree/master/analyst-assessment):
:   A series of assessment predicates describing the analyst capabilities to perform analysis. These assessment can be assigned by the analyst him/herself or by another party evaluating the analyst.

[approved-category-of-action](https://github.com/MISP/misp-taxonomies/tree/master/approved-category-of-action):
:   A pre-approved category of action for indicators being shared with partners (MIMIC).

[binary-class](https://github.com/MISP/misp-taxonomies/tree/master/binary-class):
:   Custom taxonomy for types of binary file.

[cccs](https://github.com/MISP/misp-taxonomies/tree/master/cccs):
:   Internal taxonomy for CCCS.

[circl](https://github.com/MISP/misp-taxonomies/tree/master/circl):
:   CIRCL Taxonomy is a simple scheme for incident classification and area topic where the incident took place.

[collaborative-intelligence](https://github.com/MISP/misp-taxonomies/tree/master/collaborative-intelligence):
:   Collaborative intelligence support language is a common language to support analysts to perform their analysis to get crowdsourced support when using threat intelligence sharing platform like MISP.

[copine-scale](https://github.com/MISP/misp-taxonomies/tree/master/copine-scale):
:   The COPINE Scale is a rating system created in Ireland and used in the United Kingdom to categorise the severity of images of child sex abuse.

[csirt_case_classification](https://github.com/MISP/misp-taxonomies/tree/master/csirt_case_classification):
:   FIRST CSIRT Case Classification.

[cssa](https://github.com/MISP/misp-taxonomies/tree/master/cssa):
:   The CSSA agreed sharing taxonomy.

[cyber-threat-framework](https://github.com/MISP/misp-taxonomies/tree/master/cyber-threat-framework):
:   Cyber Threat Framework was developed by the US Government to enable consistent characterization and categorization of cyber threat events, and to identify trends or changes in the activities of cyber adversaries. https://www.dni.gov/index.php/cyber-threat-framework

[data-classification](https://github.com/MISP/misp-taxonomies/tree/master/data-classification):
:   Data classification for data potentially at risk of exfiltration based on table 2.1 of Solving Cyber Risk book.

[ddos](https://github.com/MISP/misp-taxonomies/tree/master/ddos):
:   Distributed Denial of Service - or short: DDoS - taxonomy supports the description of Denial of Service attacks and especially the types they belong too.

[de-vs](https://github.com/MISP/misp-taxonomies/tree/master/de-vs):
:   Taxonomy for the handling of protectively marked information in MISP with German (DE) Government classification markings (VS)

[dhs-ciip-sectors](https://github.com/MISP/misp-taxonomies/tree/master/dhs-ciip-sectors):
:   DHS critical sectors as described in https://www.dhs.gov/critical-infrastructure-sectors.

[diamond-model](https://github.com/MISP/misp-taxonomies/tree/master/diamond-model):
:   The Diamond Model for Intrusion Analysis, a phase-based model developed by Lockheed Martin, aims to help categorise and identify the stage of an attack.

[dni-ism](https://github.com/MISP/misp-taxonomies/tree/master/dni-ism):
:   ISM (Information Security Marking Metadata) V13 as described by DNI.gov (Director of National Intelligence - US).

[domain-abuse](https://github.com/MISP/misp-taxonomies/tree/master/domain-abuse):
:   Taxonomy to tag domain names used for cybercrime.

[economical-impact](https://github.com/MISP/misp-taxonomies/tree/master/economical-impact):
:   Economical impact is a taxonomy to describe the financial impact as positive or negative gain to the tagged information.

[ecsirt](https://github.com/MISP/misp-taxonomies/tree/master/ecsirt):
:   eCSIRT incident classification Appendix C of the eCSIRT EU project including IntelMQ updates.

[enisa](https://github.com/MISP/misp-taxonomies/tree/master/enisa):
:   ENISA Threat Taxonomy - A tool for structuring threat information as published in https://www.enisa.europa.eu/topics/threat-risk-management/threats-and-trends/enisa-threat-landscape/etl2015/enisa-threat-taxonomy-a-tool-for-structuring-threat-information

[estimative-language](https://github.com/MISP/misp-taxonomies/tree/master/estimative-language):
:   Estimative language - including likelihood or probability of event based on the Intelligence Community Directive 203 (ICD 203) (6.2.(a)) and JP 2-0, Joint Intelligence.

[eu-marketop-and-publicadmin](https://github.com/MISP/misp-taxonomies/tree/master/eu-marketop-and-publicadmin):
:   Market operators and public administrations that must comply to some notifications requirements under EU NIS directive.

[eu-nis-sector-and-subsectors](https://github.com/MISP/misp-taxonomies/tree/master/eu-nis-sector-and-subsectors):
:   Sectors and sub sectors as identified by the NIS Directive.

[euci](https://github.com/MISP/misp-taxonomies/tree/master/euci):
:   EU classified information (EUCI) means any information or material designated by a EU security classification, the unauthorised disclosure of which could cause varying degrees of prejudice to the interests of the European Union or of one or more of the Member States as described in http://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32013D0488&from=EN

[europol-event](https://github.com/MISP/misp-taxonomies/tree/master/europol-event):
:   EUROPOL type of events taxonomy.

[europol-incident](https://github.com/MISP/misp-taxonomies/tree/master/europol-incident):
:   EUROPOL class of incident taxonomy.

[event-assessment](https://github.com/MISP/misp-taxonomies/tree/master/event-assessment):
:   A series of assessment predicates describing the event assessment performed to make judgement(s) under a certain level of uncertainty.

[event-classification](https://github.com/MISP/misp-taxonomies/tree/master/event-classification):
:   Event Classification.

[exercise](https://github.com/MISP/misp-taxonomies/tree/master/exercise):
:   Exercise is a taxonomy to describe if the information is part of one or more cyber or crisis exercise.

[false-positive](https://github.com/MISP/misp-taxonomies/tree/master/false-positive):
:   This taxonomy aims to ballpark the expected amount of false positives.

[file-type](https://github.com/MISP/misp-taxonomies/tree/master/file-type):
:   List of known file types.

[fpf](https://github.com/MISP/misp-taxonomies/tree/master/fpf):
:   The Future of Privacy Forum (FPF) [visual guide to practical de-identification](https://fpf.org/2016/04/25/a-visual-guide-to-practical-data-de-identification/) taxonomy is used to evaluate the degree of identifiability of personal data and the types of pseudonymous data, de-identified data and anonymous data. The work of FPF is licensed under a creative commons attribution 4.0 international license.

[fr-classif](https://github.com/MISP/misp-taxonomies/tree/master/fr-classif):
:   French gov information classification system.

[gdpr](https://github.com/MISP/misp-taxonomies/tree/master/gdpr):
:   Taxonomy related to the REGULATION (EU) 2016/679 OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL on the protection of natural persons with regard to the processing of personal data and on the free movement of such data, and repealing Directive 95/46/EC (General Data Protection Regulation)

[gsma-attack-category](https://github.com/MISP/misp-taxonomies/tree/master/gsma-attack-category):
:   Taxonomy used by GSMA for their information sharing program with telco describing the attack categories

[gsma-fraud](https://github.com/MISP/misp-taxonomies/tree/master/gsma-fraud):
:   Taxonomy used by GSMA for their information sharing program with telco describing the various aspects of fraud

[gsma-network-technology](https://github.com/MISP/misp-taxonomies/tree/master/gsma-network-technology):
:   Taxonomy used by GSMA for their information sharing program with telco describing the types of infrastructure. WiP

[honeypot-basic](https://github.com/MISP/misp-taxonomies/tree/master/honeypot-basic):
:   Christian Seifert, Ian Welch, Peter Komisarczuk, ‘Taxonomy of Honeypots’, Technical Report CS-TR-06/12, VICTORIA UNIVERSITY OF WELLINGTON, School of Mathematical and Computing Sciences, June 2006, http://www.mcs.vuw.ac.nz/comp/Publications/archive/CS-TR-06/CS-TR-06-12.pdf

[iep](https://github.com/MISP/misp-taxonomies/tree/master/iep):
:   Forum of Incident Response and Security Teams (FIRST) Information Exchange Policy (IEP) framework.

[ifx-vetting](https://github.com/MISP/misp-taxonomies/tree/master/ifx-vetting):
:   The IFX taxonomy is used to categorise information (MISP events and attributes) to aid in the intelligence vetting process

[incident-disposition](https://github.com/MISP/misp-taxonomies/tree/master/incident-disposition):
:   How an incident is classified in its process to be resolved. The taxonomy is inspired from NASA Incident Response and Management Handbook.

[infoleak](https://github.com/MISP/misp-taxonomies/tree/master/infoleak):
:   A taxonomy describing information leaks and especially information classified as being potentially leaked.

[information-security-indicators](https://github.com/MISP/misp-taxonomies/tree/master/information-security-indicators):
:   Information security indicators have been standardized by the ETSI Industrial Specification Group (ISG) ISI. These indicators provide the basis to switch from a qualitative to a quantitative culture in IT Security Scope of measurements: External and internal threats (attempt and success), user's deviant behaviours, nonconformities and/or vulnerabilities (software, configuration, behavioural, general security framework). ETSI GS ISI 001-1 (V1.1.2): ISI Indicators

[interception-method](https://github.com/MISP/misp-taxonomies/tree/master/interception-method):
:   The interception method used to intercept traffic.

[kill-chain](https://github.com/MISP/misp-taxonomies/tree/master/kill-chain):
:   Cyber Kill Chain from Lockheed Martin as described in Intelligence-Driven Computer Network Defense Informed by Analysis of Adversary Campaigns and Intrusion Kill Chains.

[maec-delivery-vectors](https://github.com/MISP/misp-taxonomies/tree/master/maec-delivery-vectors):
:   Vectors used to deliver malware based on MAEC 5.0

[maec-malware-behavior](https://github.com/MISP/misp-taxonomies/tree/master/maec-malware-behavior):
:   Malware behaviours based on MAEC 5.0

[maec-malware-capabilities](https://github.com/MISP/misp-taxonomies/tree/master/maec-malware-capabilities):
:   Malware Capabilities based on MAEC 5.0

[maec-malware-obfuscation-methods](https://github.com/MISP/misp-taxonomies/tree/master/maec-malware-obfuscation-methods):
:   Obfuscation methods used by malware based on MAEC 5.0

[malware_classification](https://github.com/MISP/misp-taxonomies/tree/master/malware_classification):
:   Malware classification based on a SANS whitepaper about malware.

[misp](https://github.com/MISP/misp-taxonomies/tree/master/misp):
:   Internal MISP taxonomy.

[monarc-threat](https://github.com/MISP/misp-taxonomies/tree/master/monarc-threat):
:   MONARC threat taxonomy.

[ms-caro-malware](https://github.com/MISP/misp-taxonomies/tree/master/ms-caro-malware):
:   Malware Type and Platform classification based on Microsoft's implementation of the Computer Antivirus Research Organization (CARO) Naming Scheme and Malware Terminology.

[ms-caro-malware-full](https://github.com/MISP/misp-taxonomies/tree/master/ms-caro-malware-full):
:   Malware Type and Platform classification based on Microsoft's implementation of the Computer Antivirus Research Organization (CARO) Naming Scheme and Malware Terminology.

[nato](https://github.com/MISP/misp-taxonomies/tree/master/nato):
:   Marking of Classified and Unclassified materials as described by the North Atlantic Treaty Organization, NATO.

[nis](https://github.com/MISP/misp-taxonomies/tree/master/nis):
:   NIS Cybersecurity Incident Taxonomy.

[open_threat](https://github.com/MISP/misp-taxonomies/tree/master/open_threat):
:   Open Threat Taxonomy v1.1 base on James Tarala of SANS ref. - http://www.auditscripts.com/resources/open_threat_taxonomy_v1.1a.pdf

[osint](https://github.com/MISP/misp-taxonomies/tree/master/osint):
:   Open Source Intelligence - Classification (MISP taxonomies).

[passivetotal](https://github.com/MISP/misp-taxonomies/tree/master/passivetotal):
:   Tags for RiskIQ's passivetotal service

[pentest](https://github.com/MISP/misp-taxonomies/tree/master/pentest):
:   Penetration test (pentest) classification.

[priority-level](https://github.com/MISP/misp-taxonomies/tree/master/priority-level):
:   After an incident is scored, it is assigned a priority level. The six levels listed below are aligned with NCCIC, DHS, and the CISS to help provide a common lexicon when discussing incidents. This priority assignment drives NCCIC urgency, pre-approved incident response offerings, reporting requirements, and recommendations for leadership escalation. Generally, incident priority distribution should follow a similar pattern to the graph below. Based on https://www.us-cert.gov/NCCIC-Cyber-Incident-Scoring-System.

[rsit](https://github.com/MISP/misp-taxonomies/tree/master/rsit):
:   Reference Security Incident Classification Taxonomy.

[rt_event_status](https://github.com/MISP/misp-taxonomies/tree/master/rt_event_status):
:   Status of events used in Request Tracker.

[runtime-packer](https://github.com/MISP/misp-taxonomies/tree/master/runtime-packer):
:   Runtime or software packer used to combine compressed data with the decompression code. The decompression code can add additional obfuscations mechanisms including polymorphic-packer or other obfuscation techniques. This taxonomy lists all the known or official packer used for legitimate use or for packing malicious binaries.

[smart-airports-threats](https://github.com/MISP/misp-taxonomies/tree/master/smart-airports-threats):
:   Threat taxonomy in the scope of securing smart airports by ENISA.

[stealth_malware](https://github.com/MISP/misp-taxonomies/tree/master/stealth_malware):
:   Classification based on malware stealth techniques.

[stix-ttp](https://github.com/MISP/misp-taxonomies/tree/master/stix-ttp):
:   Representation of the behavior or modus operandi of cyber adversaries (a.k.a TTP) as normalized in STIX

[targeted-threat-index](https://github.com/MISP/misp-taxonomies/tree/master/targeted-threat-index):
:   The Targeted Threat Index is a metric for assigning an overall threat ranking score to email messages that deliver malware to a victim’s computer. The TTI metric was first introduced at SecTor 2013 by Seth Hardy as part of the talk “RATastrophe: Monitoring a Malware Menagerie” along with Katie Kleemola and Greg Wiseman.

[tlp](https://github.com/MISP/misp-taxonomies/tree/master/tlp):
:   The Traffic Light Protocol - or short: TLP - was designed with the objective to create a favorable classification scheme for sharing sensitive information while keeping the control over its distribution at the same time. Extended with TLP:EX:CHR.

[tor](https://github.com/MISP/misp-taxonomies/tree/master/tor):
:   Taxonomy to describe Tor network infrastructure

[type](https://github.com/MISP/misp-taxonomies/tree/master/type):
:   Taxonomy to describe different types of intelligence gathering discipline which can be described the origin of intelligence.

[use-case-applicability](https://github.com/MISP/misp-taxonomies/tree/master/use-case-applicability):
:   The Use Case Applicability categories reflect standard resolution categories, to clearly display alerting rule configuration problems.

[veris](https://github.com/MISP/misp-taxonomies/tree/master/veris):
:   Vocabulary for Event Recording and Incident Sharing (VERIS).

[vocabulaire-des-probabilites-estimatives](https://github.com/MISP/misp-taxonomies/tree/master/vocabulaire-des-probabilites-estimatives):
:   Vocabulaire des probabilités estimatives

[workflow](https://github.com/MISP/misp-taxonomies/tree/master/workflow):
:   Workflow support language is a common language to support intelligence analysts to perform their analysis on data and information.


## MISP Galaxy

MISP galaxy is a simple method to express a large object called cluster that can be attached to MISP events or attributes. A cluster can be composed of one or more elements. Elements are expressed as key-values. There are default vocabularies available in MISP galaxy but those can be overwritten, replaced or updated as you wish. Existing clusters and vocabularies can be used as-is or as a template. MISP distribution can be applied to each cluster to permit a limited or broader distribution scheme. Many MISP galaxy clusters are already available like Exploit-Kit, Microsoft Activity Group actor, Preventive Measure, 
Ransomware, TDS, Threat actor or Tool used by adversaries.

The galaxy can be [browsed via the web site](/galaxy.html) or downloaded as [PDF](/galaxy.pdf) or directly via the MISP software.
