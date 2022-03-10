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

        headlines = soup.find_all(attrs={'class':'headline'})

        articles = []
        for i in headlines:
            headline = i.text
            link = nbc_business + i['href']
            info = [headline, link]
            articles.append(info)
        return articles

