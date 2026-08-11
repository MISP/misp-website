---
layout: page
title: Best Practices for MISP API Key Management 
permalink: /best-practices-for-misp-api-key-management/
toc: true
---

# Best Practices for MISP API Key Management

## Overview

API keys are a critical component of automation and integration in MISP. They allow users and external systems to interact with the MISP API without requiring interactive authentication. Because API keys can provide direct access to sensitive threat intelligence, sightings, attributes, events, objects, and administrative functions depending on the associated account permissions, they must be managed carefully.

This document provides best practices for creating, using, reviewing, and revoking MISP API keys in a secure and operationally sustainable way.

## General Principles

MISP API keys should be treated as sensitive credentials. Any system, script, integration, or user possessing a valid API key can perform actions allowed by the account and role associated with that key.

The recommended approach is to:

- Use short-lived or ephemeral API keys whenever possible.
- Assign API keys only the minimum required permissions.
- Revoke unused or suspicious keys immediately.
- Regularly review API key usage.
- Restrict API key usage to known IP addresses where possible.
- Avoid reusing the same API key across multiple systems or integrations.

## API Keys Are Not Stored in Clear Text

MISP does not store authentication keys in clear text. This reduces the risk of key disclosure from the database itself.

However, this does not remove the need for proper operational security. API keys may still be exposed through:

- Application configuration files.
- Environment variables.
- CI/CD logs.
- Command-line history.
- Backup files.
- SaaS platforms.
- Third-party integrations.
- Monitoring or debugging systems.
- Source code repositories.

For this reason, API keys should still be handled as secrets throughout their entire lifecycle.

## Prefer Ephemeral API Keys

Wherever possible, API keys should be ephemeral. An ephemeral API key is created for a specific purpose and a limited period of time, then revoked once it is no longer required.

This approach limits the impact of accidental exposure or compromise.

Examples of good use cases for ephemeral API keys include:

- Temporary data exports.
- One-off automation tasks.
- Short-term partner access.
- Testing or debugging integrations.
- Incident response workflows.
- Temporary synchronization jobs.

Long-lived API keys should be avoided unless there is a clear operational requirement.

## Revoke API Keys When No Longer Needed

MISP API keys can be easily revoked. Revocation should be part of the normal lifecycle of every API key.

API keys should be revoked when:

- The related integration is retired.
- The user or service account no longer needs access.
- The key was used for a temporary task.
- The key may have been exposed.
- The key shows unexpected activity.
- The associated system has been compromised.
- The person responsible for the key changes role or leaves the organization.

Revocation should be preferred over leaving unused keys active.

## Use Dedicated Accounts for API Access

Avoid using personal user accounts for long-running automation or system-to-system integrations.

Instead, create dedicated accounts for API access. These accounts should have:

- A clear purpose.
- A responsible owner.
- A limited role.
- Restricted ACLs.
- One or more dedicated API keys.
- Regular review.

Using dedicated accounts makes it easier to audit activity, identify the source of API usage, and revoke access without affecting human users.

## Apply the Principle of Least Privilege

API keys inherit the permissions of the account and role to which they are attached. For this reason, the associated account should have only the permissions required for the intended use case.

For example:

- Use a read-only account for integrations that only need to fetch events or attributes.
- Avoid using administrator accounts for automation unless strictly required.
- Create specific ACL profiles for specific API use cases.
- Separate ingestion, export, synchronization, and administrative functions into different accounts where practical.

A read-only API integration should not use an account with write or administrative privileges.

## Restrict API Keys by IP Address

MISP allows API key usage to be pinned or restricted to a defined set of IP addresses.

This is strongly recommended when the source IP addresses are known and stable.

IP restrictions help reduce the risk of misuse if an API key is leaked. Even if an attacker obtains the key, they cannot use it unless requests originate from an allowed IP address.

Recommended practices include:

- Restrict keys to known server, proxy, or NAT addresses.
- Use dedicated egress IP addresses for automation systems.
- Avoid allowing API keys from broad or unknown network ranges.
- Review IP restrictions when infrastructure changes.
- Remove obsolete IP addresses from allowed lists.

## Monitor and Review API Key Usage

MISP logs IP addresses for API key usage. These logs should be reviewed regularly to detect abnormal or unexpected activity.

Review should include:

- Last usage date.
- Source IP addresses.
- Frequency of use.
- Associated user or service account.
- Type of activity performed.
- Whether the key is still required.
- Whether the source IP addresses are expected.

Unexpected IP addresses, sudden increases in usage, or activity outside the expected use case should be investigated.

## Avoid Sharing API Keys

API keys should not be shared between users, teams, systems, or partners.

Each user, service, or integration should have its own API key. This improves:

- Accountability.
- Auditability.
- Revocation.
- Incident response.
- Access control.

If multiple systems use the same key, it becomes difficult to determine which system performed a specific action or where a leak occurred.

## Be Careful with SaaS and Third-Party Platforms

API keys extracted from MISP and configured in SaaS platforms or third-party services may be exposed to additional risks.

These risks include:

- Storage outside your direct control.
- Access by platform administrators.
- Logging by the platform.
- Exposure through support bundles or debug logs.
- Compromise of the third-party platform.
- Weak secret management practices.
- Unclear data retention policies.

