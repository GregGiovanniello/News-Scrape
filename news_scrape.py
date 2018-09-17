"""
program: news_scrape.py
author: greg

uses the beautiful soup web scraper to pull rss data from a news feed url.
"""
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

news_url = "http://rss.cnn.com/rss/cnn_health.rss"
Client = urlopen(news_url)
xml_page = Client.read()
Client.close()

soup_page = soup(xml_page, "xml")
news_list = soup_page.findAll("item")

for news in news_list:
	print(news.title.text)
	print(news.link.text)
	print(news.pubDate.text)
	print("-" * 60)