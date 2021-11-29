import requests
import hashlib
import json

# The tolerable number of times the password was leaked
# Set 0 (zero) for maximum security
security_treshold = 0

# Checks whether the input password was already compromised
# Returns number of compromises
# Only part of the hash is transmitted, not the password itself
def is_pwned(password):
    m = hashlib.sha1()
    m.update(password.encode())
    hashed = m.hexdigest()

    try:
        response = requests.request('GET', "https://api.pwnedpasswords.com/range/" + hashed[:5], stream=False)
    except requests.ConnectionError:
        return -1

    if response.status_code != 200:
        return -1

    line = response.iter_lines()

    pwned_times = 0
    for line in response.iter_lines():
        if line.decode().split(":")[0] == hashed[5:].upper():
            pwned_times = int(line.decode().split(":")[1])
            break
    return pwned_times

# Checks whether the password length is long enough
def is_long(password):
    if len(password) < 8:
            return False
    return True

# A simple sign_up procedure which checks the password security
# Returns True on success
def sign_up(username="", password=""):
    if username == "":
        username = input("Enter username: ").strip('\n')
    if password == "":
        password = input("Enter password: ").strip('\n')

    while not is_long(password):
        password = input("Password too short! Try again.\nEnter password: ").strip('\n')

    pwned_times = is_pwned(password)
    if pwned_times == -1:
        print("The service is unavailiable at the moment"
                + ", so we can't check the password. Try again later")
        return False

    while pwned_times > security_treshold:
        print("This password was already compromised "
                + str(pwned_times)
                + " times. See https://haveibeenpwned.com/ for more info.")
        password = input("Try another one!\nEnter password: ").strip('\n')
        pwned_times = is_pwned(password)

    print("Great! Signed up as " + username)
    return True

if __name__ == "__main__":
    sign_up()
        

