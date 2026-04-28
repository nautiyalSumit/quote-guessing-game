# https://quotes.toscrape.com
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://quotes.toscrape.com"

def scrape_quotes():
    all_quotes=[]
    url = "/page/1"
    while url:
        res = requests.get(f"{BASE_URL}{url}")
        soup = BeautifulSoup(res.text,"html.parser")
        quotes = soup.find_all(class_="quote")
        for quote in quotes:
            all_quotes.append({
                "text":quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link":quote.find("a")['href']
            })
        nxt_btn = soup.find(class_="next")
        url = nxt_btn.find("a")["href"] if nxt_btn else None
    return all_quotes