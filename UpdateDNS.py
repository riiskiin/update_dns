import requests
import certifi
from requests import get
import xmltodict

domain = "imparare.com"
APIKEY="b1f234kb5748234a9d17f7b2c76f4"  #4 Namecheap DDNS Token (Accounts > Domain List > Advanced DNS)

def getIP():
    ip = get('https://api.ipify.org').content.decode('utf8')
    return ip

def updateRecord(ip):
    global domain
    global APIKEY
    host = "@"
    return requests.get("https://dynamicdns.park-your-domain.com/update?host=" + host + "&domain=" + domain + "&password=" + APIKEY + "&ip=" + ip, verify=certifi.where())

ip = getIP()
print("External IP: " + ip)
r = updateRecord(ip)
errCount = r.content.decode('utf8')
obj = xmltodict.parse(errCount)
ErrCount = obj["interface-response"]["ErrCount"]

if ErrCount == '1':
    print ("Failed to update DNS err: ", obj["interface-response"]["errors"])
else:
    print ("Successful updated DNS to", ip)
