import requests
from bs4 import BeautifulSoup

requestment = requests.get(url='/{{config.items.__class__.__mro__[1].__subclasses__()}}').text
soup = BeautifulSoup(requestment, 'html.parser')
soup_findstr = soup.find('str').text.strip('[]').split(',')
counter = 0
for elementos in soup_findstr:
    print(counter, elementos)
    counter += 1
