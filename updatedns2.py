import requests
import io, json
import certifi
from requests import get
from xml.etree import ElementTree

domain = "imparare.click"
APIKEY="b1fb53276b5748a9bea9d17f7b2c76f4"  # Namecheap DDNS Token (Accounts > Domain List > Advanced DNS)

def getIP():
    ip = get('https://api.ipify.org').content.decode('utf8')
    #print('My public IP address is: {}'.format(ip))
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
#print (errCount)
if "<ErrCount>0</ErrCount>" in errCount:
    print ("IP Updated Successful")
else:
    print ("Error Updating IP")
    print (str(errCount))
#errCount = ElementTree.fromstring(r.content).find("ErrCount").text
errCount = 1
#if int(errCount) > 0:
#	print("API error\n" + str(r.content))
#else:
#    print("Updete IP success!")
#    print("r content: \n" + str(r.content))
