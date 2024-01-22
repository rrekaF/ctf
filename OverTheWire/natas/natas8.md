link: http://natas8.natas.labs.overthewire.org/
login: natas8
pwd: a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB

*steps:*
- check source code
```php
$secret = "3d3d516343746d4d6d6c315669563362";

function decodeSecret($secret) {
    // return bin2hex(strrev(base64_encode($secret)));
    return base64_decode(strrev(hex2bin($secret)));
}
print decodeSecret($secret);
```
- secret = oubWYf2kBq

flag: Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd