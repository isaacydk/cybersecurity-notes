ps          List processes
ps aux   List processes for all users
top         most resource using process

**Manageing Processes**
nice  - setting priority
- to increace -1 upto -20   eg     nice -n -10 /bin/slowprocess
- to decrease 1 upto 19    eg      nice -n  10 /bin/slowprocess
- 0 default

renice - also for setting priority
- takes value form -20 to 19 and the process PID number
- eg  renice 19 3432

another way to change priority by Top ---> press R 

**killing processes**
kill -n PID
-n 
- -1 hangup)(HUP) signal . it stops it and resurt it with the same pid
- -2 Inerrupt(INT) it  may not work
- -3  core dump , teminate and save the process info in memory
- -15 Terminator default
- -9 Absolute kill
eg kill -9 2114

**Running process in the background**
somecommand &
fg  PID     to move the process that running backgroud to the foreground

**Scheduling process**
at 7:20pm
at 7:20pm June 25
at noon
at tomorrow
at now + 20 minutes
at 7:20pm 02/22/2026

then
at > /root/myscanningscript


