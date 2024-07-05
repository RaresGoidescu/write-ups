
from hashlib import sha256

ip_client = "10.0.3.19"
ip_target = "93.184.216.34"

def calculate_sha256(ip_client, ip_target):
    input_string = ip_client + ip_target
    hash_result = sha256(input_string.encode()).hexdigest()
    return hash_result

sha256_sum = calculate_sha256(ip_client, ip_target)
print('CTF{'+sha256_sum+'}')
