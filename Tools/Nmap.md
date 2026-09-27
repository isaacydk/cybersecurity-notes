
```
nmap scanme.nmap.org -sp  --SAME AS PING(FASTER)
nmap scanme.nmap.org -sT  --FULL TCP SCAN(3 WAY HANDSHAKE)
nmap scanme.nmap.org      --WITHOUT THE 3 WAY HANDSHAKE

nmap scanme.nmap.org -sV   -- VERSION OF THE SERVICE
sudo nmap scanme.nmap.org -O  -- OPERATING SYSTEM
nmap scanme.nmap.org .... -p80,22,21 --TO FOCUS ON SPECIFIED PROTS

```

To make the firewall respond with a RST TCP packet (makes it extremely difficult to get accurate reading by nmap)

`iptables -I INPUT -p tcp --dport <port> -j REJECT --reject-with tcp-reset`   


-sT  --TCP full hand shake
-sS   --TCP half open scans for stealth

`-sU --top-ports 20 <target>`. Will scan the top 20 most commonly used UDP ports, resulting in a much more acceptable scan time.

-sN --NULL SCAN request with no flag
-sF --FIN flag usually used to gracefully close an active connection
-sX -- xmas send a malformed TCP packet
-vv -- to increare the verbosity in your scans

`nmap -sn 192.168.0.0/24 0r .1-254`  for ping sweep

There are many categories available. Some useful categories include:

- `safe`:- Won't affect the target
- `intrusive`:- Not safe: likely to affect the target  
    
- `vuln`:- Scan for vulnerabilities
- `exploit`:- Attempt to exploit a vulnerability
- `auth`:- Attempt to bypass authentication for running services (e.g. Log into an FTP server anonymously)
- `brute`:- Attempt to bruteforce credentials for running services
- `discovery`:- Attempt to query running services for further information about the network (e.g. query an SNMP server).

eg --script=vuln

--script-args -for scripts that require arguments 

`/usr/share/nmap/scripts`  -to find the scripts

-Pn -for invading firewalls by not pinging before scanning by passing ICMP block, takes a long time

