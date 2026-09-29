## 1. System Purpose
```
PS C:\Users\Administrator> hostname
DC-1
PS C:\Users\Administrator> systeminfo

Host Name:                 DC-1
OS Name:                   Microsoft Windows Server 2019 Datacenter
OS Version:                10.0.17763 N/A Build 17763
OS Manufacturer:           Microsoft Corporation
OS Configuration:          Primary Domain Controller
OS Build Type:             Multiprocessor Free
Registered Owner:          EC2
Registered Organization:   Amazon.com
Product ID:                00430-00000-00000-AA826
Original Install Date:     7/17/2021, 5:23:57 PM
System Boot Time:          9/17/2026, 7:46:47 AM
System Manufacturer:       Xen
System Model:              HVM domU
System Type:               x64-based PC
Processor(s):              1 Processor(s) Installed.
                           [01]: Intel64 Family 6 Model 79 Stepping 1 GenuineIntel ~2300 Mhz
BIOS Version:              Xen 4.11.amazon, 8/24/2006
Windows Directory:         C:\Windows
System Directory:          C:\Windows\system32
Boot Device:               \Device\HarddiskVolume1
System Locale:             en-us;English (United States)
Input Locale:              en-us;English (United States)
Time Zone:                 (UTC) Coordinated Universal Time
Total Physical Memory:     4,096 MB
Available Physical Memory: 2,498 MB
Virtual Memory: Max Size:  4,800 MB
Virtual Memory: Available: 3,153 MB
Virtual Memory: In Use:    1,647 MB
Page File Location(s):     C:\pagefile.sys
Domain:                    conda.local
Logon Server:              \\DC-1
Hotfix(s):                 30 Hotfix(s) Installed.
                           [01]: KB5004332
                           [02]: KB4470502
                           [03]: KB4470788
                           [04]: KB4480056
                           [05]: KB4486153
                           [06]: KB4493510
                           [07]: KB4499728
                           [08]: KB4504369
                           [09]: KB4512577
                           [10]: KB4512937
                           [11]: KB4521862
                           [12]: KB4523204
                           [13]: KB4535680
                           [14]: KB4539571
                           [15]: KB4549947
                           [16]: KB4558997
                           [17]: KB4562562
                           [18]: KB4566424
                           [19]: KB4570332
                           [20]: KB4577667
                           [21]: KB4587735
                           [22]: KB4589208
                           [23]: KB4598480
                           [24]: KB4601393
                           [25]: KB5000859
                           [26]: KB5001404
                           [27]: KB5003243
                           [28]: KB5003711
                           [29]: KB5005112
                           [30]: KB5005030
Network Card(s):           1 NIC(s) Installed.
                           [01]: AWS PV Network Device
                                 Connection Name: Ethernet
                                 DHCP Enabled:    Yes
                                 DHCP Server:     10.10.1.1
                                 IP address(es)
                                 [01]: 10.10.1.100
                                 [02]: fe80::88a3:7388:e822:ac71
Hyper-V Requirements:      A hypervisor has been detected. Features required for Hyper-V will not be displayed.
```

**System Role**
Role: Domain Controller (DC)
Domain: conda.local
Environment: Likely enterprise simulation


## 2. Open ports

