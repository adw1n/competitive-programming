import urllib.parse
import requests
shattered1=requests.get("https://shattered.io/static/shattered-1.pdf")
shattered2=requests.get("https://shattered.io/static/shattered-2.pdf")
#only first 1k bytes from each string, because apache had a limit of max 8k bytes URI
response=requests.get("http://54.202.82.13?%s"%urllib.parse.urlencode({"name":shattered1.content[:1000],"password":shattered2.content[:1000]}))
print(response.status_code)
print(response.content)
