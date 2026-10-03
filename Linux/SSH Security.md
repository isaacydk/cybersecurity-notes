1. Disabling root login 

Create another user first if there is none within sudo group

`nano  /etc/ssh/sshd_config`
then set this     `PermitRootLogin NO`

2. SSH Key longin

to create the the key

`ssh-keygen -t rsa`  rsa the algorithm

the key will be on ~/.ssh/
you can share the id_rsa to other people to login

then copy the public key to the server

`ssh-copy-id isaac@192.168.122.42`

to disable password login completely 

`nano /etc/ssh/sshd_config`
then set this  `PasswordAuthentication no`



systemctl restart ssh      ---> to restart after change
