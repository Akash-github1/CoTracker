#Importing modules
from re import findall
import pyfiglet
import requests, random, sys, os, time
from bs4 import BeautifulSoup
from pyfiglet import *
from termcolor import colored
import matplotlib.pyplot as py

#colors and shit like it
if sys.platform == 'win32':
    white  = '\033[0m'
    red    = '\033[31;1m'
    green  = '\033[32;1m'
    yellow = '\033[33;1m'
    blue   = '\033[34;1m'
    pink   = '\033[35;1m'
    cyan   = '\033[36;1m'
    r = (white, red, green, yellow, blue, pink, cyan)
    z = random.choice(r)
elif sys.platform == 'linux' or sys.platform == 'linux2':
    white  = '\033[0m'
    red    = '\033[31;1m'
    green  = '\033[32;1m'
    yellow = '\033[33;1m'
    blue   = '\033[34;1m'
    pink   = '\033[35;1m'
    cyan   = '\033[36;1m'
    r = (white, red, green, yellow, blue, pink, cyan)
    z = random.choice(r)

try:
    import re , bs4,matplotlib,pyfiglet,termcolor
except ImportError:
    print(red+'\n['+white+'!'+red+'] '+green+'module '+white+'re or bs4'+green+'not installed'+white+'\n')
    sys.exit()
os.system('cls')

print (red+"\n<------------------------------------------------------------------->")
print (red+"\n<------------------------------------------------------------------->")
fig = pyfiglet.figlet_format('         Co-Tracker',font='standard')
banner = colored(fig,'yellow')
print(banner,end='')
print (green+"\n<-------------------------COVID-19-Tracker-------------------------->")
print (green+"\n<------------------------------------------------------------------->")
print()

print(yellow+'['+white+'*'+yellow+']'+ pink + ' Press ctrl + z to exit.')
print(yellow+'['+white+'*'+yellow+']'+ pink + " Don't forget to captalized the first letter.")
print(yellow+'['+white+'*'+yellow+']'+ pink + ' List of cases may vary.')
print()

for _ in range(0,50):    
    try:
        country = input(red+'['+white+'!'+red+'] '+cyan+'Country Name'+green+': '+white)
    except NameError:
        print(red+"\n["+white+"*"+red+"] "+green+"use "+white+"python2.7\n")
    print(red+'['+white+'*'+red+'] '+cyan+'Fetching Details'+white+'.../'+white)
    print()


    def getdata(url):
        rq = requests.get(url)
        return rq.text

    if __name__ == '__main__':
        data = getdata('https://www.worldometers.info/coronavirus/?fbclid=IwAR35ZFiRZJ8tyBCwazX2N-k7yJjZOLDQiZSA_MsJAfdK74s8f2a_Dgx4iVk')

        soup = BeautifulSoup(data,'html.parser')

        datastr = ''
        for tr in soup.find_all('tbody')[3].find_all('tr'):
            datastr += tr.get_text()
        datastr = datastr[752:]
        # print(datastr)
        datalist=datastr.split('\n\n')

        for item in datalist[0:]:
            co_data = item.split('\n')
            
            # print(co_data)
            if country in co_data:
                try:
                    print (green +"["+white+"1"+red +"] "+z+"Country                 "+blue+"|    " +yellow+country,end='\n\n')
                    print (green +"["+white+"2"+red +"] "+z+"Total cases             "+blue+"|    " +yellow+co_data[2],end='\n\n')
                    print (green +"["+white+"3"+red +"] "+z+"New Cases               "+blue+"|    " +yellow+co_data[3],end='\n\n')
                    print (green +"["+white+"4"+red +"] "+z+"Total Deaths            "+blue+"|    " +yellow+co_data[4],end='\n\n')
                    print (green +"["+white+"5"+red +"] "+z+"New Deaths              "+blue+"|    " +yellow+co_data[5],end='\n\n')
                    print (green +"["+white+"6"+red +"] "+z+"Recovered Deaths        "+blue+"|    " +yellow+co_data[6],end='\n\n')
                    print (green +"["+white+"7"+red +"] "+z+"Active Cases            "+blue+"|    " +yellow+co_data[7],end='\n\n'+white)
                except:
                    print()
                break

    print('<-------------------------'+green+"Fetching Completed "+green+'----------------------->')
