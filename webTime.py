#! /usr/bin/python3
#https://24timezones.com/time-zone/ist
#<div class="time"><span>3</span><span>36</span><span>21</span><sup>PM</sup></div><p>Sunday, February 3, 2019</p>
#//*[@id="cityClock"]
#<span class="hours">8</span><span class="minutes">52</span><span class="seconds">18</span><sup>am</sup>
from bs4 import BeautifulSoup 
import requests
import re
url = 'https://24timezones.com/time-zone/ist'
while True:
    page = requests.get(url)
    data = page.text
    soup = BeautifulSoup(data, 'lxml')
    soup = str((soup.find(id = 'cityClock')))
    hours = re.search('<span class=\"hours\">(.+?)</span>',soup).group(1)
    minutes = re.search('<span class=\"minutes\">(.+?)</span>',soup).group(1)
    sec = re.search('<span class=\"seconds\">(.+?)</span>',soup).group(1)
    am_pm = re.search('<sup>(.+?)</sup',soup).group(1)

#    time = soup.get_text()
#    time = time.split()
    print(("{}:{}:{}{}").format(hours,minutes,sec,am_pm))
'''
#print ((soup.find()))

date = re.search('<p>(.+?)</p>',soup)
if date:
    date = date.group(1)

print (date)
'''