```
PS C:\Users\Administrator> netstat -ano | findstr LISTENING
  TCP    0.0.0.0:88             0.0.0.0:0              LISTENING       816
  TCP    0.0.0.0:135            0.0.0.0:0              LISTENING       596
  TCP    0.0.0.0:389            0.0.0.0:0              LISTENING       816
  TCP    0.0.0.0:445            0.0.0.0:0              LISTENING       4
  TCP    0.0.0.0:464            0.0.0.0:0              LISTENING       816
  TCP    0.0.0.0:593            0.0.0.0:0              LISTENING       596
  TCP    0.0.0.0:636            0.0.0.0:0              LISTENING       816
  TCP    0.0.0.0:3268           0.0.0.0:0              LISTENING       816
  TCP    0.0.0.0:3269           0.0.0.0:0              LISTENING       816
  TCP    0.0.0.0:3389           0.0.0.0:0              LISTENING       1104
  TCP    0.0.0.0:5985           0.0.0.0:0              LISTENING       4
  TCP    0.0.0.0:9389           0.0.0.0:0              LISTENING       3268
  TCP    0.0.0.0:47001          0.0.0.0:0              LISTENING       4
  TCP    0.0.0.0:49664          0.0.0.0:0              LISTENING       676
  TCP    0.0.0.0:49665          0.0.0.0:0              LISTENING       1220
  TCP    0.0.0.0:49666          0.0.0.0:0              LISTENING       1860
  TCP    0.0.0.0:49667          0.0.0.0:0              LISTENING       2404
  TCP    0.0.0.0:49668          0.0.0.0:0              LISTENING       816
  TCP    0.0.0.0:49674          0.0.0.0:0              LISTENING       816
  TCP    0.0.0.0:49675          0.0.0.0:0              LISTENING       816
  TCP    0.0.0.0:49677          0.0.0.0:0              LISTENING       2720
  TCP    0.0.0.0:49693          0.0.0.0:0              LISTENING       796
  TCP    0.0.0.0:49705          0.0.0.0:0              LISTENING       3328
  TCP    0.0.0.0:49740          0.0.0.0:0              LISTENING       3320
  TCP    10.10.1.100:53         0.0.0.0:0              LISTENING       3328
  TCP    10.10.1.100:139        0.0.0.0:0              LISTENING       4
  TCP    127.0.0.1:53           0.0.0.0:0              LISTENING       3328
  TCP    [::]:88                [::]:0                 LISTENING       816
  TCP    [::]:135               [::]:0                 LISTENING       596
  TCP    [::]:389               [::]:0                 LISTENING       816
  TCP    [::]:445               [::]:0                 LISTENING       4
  TCP    [::]:464               [::]:0                 LISTENING       816
  TCP    [::]:593               [::]:0                 LISTENING       596
  TCP    [::]:636               [::]:0                 LISTENING       816
  TCP    [::]:3268              [::]:0                 LISTENING       816
  TCP    [::]:3269              [::]:0                 LISTENING       816
  TCP    [::]:3389              [::]:0                 LISTENING       1104
  TCP    [::]:5985              [::]:0                 LISTENING       4
  TCP    [::]:9389              [::]:0                 LISTENING       3268
  TCP    [::]:47001             [::]:0                 LISTENING       4
  TCP    [::]:49664             [::]:0                 LISTENING       676
  TCP    [::]:49665             [::]:0                 LISTENING       1220
  TCP    [::]:49666             [::]:0                 LISTENING       1860
  TCP    [::]:49667             [::]:0                 LISTENING       2404
  TCP    [::]:49668             [::]:0                 LISTENING       816
  TCP    [::]:49674             [::]:0                 LISTENING       816
  TCP    [::]:49675             [::]:0                 LISTENING       816
  TCP    [::]:49677             [::]:0                 LISTENING       2720
  TCP    [::]:49693             [::]:0                 LISTENING       796
  TCP    [::]:49705             [::]:0                 LISTENING       3328
  TCP    [::]:49740             [::]:0                 LISTENING       3320
  TCP    [::1]:53               [::]:0                 LISTENING       3328
  TCP    [fe80::88a3:7388:e822:ac71%4]:53  [::]:0                 LISTENING       3328
```


