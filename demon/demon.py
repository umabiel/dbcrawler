import json
import urllib2

url = 'http://api.peoplecall.com/portables/v1/phonenumbers/public/628774744'
r = urllib2.urlopen(url)
data = json.loads(r.read().decode(r.info().getparam('charset') or 'utf-8'))
print data["currentOperator"]
print data