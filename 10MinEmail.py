from bs4 import BeautifulSoup
import threading
import urllib
web=urllib.urlopen('http://www.my10minutemail.com/')
soup=BeautifulSoup(web)
print soup.p.string
print 'Email Valid For 10 minutes'
raw_input()
#def alarm():
#    print 'One Minute is Left'
#t = threading.Timer(60.0, alarm)
#t.start() 