## 3. Servieces
```
PS C:\Users\Administrator> tasklist /svc

Image Name                     PID Services
========================= ======== ============================================
System Idle Process              0 N/A
System                           4 N/A
Registry                        88 N/A
smss.exe                       416 N/A
csrss.exe                      572 N/A
csrss.exe                      648 N/A
wininit.exe                    676 N/A
winlogon.exe                   720 N/A
services.exe                   796 N/A
lsass.exe                      816 Kdc, KeyIso, Netlogon, NTDS, SamSs
svchost.exe                   1008 PlugPlay
svchost.exe                     60 BrokerInfrastructure, DcomLaunch, Power,
                                   SystemEventsBroker
svchost.exe                    596 RpcEptMapper, RpcSs
svchost.exe                    936 LSM
LogonUI.exe                   1028 N/A
dwm.exe                       1036 N/A
svchost.exe                   1104 TermService
svchost.exe                   1172 NcbService
svchost.exe                   1212 lmhosts
svchost.exe                   1220 EventLog
svchost.exe                   1228 nsi
svchost.exe                   1236 W32Time
svchost.exe                   1296 TimeBrokerSvc
svchost.exe                   1332 Dnscache
svchost.exe                   1340 Dhcp
svchost.exe                   1556 BFE, mpssvc
svchost.exe                   1632 NlaSvc
svchost.exe                   1656 gpsvc
svchost.exe                   1700 ProfSvc
svchost.exe                   1708 Themes
svchost.exe                   1716 EventSystem
svchost.exe                   1796 netprofm
svchost.exe                   1840 SENS
svchost.exe                   1860 Schedule
svchost.exe                   1944 Wcmsvc
svchost.exe                   1980 ShellHWDetection
svchost.exe                   2044 FontCache
svchost.exe                   2132 UserManager
svchost.exe                   2232 UmRdpService
svchost.exe                   2252 LanmanWorkstation
svchost.exe                   2372 CertPropSvc
svchost.exe                   2404 SessionEnv
svchost.exe                   2464 Winmgmt
svchost.exe                   2576 iphlpsvc
svchost.exe                   3004 LanmanServer
fontdrvhost.exe               2188 N/A
fontdrvhost.exe               2904 N/A
spoolsv.exe                   2720 Spooler
svchost.exe                   2292 CoreMessagingRegistrar
svchost.exe                   2008 CryptSvc
svchost.exe                   3096 SysMain
svchost.exe                   3140 WinRM
svchost.exe                   3148 WpnService
ismserv.exe                   3188 IsmServ
MpDefenderCoreService.exe     3228 MDCoreSvc
amazon-ssm-agent.exe          3260 AmazonSSMAgent
Microsoft.ActiveDirectory     3268 ADWS
LiteAgent.exe                 3288 AWSLiteAgent
dfsrs.exe                     3320 DFSR
dns.exe                       3328 DNS
MsMpEng.exe                   3336 WinDefend
dfssvc.exe                    3352 Dfs
wazuh-agent.exe               3492 WazuhSvc
vds.exe                       3756 vds
ssm-agent-worker.exe          4012 N/A
conhost.exe                   4020 N/A
dllhost.exe                   4040 N/A
NisSrv.exe                    4512 WdNisSvc
svchost.exe                   4332 UsoSvc
svchost.exe                   4128 DPS
msdtc.exe                     4296 MSDTC
svchost.exe                   4048 UALSVC
svchost.exe                   1732 CDPSvc
svchost.exe                   4940 DsSvc
svchost.exe                   2240 StorSvc
svchost.exe                   2552 StateRepository
svchost.exe                   1188 WinHttpAutoProxySvc
csrss.exe                     1416 N/A
winlogon.exe                  2916 N/A
fontdrvhost.exe               1248 N/A
dwm.exe                       3364 N/A
rdpclip.exe                   1288 N/A
sihost.exe                    3240 N/A
svchost.exe                   2012 CDPUserSvc_20e4a6
svchost.exe                   3764 WpnUserService_20e4a6
taskhostw.exe                 3368 N/A
svchost.exe                   4172 TokenBroker
svchost.exe                   1468 TabletInputService
ctfmon.exe                    1208 N/A
explorer.exe                  5148 N/A
ShellExperienceHost.exe       5468 N/A
SearchUI.exe                  5556 N/A
RuntimeBroker.exe             5636 N/A
RuntimeBroker.exe             5752 N/A
DefenderSessionHelper.exe     6000 N/A
RuntimeBroker.exe             5320 N/A
smartscreen.exe               3648 N/A
svchost.exe                   5908 LicenseManager
svchost.exe                   3616 WdiSystemHost
dllhost.exe                   3128 N/A
powershell.exe                2640 N/A
conhost.exe                   2104 N/A
tasklist.exe                  4836 N/A
WmiPrvSE.exe                  3160 N/A
```

