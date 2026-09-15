
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


-sS   --TCP half open scans for stealth