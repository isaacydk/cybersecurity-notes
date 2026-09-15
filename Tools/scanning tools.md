
# Automated Scanning
## Vulnerability Scanners
### Nessus: Comprehensive Vulnerability Scanner
- Basic Network Scan
- Web Application Tests
- Configuration Audit
- Compliance Checks
- Malware Scan'

### OpenVAS: Open Source Vulnerability Scanner

- **Scanner Setup**:
    - `openvas-setup` - Initial configuration and database setup
    - `openvas-start` - Start OpenVAS services and scanner daemon
- **Scan Task Creation**:
    - `omp -u admin -w admin -X '<create_task><name>Network Scan</name><target>192.168.1.0/24</target><config>Full and fast</config></create_task>'`
    - Creates new vulnerability scan tasks with specified targets and configurations
- **Scan Execution**:
    - `omp -u admin -w admin -X '<start_task task_id="task_id"/>'`
    - Initiates scanning process for configured targets
- **Results Retrieval**:
    - `omp -u admin -w admin -X '<get_tasks/>'`
    - Retrieves scan results and vulnerability findings


## Web Application Scanners

### OWASP ZAP: Web Application Security Scanner

- **Quick Scanning**:
    - `zap-cli quick-scan --self-contained --start-options "-config api.disablekey=true" https://target.com`
    - Rapid vulnerability assessment with basic security checks
- **Comprehensive Scanning**:
    - `zap-cli full-scan --self-contained --start-options "-config api.disablekey=true" https://target.com`
    - Complete security assessment including passive and active scanning
- **Application Crawling**:
    - `zap-cli spider https://target.com`
    - Automated discovery of application endpoints and functionality
- **Active Vulnerability Testing**:
    - `zap-cli active-scan https://target.com`
    - Targeted vulnerability testing with attack payloads
- **Report Generation**:
    - `zap-cli report -o report.html -f html`
    - Comprehensive vulnerability reports in multiple formats

### Burp Suite: Web Application Testing Platform

Key Burp Suite components:

- **Proxy:** Intercept and modify traffic
- **Scanner:** Automated vulnerability detection
- **Intruder:** Custom attack automation
- **Repeater:** Manual request manipulation
- **Sequencer:** Token analysis

## Database Scanners

### SQLMap: SQL Injection Scanner

- **Basic Vulnerability Detection**:
    - `sqlmap -u "http://target.com/page.php?id=1"`
    - Automated detection of SQL injection vulnerabilities in web parameters
- **Database Enumeration**:Key capabilities:

- **MongoDB scanning**
- **CouchDB scanning**
- **Redis scanning**
- **Authentication testing**
- **Data extraction**

    - `sqlmap -u "http://target.com/page.php?id=1" --dbs` - List available databases
    - `sqlmap -u "http://target.com/page.php?id=1" -D dbname --tables` - Enumerate database tables
    - `sqlmap -u "http://target.com/page.php?id=1" -D dbname -T tablename --columns` - List table columns
- **Data Extraction**:
    - `sqlmap -u "http://target.com/page.php?id=1" -D dbname -T tablename -C column --dump`
    - Extract sensitive data from identified database tables
- **Advanced Testing Options**:
    - `sqlmap -u "http://target.com/page.php?id=1" --level=5 --risk=3` - Aggressive testing with high detection levels
    - `sqlmap -u "http://target.com/page.php?id=1" --batch --random-agent` - Automated testing with evasion techniques

### NoSQLMap: NoSQL Database Scanner

Key capabilities:

- **MongoDB scanning**
- **CouchDB scanning**
- **Redis scanning**
- **Authentication testing**
- **Data extraction**


## Cloude Security Scanner
- AWS Security tools
- Azure Security Scanner

## Container Security Scanners
- Doker Security Scanning
- Kubernates Security tools


# Manual Network Scanning

### Phase 1: Host Discovery

**The Foundation Layer**

- Identify which hosts are actually online and responding
- Determine the scope of active targets
- Filter out non-responsive systems
- Create a baseline of live hosts for further investigation

```
- **Ping Sweep**:
    - `nmap -sn 192.168.1.0/24` - Standard ping sweep across subnet
- **ARP Scan**:
    - `nmap -sn -PR 192.168.1.0/24` - ARP-based host discovery
- **ICMP Echo Scan**:
    - `nmap -sn -PE 192.168.1.0/24` - ICMP echo request scan
- **TCP SYN Ping**:
    - `nmap -sn -PS22,80,443 192.168.1.0/24` - TCP SYN ping to common ports
      
```

### Phase 2: Port Discovery

**The Service Layer**

- Scan discovered hosts to identify open ports
- Determine which services are listening
- Map the attack surface of each host
- Identify potential entry points

```
- **TCP SYN Scan (Stealth)**:
    - `nmap -sS 192.168.1.10` - Half-open scan for stealth
- **TCP Connect Scan**:
    - `nmap -sT 192.168.1.10` - Full TCP connection scan
- **UDP Scan**:
    - `nmap -sU 192.168.1.10` - UDP port scanning
- **Common Ports Scan**:
    - `nmap -sS -p 21,22,23,25,53,80,110,111,135,139,143,443,993,995,1723,3306,3389,5900,8080 192.168.1.10`

```

### Phase 3: Service Identification

**The Application Layer**

- Determine what specific services are running
- Identify software versions and configurations
- Map service dependencies and relationships
- Understand the technology stack

```
- **Service and Version Detection**:
    - `nmap -sV 192.168.1.10` - Identify service versions
- **Aggressive Service Detection**:
    - `nmap -sV -sC 192.168.1.10` - Version detection with default scripts
- **OS Detection**:
    - `nmap -O 192.168.1.10` - Operating system fingerprinting
- **Comprehensive Scan**:
    - `nmap -sS -sV -O -sC 192.168.1.10` - Complete service analysis
      
```

### Phase 4: Vulnerability Assessment

**The Security Layer**

- Research known vulnerabilities for identified services (think Exploit-DB, CVE database's)
- Analyze version-specific security issues
- Identify misconfigurations and weaknesses
- Prioritize potential attack vectors
- Scan for service and vulnerability specific vulnerabilities.
    - This can be with Nmap or we can pivot to Exploit frameworks to confirm the vulnerabilities such as Metasploit

```
- **Nmap Vulnerability Scripts**:
    - `nmap --script vuln 192.168.1.10` - General vulnerability scanning
- **Specific Vulnerability Checks**:
    - `nmap --script vulners 192.168.1.10` - CVE database checks
- **Service-Specific Vulnerability Checks**:
    - `nmap --script ssh* 192.168.1.10` - SSH vulnerability scripts
    - `nmap --script http* 192.168.1.10` - HTTP vulnerability scripts
    - `nmap --script mysql* 192.168.1.10` - MySQL vulnerability scripts
- **Metasploit Vulnerability Scanning**:
    - `msfconsole -q -x "use auxiliary/scanner/portscan/tcp; set RHOSTS 192.168.1.10; run"`
      
```

**Scanning Methodology Flow:**

```
[Host Discovery] → [Port Discovery] → [Service ID] → [Vuln Research]
       |                |                |              |
       v                v                v              v
   Find Live         Find Open        Identify      Research
    Hosts             Ports          Services      Vulnerabilities
       |                |                |              |
       v                v                v              v
   Reduce Scope     Focus Effort    Get Details    Plan Attacks
```

More on [[Nmap]]
