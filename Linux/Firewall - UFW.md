
default ufw configuration file /etc/default/ufw

sudo systemctl status ufw

sudo systemctl disable ufw  or
sudo ufw disable

sudo ufw reset     --recommended to start form zero

**default configuration for incoming and outgoing**

```
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

**allowing and denying connections**

sudo ufw allow ssh      sudo ufw allow http  /80
sudo ufw allow 22        sudo ufw allow https  /443

sudo ufw allow from 10.0.0.1
sudo ufw alllow from 10.0.0.1/24 to any port 22   --only ssh connection is allowed from this ip address

sudo ufw deny ssh

**deleting rules**

sudo ufw delete  5
to know the numbers -->  sudo ufw status numbered

**reset rules**
sudo ufw reset


