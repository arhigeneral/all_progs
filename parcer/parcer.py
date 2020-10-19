import requests
from bs4 import BeautifulSoup as BS

#word = input("Введите желаемый запрос - ")
def articles(word):

    r = requests.get('https://habr.com/ru/search/?q=' + word + '#h')
    html = BS(r.content, 'html.parser')

    info = str(html.select('.post__title > a'))

    i = 0
    marker = info[29:34]
    stats_list = []
    article = ""
    while len(info) > 30:
        i += 1
        if info[i:i+5] == marker:
            i += 6
            while info[i] != ">":
                article += info[i]
                i += 1
            stats_list.append(article[0:len(article) - 1])
            article = ""
            i += 150
        if i >= len(info):
            break

    return stats_list
