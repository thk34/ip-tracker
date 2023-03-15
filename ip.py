import sys
import json
import requests

api = "http://ip-api.com/json/"

ip = sys.argv[1]
res = requests.get(api + ip).text
js = json.loads(res)
if js['status'] == "success":
  print("""
------- Ip Track -------
Ip: """ + js['query'] + """
Country: """ + js['country'] + """
Region: """ + js['regionName'] + """
City: """ + js['city'] + """
Zip: """ + js['zip'] + """
Timezone: """ + js['timezone'] + """
Isp: """ + js['isp'] + """
Org: """ + js['org'] + """
As: """ + js['as'] + """
------------------------
  """)

else:
  print('[-] Invalid ip address!')
