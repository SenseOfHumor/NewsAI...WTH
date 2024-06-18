import streamlit as st
import requests, json
import time
import google.generativeai as genai
from dotenv import load_dotenv
import os
import base64
import xmltodict
import random

################################################################################################


#Fetching the RSS news feed
def getRSS(url: str) -> dict:
    response = requests.get(url)
    return xmltodict.parse(response.content)
data = getRSS("https://feeds.bbci.co.uk/news/technology/rss.xml")
# Get the list of news articles
items = data['rss']['channel']['item']
# Randomly select a news article
item = random.choice(items)
#News functions
def getTitle():
    return item['title']
def getDescription():
    return item['description']
def getURL():
    return item['link']
def getImage():
    return item['media:thumbnail']['@url']

################################################################################################

#Card UI
def card():  ## inspired by https://github.com/gamcoh/st-card
    data = newsImage
    from streamlit_card import card
    card = card(
        title=newsTitle,
        text=newsDescription,
        image=data,
        styles={
            "card": {
                "width": "100%", # <- make the card use the width of its container, note that it will not resize the height of the card automatically
                "height": "300px", # <- if you want to set the card height to 300px
                "filter": "brightness(100%)"
            }
        }
    )


################################################################################################


#Streamlit UI
st.title("MindFeed")
st.write("Treat your mind to the latest news articles.")
st.write("_" * 50)



if st.button("show card"):  # function call to test the functionality of the card
    newsTitle = getTitle()
    newsDescription = getDescription()
    newsUrl = getURL()
    newsImage = getImage()

    st.write(newsTitle)
    st.write(newsDescription)
    st.write(newsUrl)
    st.write(newsImage)
    card()

    



