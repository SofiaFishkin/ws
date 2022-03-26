import requests
from bs4 import BeautifulSoup
from pprint import pprint
KEYWORDS = {'дизайн', 'фото', 'web', 'python'}
response = requests.get('https://habr.com/ru/all/')
soup = BeautifulSoup(response.text, features = 'html.parser')
articles = soup.find_all('article')
for article in articles:
    date = article.find('datetime', class_ = 'tm-article-snippet__datetime-published')
    header = article.find('h2', class_ = "tm-article-snippet__title tm-article-snippet__title_h2")
    hubs = article.find_all('span', class_ = 'tm-article-snippet__hubs-item')
    hubs = set([hub.text for hub in hubs])
    title = article.find('a', class_='post__title_link')
    link = header.text.find('a')
    if KEYWORDS & hubs:
         print('<{}>-<{}>-<{}>'.format(date.text, title.text, link.text))