## 4. Ports classification

Core Active Directory Ports (DO NOT TOUCH)

|Port|Service|Why it exists|
|---|---|---|
|88|Kerberos|Authentication|
|389|LDAP|Directory queries|
|636|LDAPS|Secure LDAP|
|3268|Global Catalog|AD search|
|3269|Secure GC|Secure AD queries|
|464|Kerberos password change|Auth support|
Windows Core Communication 

|Port|Service|
|---|---|
|135|RPC|
|593|RPC over HTTP|
|47001|WinRM service|
|49664–49740|Dynamic RPC ports|
File Sharing / Domain Ops 

|Port|Service|
|---|---|
|445|SMB|
|139|NetBIOS|
Remote access (high risk)

|Port|Service|Risk|
|---|---|---|
|3389|RDP|HIGH|
|5985|WinRM (HTTP)|HIGH|


Attacker exposed ports
- 3389 - RDP
- 5985 - WinRM
- 445 - SMB
- 389 - LDAP (not encrypted)

## 🔹 Open Ports Summary

### ✅ Expected (Do Not Remove)

- 88, 389, 636, 3268, 3269 → Active Directory
- 53 → DNS
- 135, 593, 47001, 496xx → RPC
- 445, 139 → SMB

---

### ⚠️ High-Risk Exposure

- 3389 (RDP) → Open to all interfaces
- 5985 (WinRM) → Remote execution risk
- 445 (SMB) → Attack surface

## 5. Firewall profile

```
PS C:\Users\Administrator> Get-NetFirewallProfile


Name                            : Domain
Enabled                         : True
DefaultInboundAction            : NotConfigured
DefaultOutboundAction           : NotConfigured
AllowInboundRules               : NotConfigured
AllowLocalFirewallRules         : NotConfigured
AllowLocalIPsecRules            : NotConfigured
AllowUserApps                   : NotConfigured
AllowUserPorts                  : NotConfigured
AllowUnicastResponseToMulticast : NotConfigured
NotifyOnListen                  : False
EnableStealthModeForIPsec       : NotConfigured
LogFileName                     : %systemroot%\system32\LogFiles\Firewall\pfirewall.log
LogMaxSizeKilobytes             : 4096
LogAllowed                      : False
LogBlocked                      : False
LogIgnored                      : NotConfigured
DisabledInterfaceAliases        : {NotConfigured}

Name                            : Private
Enabled                         : True
DefaultInboundAction            : NotConfigured
DefaultOutboundAction           : NotConfigured
AllowInboundRules               : NotConfigured
AllowLocalFirewallRules         : NotConfigured
AllowLocalIPsecRules            : NotConfigured
AllowUserApps                   : NotConfigured
AllowUserPorts                  : NotConfigured
AllowUnicastResponseToMulticast : NotConfigured
NotifyOnListen                  : False
EnableStealthModeForIPsec       : NotConfigured
LogFileName                     : %systemroot%\system32\LogFiles\Firewall\pfirewall.log
LogMaxSizeKilobytes             : 4096
LogAllowed                      : False
LogBlocked                      : False
LogIgnored                      : NotConfigured
DisabledInterfaceAliases        : {NotConfigured}

Name                            : Public
Enabled                         : True
DefaultInboundAction            : NotConfigured
DefaultOutboundAction           : NotConfigured
AllowInboundRules               : NotConfigured
AllowLocalFirewallRules         : NotConfigured
AllowLocalIPsecRules            : NotConfigured
AllowUserApps                   : NotConfigured
AllowUserPorts                  : NotConfigured
AllowUnicastResponseToMulticast : NotConfigured
NotifyOnListen                  : False
EnableStealthModeForIPsec       : NotConfigured
LogFileName                     : %systemroot%\system32\LogFiles\Firewall\pfirewall.log
LogMaxSizeKilobytes             : 4096
LogAllowed                      : False
LogBlocked                      : False
LogIgnored                      : NotConfigured
DisabledInterfaceAliases        : {NotConfigured}
```

