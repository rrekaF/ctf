login: ssh -p 2220 bandit5@bandit.labs.overthewire.org
pwd: lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR

```
find -size 1033c
cat ./inhere/maybehere07/.file2
```

there was only 1 file that matched "1033 bytes in size" but if there were multiple i could use `file ./inhere/maybehere07/.file2` to check if it is human-readable (ASCII text) and `ls -l ./inhere/maybehere07/.file2` to check if it is executable

flag: P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU
[[find]]