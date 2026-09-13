# Supported Scans
 - Virtual Hosts44
 - Subdomains
 - Directories
 - S3 Buckets
 - Google cloud storage(GCS)
 - TFTP
 - Files

# Dir and File Enumeration

`$ gobuster dir -u example.com -w /usr/../../....txt`

dir - activate the directory and file discovery mode
-u URL
-w Worldlist
help mode

word list on secList  /usr/share/secList/Discovery/web-content/
defaul kali wordlist   /usr/share/wordlists/
 
 # Subdomain Discover
 
  `$ gobuster dns -d example.com -w /usr/share/secList/Discovery/DNS/...txt --wildcard`
  
  --wildcard 
  -d  Domain
  -i  ipAddress


# Virtual Hosts
- function of a web server it is used multiple domain have same server(ipAddress)

$ gobuster vhost -w worldlist -u url