currently allowed and services depend on firewall rules

```
PS C:\Users\Administrator> Get-NetFirewallRule | Where-Object {$_.Enabled -eq "True"} | Select DisplayName, Direction, Action

DisplayName                                                                  Direction Action
-----------                                                                  --------- ------
Connected User Experiences and Telemetry                                      Outbound  Allow
Delivery Optimization (TCP-In)                                                 Inbound  Allow
Delivery Optimization (UDP-In)                                                 Inbound  Allow
AllJoyn Router (TCP-In)                                                        Inbound  Allow
AllJoyn Router (TCP-Out)                                                      Outbound  Allow
AllJoyn Router (UDP-In)                                                        Inbound  Allow
AllJoyn Router (UDP-Out)                                                      Outbound  Allow
DIAL protocol server (HTTP-In)                                                 Inbound  Allow
DIAL protocol server (HTTP-In)                                                 Inbound  Allow
Windows Device Management Enrollment Service (TCP out)                        Outbound  Allow
Windows Remote Management (HTTP-In)                                            Inbound  Allow
Windows Remote Management (HTTP-In)                                            Inbound  Allow
Remote Desktop - User Mode (TCP-In)                                            Inbound  Allow
Remote Desktop - User Mode (UDP-In)                                            Inbound  Allow
Remote Desktop - Shadow (TCP-In)                                               Inbound  Allow
Cast to Device streaming server (HTTP-Streaming-In)                            Inbound  Allow
Cast to Device streaming server (HTTP-Streaming-In)                            Inbound  Allow
Cast to Device streaming server (HTTP-Streaming-In)                            Inbound  Allow
Cast to Device streaming server (RTCP-Streaming-In)                            Inbound  Allow
Cast to Device streaming server (RTCP-Streaming-In)                            Inbound  Allow
Cast to Device streaming server (RTCP-Streaming-In)                            Inbound  Allow
Cast to Device streaming server (RTP-Streaming-Out)                           Outbound  Allow
Cast to Device streaming server (RTP-Streaming-Out)                           Outbound  Allow
Cast to Device streaming server (RTP-Streaming-Out)                           Outbound  Allow
Cast to Device streaming server (RTSP-Streaming-In)                            Inbound  Allow
Cast to Device streaming server (RTSP-Streaming-In)                            Inbound  Allow
Cast to Device streaming server (RTSP-Streaming-In)                            Inbound  Allow
Cast to Device SSDP Discovery (UDP-In)                                         Inbound  Allow
Cast to Device UPnP Events (TCP-In)                                            Inbound  Allow
Cast to Device functionality (qWave-UDP-In)                                    Inbound  Allow
Cast to Device functionality (qWave-UDP-Out)                                  Outbound  Allow
Cast to Device functionality (qWave-TCP-In)                                    Inbound  Allow
Cast to Device functionality (qWave-TCP-Out)                                  Outbound  Allow
Windows Device Management Certificate Installer (TCP out)                     Outbound  Allow
File and Printer Sharing (NB-Session-In)                                       Inbound  Allow
File and Printer Sharing (NB-Session-Out)                                     Outbound  Allow
File and Printer Sharing (SMB-In)                                              Inbound  Allow
File and Printer Sharing (SMB-Out)                                            Outbound  Allow
File and Printer Sharing (NB-Name-In)                                          Inbound  Allow
File and Printer Sharing (NB-Name-Out)                                        Outbound  Allow
File and Printer Sharing (NB-Datagram-In)                                      Inbound  Allow
File and Printer Sharing (NB-Datagram-Out)                                    Outbound  Allow
File and Printer Sharing (Spooler Service - RPC)                               Inbound  Allow
File and Printer Sharing (Spooler Service - RPC-EPMAP)                         Inbound  Allow
File and Printer Sharing (Echo Request - ICMPv4-In)                            Inbound  Allow
File and Printer Sharing (Echo Request - ICMPv4-Out)                          Outbound  Allow
File and Printer Sharing (Echo Request - ICMPv6-In)                            Inbound  Allow
File and Printer Sharing (Echo Request - ICMPv6-Out)                          Outbound  Allow
File and Printer Sharing (LLMNR-UDP-In)                                        Inbound  Allow
File and Printer Sharing (LLMNR-UDP-Out)                                      Outbound  Allow
Windows Device Management Sync Client (TCP out)                               Outbound  Allow
Core Networking - Destination Unreachable (ICMPv6-In)                          Inbound  Allow
Core Networking - Packet Too Big (ICMPv6-In)                                   Inbound  Allow
Core Networking - Packet Too Big (ICMPv6-Out)                                 Outbound  Allow
Core Networking - Time Exceeded (ICMPv6-In)                                    Inbound  Allow
Core Networking - Time Exceeded (ICMPv6-Out)                                  Outbound  Allow
Core Networking - Parameter Problem (ICMPv6-In)                                Inbound  Allow
Core Networking - Parameter Problem (ICMPv6-Out)                              Outbound  Allow
Core Networking - Neighbor Discovery Solicitation (ICMPv6-In)                  Inbound  Allow
Core Networking - Neighbor Discovery Solicitation (ICMPv6-Out)                Outbound  Allow
Core Networking - Neighbor Discovery Advertisement (ICMPv6-In)                 Inbound  Allow
Core Networking - Neighbor Discovery Advertisement (ICMPv6-Out)               Outbound  Allow
Core Networking - Router Advertisement (ICMPv6-In)                             Inbound  Allow
Core Networking - Router Advertisement (ICMPv6-Out)                           Outbound  Allow
Core Networking - Router Solicitation (ICMPv6-In)                              Inbound  Allow
Core Networking - Router Solicitation (ICMPv6-Out)                            Outbound  Allow
Core Networking - Multicast Listener Query (ICMPv6-In)                         Inbound  Allow
Core Networking - Multicast Listener Query (ICMPv6-Out)                       Outbound  Allow
Core Networking - Multicast Listener Report (ICMPv6-In)                        Inbound  Allow
Core Networking - Multicast Listener Report (ICMPv6-Out)                      Outbound  Allow
Core Networking - Multicast Listener Report v2 (ICMPv6-In)                     Inbound  Allow
Core Networking - Multicast Listener Report v2 (ICMPv6-Out)                   Outbound  Allow
Core Networking - Multicast Listener Done (ICMPv6-In)                          Inbound  Allow
Core Networking - Multicast Listener Done (ICMPv6-Out)                        Outbound  Allow
Core Networking - Destination Unreachable Fragmentation Needed (ICMPv4-In)     Inbound  Allow
Core Networking - Internet Group Management Protocol (IGMP-In)                 Inbound  Allow
Core Networking - Internet Group Management Protocol (IGMP-Out)               Outbound  Allow
Core Networking - Dynamic Host Configuration Protocol (DHCP-In)                Inbound  Allow
Core Networking - Dynamic Host Configuration Protocol (DHCP-Out)              Outbound  Allow
Core Networking - Dynamic Host Configuration Protocol for IPv6(DHCPV6-In)      Inbound  Allow
Core Networking - Dynamic Host Configuration Protocol for IPv6(DHCPV6-Out)    Outbound  Allow
Core Networking - Teredo (UDP-In)                                              Inbound  Allow
Core Networking - Teredo (UDP-Out)                                            Outbound  Allow
Core Networking - IPHTTPS (TCP-In)                                             Inbound  Allow
Core Networking - IPHTTPS (TCP-Out)                                           Outbound  Allow
Core Networking - IPv6 (IPv6-In)                                               Inbound  Allow
Core Networking - IPv6 (IPv6-Out)                                             Outbound  Allow
Core Networking - Group Policy (NP-Out)                                       Outbound  Allow
Core Networking - Group Policy (TCP-Out)                                      Outbound  Allow
Core Networking - DNS (UDP-Out)                                               Outbound  Allow
Core Networking - Group Policy (LSASS-Out)                                    Outbound  Allow
mDNS (UDP-In)                                                                  Inbound  Allow
mDNS (UDP-In)                                                                  Inbound  Allow
mDNS (UDP-In)                                                                  Inbound  Allow
mDNS (UDP-Out)                                                                Outbound  Allow
mDNS (UDP-Out)                                                                Outbound  Allow
mDNS (UDP-Out)                                                                Outbound  Allow
Windows Management Instrumentation (DCOM-In)                                   Inbound  Allow
Windows Management Instrumentation (WMI-In)                                    Inbound  Allow
Windows Management Instrumentation (WMI-Out)                                  Outbound  Allow
Windows Management Instrumentation (ASync-In)                                  Inbound  Allow
Remote Desktop - User Mode (TCP-In)                                            Inbound  Allow
Remote Desktop - User Mode (UDP-In)                                            Inbound  Allow
Remote Desktop - Shadow (TCP-In)                                               Inbound  Allow
Work or school account                                                        Outbound  Allow
Work or school account                                                         Inbound  Allow
Your account                                                                  Outbound  Allow
Your account                                                                   Inbound  Allow
Windows Shell Experience                                                      Outbound  Allow
Cortana                                                                       Outbound  Allow
Cortana                                                                        Inbound  Allow
Network Discovery (Pub WSD-Out)                                               Outbound  Allow
Network Discovery (Pub-WSD-In)                                                 Inbound  Allow
Network Discovery (LLMNR-UDP-Out)                                             Outbound  Allow
Network Discovery (LLMNR-UDP-In)                                               Inbound  Allow
Network Discovery (WSD-Out)                                                   Outbound  Allow
Network Discovery (WSD-In)                                                     Inbound  Allow
Network Discovery (UPnPHost-Out)                                              Outbound  Allow
Network Discovery (SSDP-Out)                                                  Outbound  Allow
Network Discovery (SSDP-In)                                                    Inbound  Allow
Network Discovery (WSD Events-Out)                                            Outbound  Allow
Network Discovery (WSD Events-In)                                              Inbound  Allow
Network Discovery (WSD EventsSecure-Out)                                      Outbound  Allow
Network Discovery (WSD EventsSecure-In)                                        Inbound  Allow
Network Discovery (NB-Datagram-Out)                                           Outbound  Allow
Network Discovery (NB-Datagram-In)                                             Inbound  Allow
Network Discovery (NB-Name-Out)                                               Outbound  Allow
Network Discovery (NB-Name-In)                                                 Inbound  Allow
Network Discovery (UPnP-Out)                                                  Outbound  Allow
Network Discovery (UPnP-In)                                                    Inbound  Allow
Windows Security                                                              Outbound  Allow
Windows Shell Experience                                                      Outbound  Allow
Narrator QuickStart                                                           Outbound  Allow
Windows Defender SmartScreen                                                  Outbound  Allow
Desktop App Web Viewer                                                        Outbound  Allow
Desktop App Web Viewer                                                         Inbound  Allow
Windows Default Lock Screen                                                   Outbound  Allow
Email and accounts                                                            Outbound  Allow
Shell Input Application                                                       Outbound  Allow
Captive Portal Flow                                                           Outbound  Allow
Kerberos Key Distribution Center (TCP-In)                                      Inbound  Allow
Kerberos Key Distribution Center (UDP-In)                                      Inbound  Allow
Kerberos Key Distribution Center - PCR (TCP-In)                                Inbound  Allow
Kerberos Key Distribution Center - PCR (UDP-In)                                Inbound  Allow
File Replication (RPC)                                                         Inbound  Allow
File Replication (RPC-EPMAP)                                                   Inbound  Allow
Active Directory Web Services (TCP-In)                                         Inbound  Allow
Active Directory Web Services (TCP-Out)                                       Outbound  Allow
Active Directory Domain Controller (RPC)                                       Inbound  Allow
Active Directory Domain Controller (RPC-EPMAP)                                 Inbound  Allow
Active Directory Domain Controller - LDAP (TCP-In)                             Inbound  Allow
Active Directory Domain Controller - LDAP (UDP-In)                             Inbound  Allow
Active Directory Domain Controller - Secure LDAP (TCP-In)                      Inbound  Allow
Active Directory Domain Controller - LDAP for Global Catalog (TCP-In)          Inbound  Allow
Active Directory Domain Controller - Secure LDAP for Global Catalog (TCP-In)   Inbound  Allow
Active Directory Domain Controller (TCP-Out)                                  Outbound  Allow
Active Directory Domain Controller (UDP-Out)                                  Outbound  Allow
Active Directory Domain Controller - SAM/LSA (NP-UDP-In)                       Inbound  Allow
Active Directory Domain Controller - SAM/LSA (NP-TCP-In)                       Inbound  Allow
Active Directory Domain Controller - NetBIOS name resolution (UDP-In)          Inbound  Allow
Active Directory Domain Controller - W32Time (NTP-UDP-In)                      Inbound  Allow
Active Directory Domain Controller -  Echo Request (ICMPv4-In)                 Inbound  Allow
Active Directory Domain Controller -  Echo Request (ICMPv4-Out)               Outbound  Allow
Active Directory Domain Controller -  Echo Request (ICMPv6-In)                 Inbound  Allow
Active Directory Domain Controller -  Echo Request (ICMPv6-Out)               Outbound  Allow
DFS Management (TCP-In)                                                        Inbound  Allow
DFS Management (DCOM-In)                                                       Inbound  Allow
DFS Management (WMI-In)                                                        Inbound  Allow
DFS Management (SMB-In)                                                        Inbound  Allow
DFS Replication (RPC-In)                                                       Inbound  Allow
DFS Replication (RPC-EPMAP)                                                    Inbound  Allow
Microsoft Key Distribution Service                                             Inbound  Allow
Microsoft Key Distribution Service                                             Inbound  Allow
RPC Endpoint Mapper (TCP, Incoming)                                            Inbound  Allow
DNS (TCP, Incoming)                                                            Inbound  Allow
DNS (UDP, Incoming)                                                            Inbound  Allow
RPC (TCP, Incoming)                                                            Inbound  Allow
All Outgoing (TCP)                                                            Outbound  Allow
All Outgoing (UDP)                                                            Outbound  Allow
File Server Remote Management (WMI-In)                                         Inbound  Allow
File Server Remote Management (DCOM-In)                                        Inbound  Allow
File Server Remote Management (SMB-In)                                         Inbound  Allow

```

