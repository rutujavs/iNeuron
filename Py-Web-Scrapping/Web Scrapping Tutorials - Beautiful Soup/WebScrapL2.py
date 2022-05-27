import requests
from bs4 import BeautifulSoup

url = 'https://www.indiatoday.in/'

res = requests.get(url).content

soup = BeautifulSoup(res,'lxml')
# print(soup.prettify())

# aTag = soup.find_all('a')
# print(aTag)

# for link in aTag:
#     # print(link.text)
#     print(link.get('href'))


# for h3Tag in soup.find_all('h3'):
#     print(h3Tag.a.get('href'))


for h3Tag in soup.find_all('h3'):
    for aTag in h3Tag.find_all('a'):
        print(url+aTag.get('href'))