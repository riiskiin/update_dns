import requests
import io, json
import certifi
from xml.etree import ElementTree

domain = "moldavian.xyz"
APIKEY="25153307711d47d88147573e6c66f87a"  # Namecheap DDNS Token (Accounts > Domain List > Advanced DNS)

def getIP():
	r = requests.get("https://ifconfig.co/json", verify=certifi.where()).json()
	return r['ip']

def updateRecord(ip):
    global domain
    global APIKEY
    host = "@"
    return requests.get("https://dynamicdns.park-your-domain.com/update?host=" + host + "&domain=" + domain + "&password=" + APIKEY + "&ip=" + ip, verify=certifi.where())

ip = getIP()
print("External IP: " + ip)
r = updateRecord(ip)
errCount = ElementTree.fromstring(r.content).find("ErrCount").text
if int(errCount) > 0:
	print("API error\n" + str(r.content))
else:
	print("Updete IP success!")