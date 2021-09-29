from bs4 import BeautifulSoup as bs4
import requests
url = 'https://was.livere.me/comment/moneytoday?id=moneytoday&refer=star.mt.co.kr%2Fstview.php%3Fno%3D2021080714155164315&uid=MTI2Ni80MzkwNi8yMDQ0Mg%3D%3D&site=https%3A%2F%2Fstar.mt.co.kr%2Fstview.php%3Fno%3D2021080714155164315&title=%252527146%2525uAD6C%252520%2525uD22C%2525uD63C%252527%25252027%2525uC138%252520%2525uC870%2525uC0C1%2525uC6B0%252520%2525uC2DC%2525uC98C%252520%2525uB4A4%252520%2525uC785%2525uB300%25253F%252520%2525uD0A4%2525uC6C0%252520%252522%2525uC0C1%2525uC758%2525uD574%2525uBD10%2525uC57C%252520%2525uD55C%2525uB2E4%252522-%252520%2525uC2A4%2525uD0C0%2525uB274%2525uC2A4&titleLength=46&logo=https%3A%2F%2Fthumb.mtstarnews.com%2F21%2F2021%2F08%2F2021080714155164315_1.jpg%2Fdims%2Fresize%2F1200%2Fcrop%2F1200x630!%2Foptimize%2F&uuid=39dd17a5-d9e6-47f3-8e1c-df23d20ca81f'
res = requests.get(url)
soup = bs4(res.content, 'html.parser')
print(soup.select('.reply-content'))
print(soup)
