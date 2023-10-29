import requests
from bs4 import BeautifulSoup

url = 'https://omsk.drom.ru/auto/'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
print(page.status_code)

mod = soup.find_all('div', class_='css-1wgtb37')
par = soup.find_all('div', class_='css-1fe6w6s')
price = soup.find_all('div', class_='css-1dv8s3l')

with open('parser.txt', 'w', encoding='utf-8') as f:
    for i in range(0, len(mod)):
        f.write(mod[i].text + '\n')
        f.write(par[i].text + '\n')
        f.write(price[i].text + '\n')
        f.write('\n')
