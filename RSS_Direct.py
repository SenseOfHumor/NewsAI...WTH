import xmltodict
import requests
import json
import random

def getRSS(url: str) -> dict:
    response = requests.get(url)
    return xmltodict.parse(response.content)

data = getRSS("https://feeds.bbci.co.uk/news/technology/rss.xml")

# Get the list of news articles
items = data['rss']['channel']['item']

# Randomly select a news article
item = random.choice(items)

# print(item['title'])
# print(item['description'])
# print(item['link'])
# print(item['media:thumbnail']['@url'])

def getTitle():
    return item['title']

def getDescription():
    return item['description']

def getURL():
    return item['link']

def getImage():
    return item['media:thumbnail']['@url']