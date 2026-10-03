`sudo adduser username`    (better)OR
`sudo useradd -m -s /bin/bash username`  -m - to create home dir.  -s -to specifiy shell

`sudo passwd username`    -to set password to a user
`su username`    to switch user

`list of the user - /etc/passwd`
`Hashed password storage - /etc/shadow`

**usermod**

`sudo usermod -aG groupname username`     --  to append the user to the group without removig from the existing group  or
`$sudo visudo   ----->then by adding------->  username ALL=(ALL:ALL) ALL`

**Change the default shell:** `sudo usermod -s /bin/bash username`

**Change the home directory:** `sudo usermod -d /new/path -m username`

**Lock an account:** `sudo usermod -L username`

**Enable Login**: `sudo usermod -U username`

**Side quest** -for secure copy
`scp linux_audit_day1.py user@<ubuntu-ip>:/home/user/`



