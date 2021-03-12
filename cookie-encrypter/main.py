from bs4 import BeautifulSoup
import requests, hashlib

first_request = requests.get(url=' ')
soup = BeautifulSoup(first_request.text, 'html.parser').find('h3').text
second_request = requests.post(url=' ', data={'hash': {hashlib.md5(soup.encode('utf-8')).hexdigest()}}, cookies=first_request.cookies.get_dict())
print(second_request.content)
