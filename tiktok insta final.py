
# coding: utf-8

# In[11]:


followers_gain=0
followers_loss=0
followers_status=[]
o_likes=119.1
o_fans=25.4
f=71640


# In[ ]:


#from time import sleep
from requests import get
from bs4 import BeautifulSoup
import datetime
from IPython.core.display import clear_output
import pandas as pd
import re
from time import sleep
import subprocess
from selenium import webdriver
from bs4 import BeautifulSoup
path1='/home/sohel/Learning/fun projects/chromedriver'
#old_f=71632
old_f=71640
new_f=0
old_like=0
for i in range(1000):
    try:
        old_like=float(t1[40:45])
    except:
        pass
    PATH = 'https://m.tiktok.com/h5/share/usr/6585075929662799877.html'
    http = get(f'{PATH}')
    bsoup = BeautifulSoup(http.text, 'html.parser')
    ss=bsoup.findAll({"meta": "content"})
    t1=str(ss[9])
    likes=float(t1[40:45])
    fans=float(t1[15:19])
    if(old_like!=likes):
        #subprocess.call(['spd-say', "preksha's Tiktok total likes"])
        sleep(2)
        #subprocess.call(['spd-say', str(likes)])
        sleep(2)
        #subprocess.call(['spd-say', "preksha's Tiktok total fans"])
        sleep(2)
        #subprocess.call(['spd-say', str(fans)])
    
    print("Total likes: %s"%t1[40:46])
    print("total fans: %s"%t1[15:20])
    likes_gain=(likes-o_likes)*1000
    fans_gain=(fans-o_fans)*1000
    print("New likes today %d"% likes_gain)
    print("New fans today %d"% fans_gain)
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(path1, options=options)
    url ='https://www.instagram.com/preksha_rana_official/'
    driver.get(url)
    page = driver.execute_script('return document.body.innerHTML')
    soup = BeautifulSoup(''.join(page), 'html.parser')
    soup.find_all("span", class_="g47SY")
    s=str(soup.find_all("span", class_="g47SY")[1])
    c=s[27:33]
    if(new_f is not 0):
        old_f=new_f
    new_f=int(int(c[:2]+c[3:]))
    print("Total instagram followers: %s "%c)
    if(old_f!=new_f):
        #subprocess.call(['spd-say', "preksha's instagram total followers"])
        sleep(2)
        #subprocess.call(['spd-say', c])
        sleep(2)
        change=new_f-old_f
        followers_status.append(change)
        print("Followers Change: %d"%change)
        if(change>0):
            followers_gain=followers_gain+change
        else:
            followers_loss=followers_loss+(-change)
            
            
        sleep(2)
        #subprocess.call(['spd-say', str(change)])
        sleep(1)
        #subprocess.call(['spd-say', "new followers"])
        sleep(1.5)
        gain=new_f-f
        print("Total folloers gain today %d"% gain)
        #subprocess.call(['spd-say', "Total folloers gain today"])
        sleep(2)
        
        #subprocess.call(['spd-say', str(gain)])

    print("followers Loss today: %d"%followers_loss)
    print("followers gain today: %d"%followers_gain)
    sleep(60)
    clear_output(wait=True)
    
    


# In[ ]:


Yesterday 24-02-2018
-----------------------
Total likes: 119.1k
total fans: 25.4k
New likes today 4099
New fans today 1399
Total instagram followers: 71,635

