import requests
import json

uname=input('enter username to find email from GitHub:')

strSource = requests.get("https://api.github.com/users/"+uname+"/events/public")
strSource = json.loads(strSource.text)

print("\nemails:")

for i in strSource:
    try:
        a=i["payload"]["commits"][0]["author"]["email"]
        print(a)
    except Exception:
        continue