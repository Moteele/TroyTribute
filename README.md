# TroyTribute
A simple tool to check users password against leaked ones.

Users are usually the weakest link of the security chain. If they are given the option of using passwords, they will use the same one over and over. And many of those leaked passwords are availiable publicly on the Internet. The attacker then simply tries the users password on plenty of other services and very often, he is succesful!

To prevent users from using an already leaked and compromised password, this tool checks the provided password against a public database of leaks. If it finds out that the given password was ever used and leaked (even by other user), it prompts the user to give another. This not only prevents the usage of compromised passwords, it also prevents the users from using weak passwords, as those were most probably already used and leaked.

The password is not transmitted through the Internet in plaintext. It is hashed by SHA1 and only the first 5 letters are sent to the [have i been pwned?](https://haveibeenpwned.com/) API.

Usage:
```
python src/troytribute.py
```
And provide the required credentials.

