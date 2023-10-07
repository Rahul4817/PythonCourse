import requests

response = requests.get("https://google.com")
html = response.text
print(html)
