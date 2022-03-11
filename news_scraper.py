from bs4 import BeautifulSoup
import requests


class NewsScraper:

    def __init__(self):
        pass

    @staticmethod
    def get_headlines():

        nbc_business = "https://www.coindesk.com"
        res = requests.get(nbc_business)
        soup = BeautifulSoup(res.content, 'html.parser')

        headlines = soup.find_all(attrs={'class': 'headline'})

        articles = []
        for i in headlines:
            headline = i.text
            link = nbc_business + i['href']
            info = [headline, link]
            articles.append(info)
        return articles

    @staticmethod
    def get_reuters():
        url = "https://www.reuters.com/news/archive/economicNews"
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'html.parser')

        links = soup.select('a')
        articles = []
        for i in links:
            try:
                if i['href'].startswith("/article") and not i.text.strip() == '':
                    headline = i.text.strip()
                    link = url+i['href']
                    articles.append([headline, link])
            except:
                continue

        return articles

    @staticmethod
    def get_specific(category):
        url = f"https://cryptonews.com/news/{category}-news/"
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'html.parser')

        links = soup.select('a')
        articles = []
        for i in links:
            try:
                if i['class'][0] == 'article__title':
                    headline = i.text.strip()
                    link = url + i['href']
                    articles.append([headline, link])

            except:
                continue
        return articles


#print(NewsScraper.get_nyt())

