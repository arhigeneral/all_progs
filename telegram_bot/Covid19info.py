import requests
from bs4 import BeautifulSoup as BS

# r = requests.get('https://pikabu.ru/best')
# html = BS(r.content,'html.parser')
#
#
#
# for el in html.select('.story__main'):
#     title = el.select('.story__title > a')
#     print(title)
s = requests.Session()

auth_html = s.get('https://pikabu.ru/')
auth_bs = BS(auth_html.content, 'html-parser')
csrf = auth_bs.select('input[name=x-csrf-token]')[0]['value']

payload = {
    'x-csrf-token': csrf,
    'username': 'sad_casd@mail.ru',
    'password': '159753258sava'
}
