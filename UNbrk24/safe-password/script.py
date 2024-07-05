import requests
import hashlib

def check_password(password):
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]
    response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
    if response.status_code == 200:
        for line in response.text.splitlines():
            suffix_from_api, count = line.split(":")
            if suffix_from_api == suffix:
                return int(count)
    return 0

# Example usage
file_path = "/home/cybi/Downloads/leaked.txt"
with open(file_path, "r") as f:
    passwords = f.readlines()
    for password in passwords:
        password = password.replace('\r','')
        password = password.replace('\n','')
        password = password.replace('\t','')
        count = check_password(password[:-1])
        hashed = sha256(password);
        if count != 0:
            print(f"The password '{password}' has been pwned {count} times.\n\t{hashed}")

