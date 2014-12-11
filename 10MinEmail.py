from bs4 import BeautifulSoup
import threading
import urllib


web=urllib.urlopen('http://www.my10minutemail.com/')
print '\n'
soup=BeautifulSoup(web)
print soup.p.string
print 'Email Valid For 10 minutes\n'

t = threading.Timer(5.0, alarm)
t.start() 

def alarm():
    print 'One Minute is Left\n'
    print 'Need More Time, Extend by 10 Minutes'
    print 'Enter Y for yes or N for Exit'
    ExVar=raw_input()
    proceed='y' or 'Y'
    Exit='n' or 'N'
    if ExVar==proceed:
    #    urllib.urlopen('http://www.my10minutemail.com/Extend')
     #   print soup.h1.span
    else: exit()

raw_input()


    