## users
```
PS C:\Users\Administrator> Get-ADUser -Filter * | Select-Object Name, SamAccountName, Enabled

Name          SamAccountName Enabled
----          -------------- -------
Administrator Administrator     True
Guest         Guest            False
krbtgt        krbtgt           False
Server Admin  serveradmin       True
IT Manager    itmanager         True
```

| User          | Status   | Risk                 |
| ------------- | -------- | -------------------- |
| Administrator | Enabled  | HIGH (default creds) |
| serveradmin   | Enabled  | Medium               |
| itmanager     | Enabled  | Medium               |
| Guest         | Disabled | OK                   |
| krbtgt        | Disabled | ⚠️ unusual           |

## 🔹 Critical Risks

### 1. Overexposed Remote Access

- RDP open
- WinRM open

### 2. SMB fully accessible

- No restriction

### 3. Unnecessary services enabled

- Cast to Device
- AllJoyn
- DIAL protocol

### 4. Network discovery leaks

- LLMNR
- NetBIOS
- mDNS

### 5. No outbound control

- All traffic allowed



# Hardinings

## 1.  Overexposed Remote Access
## RDP
- save RDP rule (Allow only my IP)
```
New-NetFirewallRule -DisplayName "ALLOW_RDP_MY_IP" `
-Direction Inbound `
-Protocol TCP `
-LocalPort 3389 `
-RemoteAddress YOUR_IP `
-Action Allow
```
