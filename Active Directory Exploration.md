Server Message Block (SMB) is a critical network protocol used for file sharing, printer access, and inter-process communication in Windows environments.
## Critical SMB Vulnerabilities

- MS17-010 (EternalBlue)
- CVE-2020-0796 (SMBGhost)

Command-line tools for SMB reconnaissance
```
- **smbclient**:
    - `smbclient -L //target` - List shares
    - `smbclient -N //target/share` - Connect with null session
    - `smbclient -U username //target/share` - Authenticated connection
- **smbmap**:
    - `smbmap -H target` - Enumerate shares and permissions
    - `smbmap -H target -u username -p password` - Authenticated enumeration
    - `smbmap -H target -R` - Recursive directory listing
- **enum4linux**:
    - `enum4linux -a target` - Comprehensive enumeration
    - `enum4linux -U target` - User enumeration
    - `enum4linux -S target` - Share enumeration
```

