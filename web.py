from cgitb import text
from pyexpat import features
import bs4
import requests

web = 'https://habr.com/ru/all/' 
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language': 'ru,en;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': '_ym_d=1628840683; _ym_uid=1628840683355101683; _ga=GA1.2.137596937.1628841988; fl=ru; hl=ru; feature_streaming_comments=true; _gid=GA1.2.1021543475.1641571984; habr_web_home=ARTICLES_LIST_ALL; _ym_isad=1; visited_articles=599735:203282; SLG_GWPT_Show_Hide_tmp=1; SLG_wptGlobTipTmp=1',
'Host': 'habr.com',
'Referer': 'https://github.com/netology-code/py-homeworks-advanced/tree/master/6.Web-scrapping',
'sec-ch-ua': '"Chromium";v="94", "Yandex";v="21", ";Not A Brand";v="99"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests':'1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.4.727 Yowser/2.5 Safari/537.36'}

response = requests.get(web, headers = HEADERS)
response.raise_for_status()
text = response.text


soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    hubs = article.find_all(class_='tm-articles-list')
    hubs = set(hub.text.strip() for hub in hubs)
    for hub in hubs:
        if hub in KEYWORDS:
            href = article.fild(class_='tm-article-snippet__title-link').attrs['href']
            url = (web + href)
            title = article.fild('h2').fild('span').text
            result =f'Статья {title} - {url}'
            print(result)










