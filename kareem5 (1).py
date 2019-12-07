import requests
url = "https://www.ipinfo.io/"
res =requests.get(url)
print(res.text)
