import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com'

# res = requests.get(url)
# print(res.status_code)

res = requests.get(url).content

# soup = BeautifulSoup(res,'html.parser')
soup = BeautifulSoup(res,'lxml')

# print(soup.prettify())
# print(soup.a)
# print(soup.a.text)
# print(soup.p.text)
# print(soup.footer)
print(soup.script)

