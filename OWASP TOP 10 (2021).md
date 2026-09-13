# A01:2021 - [[Broken Access Control]]

**Vertical access control failures** - when the user can access the higher lever functionalities that they sholdn't have permission on 
**Horizontal access control failures** - when the user can access other users data at the same level (eg can see other people bank account)

Finding access contorl issues
- Access resources without authentication
- Access resources as the wrong user type
- Modify URL parameters to reach unauthorised resources
- Test API endpoints directly, bypassing client-side restrictions
- Manipulate tokens or session identifiers

 Prevention Strategies
 - centralised mechanisms
 - denay by default
 - regular testing
# A02:2021 - Cryptographic Failures

previously known as "Sensitive Data Exposure," encompass vulnerabilities resulting from improper implementation of cryptographic controls or the complete lack thereof.

storing password hashes without proper salting makes them vulnerable to rainbow table attacks, potentially compromising user accounts.

#### Common Cryptographic Issues
- weak protocols and algorithms -like MD5 or SHA-1
- Poor key management - must implement secure processes for key generation, storage, distribution, and rotation.
# A03:2021 - [[Injection]]
#### Prevention Strategies
- use parameterised Queries
- Input Validation

# A04:2021 - Insecure Design
#### Common Design Flaws
- Business logic flaws
- missing security controls
#### Prevention Strategies
- Threat modeling
- secure design patterns

# A05:2021 - Security Misconfiguration
#### Common Misconfigurations
- Default credentials
- unnecessary features
- error handling
#### Prevention Approaches
- Secure BAseline
- regular auditing

# A06:2021 - Vulnerable and Outdated Components

# A07:2021 - [[Identification and Authentication Failures]]
#### Common Authentication Weaknesses
- Weak Password Requirements
- Session Management Flaws
#### Prevention Approaches
- Multi-Factor Authentication
- Password Security
# A08:2021 - Software and Data Integrity Failures
#### Prevention Strategies
- Digital Signatures
- Supply Chain Security

# A09:2021 - Security Logging and Monitoring Failures
#### Missing Critical Events
- Authentication attempts (both successful and failed)
- High-privilege operations
- Access to sensitive data
- Configuration changes
- Input validation failures
#### Poor Log Quality
- Missing crucial details in log entries
- Inconsistent log formats
- Lack of contextual information
- Insufficient timestamp precision
- Improper log storage

#### Implementing Effective Logging
##### Log Content Requirements
- Timestamp with timezone
- Event severity
- User identification
- Source information (IP address, device ID)
- Event description
- Affected system components

#### Log Protection
- Implement write-only access for log generation
- Use secure transmission for log data
- Maintain proper log retention periods
- Implement backup procedures
- Ensure log integrity

# A10:2021 - Server-Side Request Forgery (SSRF)
manipulate a server into making requests to unintended destinations. This vulnerability has gained prominence with the increasing use of cloud services and complex web architectures.
#### Impact of SSRF
- INTERNAL network access
- data exposure
#### Prevention Strategies
- input validation
- Network Controls

Security professionals should test for SSRF vulnerabilities by:

1. Attempting to access internal resources
2. Checking for cloud metadata endpoints
3. Verifying URL validation mechanisms