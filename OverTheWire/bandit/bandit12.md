login: ssh -p 2220 bandit12@bandit.labs.overthewire.org
pwd: JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv

```
mkdir /tmp/patryk
cd /tmp/patryk
cp ~/data.txt .
xxd -r data.txt comp
file comp
mv comp comp.gz
file comp
bunzip2 comp
file comp.out
mv comp.out comp.gz
file comp
tar -xf comp
file data5.bin
tar -xf data5.bin
file data6.bin
bunzip2 data6.bin
file data6.bin.out
tar -xf data6.bin.out
file data8.bin
mv data8.bin data8.gz
gunzip data8.gz
file data8
cat data8
```

flag: wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw

[[xxd]]
[[bzip2]]
[[file]]
[[tar]]
[[gzip]]