Before placing a MISP API key in a SaaS platform, consider:

- Whether the integration is strictly necessary.
- Whether a read-only key is sufficient.
- Whether the key can be restricted by IP address.
- Whether the platform securely stores secrets.
- Whether the platform logs API requests or headers.
- Whether the key can be rotated or revoked easily.
- Whether the data accessed through the API is appropriate for that platform.

When in doubt, use a dedicated, restricted, ephemeral API key.

## Rotate API Keys Regularly

Regular rotation reduces the lifetime of exposed credentials.

The rotation interval should depend on the sensitivity of the MISP instance and the use case of the key. High-risk or externally stored keys should be rotated more frequently.

A good rotation process should include:

1. Create a new API key.
2. Update the consuming system or integration.
3. Verify that the new key works as expected.
4. Revoke the old key.
5. Confirm that the old key is no longer used.

Avoid creating new keys without revoking the old ones.

## Recommended API Key Lifecycle

A secure API key lifecycle should include the following steps:

1. **Request**
   - Define the purpose of the key.
   - Identify the responsible owner.
   - Determine required permissions.
   - Determine whether the key should be ephemeral.

2. **Creation**
   - Create the key for a dedicated user or service account.
   - Apply the minimum required ACL profile.
   - Restrict the key to known IP addresses where possible.

3. **Deployment**
   - Store the key securely.
   - Avoid exposing the key in logs, scripts, or repositories.
   - Use secret management systems where available.

4. **Monitoring**
   - Review usage logs.
   - Check source IP addresses.
   - Investigate unexpected activity.

5. **Review**
   - Confirm that the key is still needed.
   - Confirm that permissions are still appropriate.
   - Confirm that IP restrictions are still accurate.

6. **Revocation**
   - Revoke the key when it is no longer needed.
   - Revoke immediately if compromise is suspected.
   - Remove the key from external systems and configuration stores.

## Operational Checklist

When creating or reviewing a MISP API key, verify the following:

- [ ] The key has a documented purpose.
- [ ] The key has a responsible owner.
- [ ] The key is associated with a dedicated account where appropriate.
- [ ] The account has the minimum required ACL profile.
- [ ] The key is read-only if write access is not required.
- [ ] The key is ephemeral where possible.
- [ ] The key is restricted to known IP addresses where possible.
- [ ] The key is not shared between multiple systems or users.
- [ ] The key is stored securely.
- [ ] The key is not present in source code, logs, or public repositories.
- [ ] The key usage is reviewed regularly.
- [ ] The key is revoked when no longer required.

## Incident Response for Exposed API Keys

If a MISP API key is suspected to be exposed, leaked, misused, or compromised, it should be treated as a credential compromise.

The immediate response should be:

1. Revoke the affected API key immediately.
2. Identify the associated user or service account.
3. Review recent API usage linked to the key.
4. Check the source IP addresses used with the key.
5. Determine whether the key had read-only, write, synchronization, or administrative privileges.
6. Investigate whether unauthorized data access, modification, or configuration changes occurred.
7. Rotate any related credentials if they may have been exposed as well.
8. Review where the key was stored, transmitted, or logged.
9. Improve the storage or deployment process to prevent recurrence.
10. Create a new restricted key only if the integration is still required.

### Additional Checks for High-Privilege API Keys

If the exposed or compromised API key was associated with a highly privileged account, the investigation should include checks for persistence mechanisms and unauthorized configuration changes.

In particular, review whether the key was used to perform any of the following actions:

- Creation or modification of users.
- Creation, modification, or replacement of API keys.
- Modification of sharing groups, including the addition or injection of another organisation.
- Creation or modification of synchronisation connections.
- Changes to application settings.
- Changes to role permissions or ACL profiles.
- Creation or modification of workflows.

These actions may allow an attacker to maintain access, expand privileges, alter data-sharing boundaries, or establish unauthorized synchronization paths even after the original API key has been revoked.

### Persistence and Follow-up Review

After revoking the affected key, administrators should verify that no secondary access path remains active.

This should include:

- Reviewing recently created users and service accounts.
- Reviewing recently created or modified API keys.
- Checking whether new privileged accounts were added.
- Reviewing changes to roles and permissions.
- Reviewing sharing group membership and organisation changes.
- Checking synchronization server definitions and enabled sync connections.
- Reviewing recently created or modified workflows.
- Reviewing application settings for unexpected changes.
- Checking audit logs for administrative actions performed during the suspected compromise window.

If suspicious changes are found, they should be reverted, affected accounts or keys should be disabled or revoked, and the incident should be escalated according to the organisation's incident response process.

## Summary

MISP API keys are powerful credentials and should be managed with the same care as passwords or other secrets.

The most important recommendations are:

- Prefer ephemeral API keys.
- Use dedicated accounts for API integrations.
- Apply limited ACL profiles and least privilege.
- Use read-only access whenever possible.
- Restrict API keys to known IP addresses.
- Regularly review API key usage and source IP logs.
- Be cautious when placing API keys in SaaS or third-party platforms.
- Revoke unused, obsolete, or suspicious keys immediately.

Good API key hygiene reduces the risk of credential misuse, improves accountability, and supports secure automation in MISP environments.
