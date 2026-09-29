# 🧩 Challenge: 

## 📌 Info
- Category: Vulnerable machine
- Difficulty: easy
- Points: 
- Platform: Tryhackme

## 🔍 Recon
- URLs:
- IPs: 10.49.171.236
1. `nmap -sn 10.49.171.236`  to see the host is up  -> it is up
2.   nmap -sS -vv --top-ports 20 10.48.176.90 (to quickly scan top 20 commen ports ) -> port 80 was open 
3.  nmap -p80 -sV 10.48.176.90 --to check the version of the server -> nginx 1.16.1

## ⚔️ Exploitation
- Steps:-
1. 
2. 
3. 

## 🧠 Key Idea
> What was the core vulnerability?

## 🛠 Tools Used
- nmap
- burpsuite
- ffuf

## 🚩 Flag