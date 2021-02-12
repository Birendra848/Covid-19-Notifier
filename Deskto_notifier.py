import requests
from bs4 import BeautifulSoup as bs
from plyer import notification as nf
import time

result= requests.get('https://www.mohfw.gov.in/').text
soup= bs(result,'html.parser')
soup.encode('utf-8')
total_cases= soup.find('li',{'class':'bg-blue'}).get_text().strip()
print(total_cases)

def notifyme(notify_title,cases):
    nf.notify(title= notify_title,
              message = cases,
              app_icon= "C:\\Users\\virus\\Documents\\Desktop_Notifier\\virus.ico",
              timeout = 5)

while True:
    notifyme("Total Cases of corona : ",total_cases)
    time.sleep(60*60)