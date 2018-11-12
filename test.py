import time
import requests
import hashlib
import urllib
import json
url = "https://api.ix.com/balance/list"
nonce = time.time()
payload = {'nonce':nonce,'symbol':'BTC_USDT','page':1,'size':100}
payload_str = urllib.parse.urlencode(payload)
secret = "990f0190cf293292a60d29ddb5e5f6d90e81021c24556e8158f82c6d2522c0bc"
sign = str(hash(hashlib.sha256((secret+payload_str).encode("utf-8"))))
headers = { 'version':'2.0',
           'key':'ef28560afa62c3f0f8dd2c80a171aa78',
           'sign':sign,
          }
r = requests.post(url,data=payload,headers=headers)
print(r.text)