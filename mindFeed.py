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


# Fetching the RSS news feed
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

# Card UI
def card():  ## inspired by https://github.com/gamcoh/st-card
    data = newsImage
    from streamlit_card import card
    card = card(
        title=newsTitle,
        text=" ",
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


# The AI function
    
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')


def ai_summary(newsTitle, newsDescription):

    context = """You are an expert news summarizer with an ability to 
    summarize news in a very interesting and indulging way, you have
    to be short and to the point
    The format should be: the news title but rewritten in an indulging way
    and your summary from the next line, like a professional news article.
    You will not mention the word "title" or "description" or "summary" in your response AND KEEP THE SUMMARY SHORT.
    YOU WILL ONLY RESPOND WITH THE SUMMARY IN TEXT FORMAT AND NOTHING ELSE.
    newsTitle:{newsTitle} newsDescription:{newsDescription}"""

    context = context.format(newsTitle=newsTitle, newsDescription=newsDescription)
    response = model.generate_content(context, stream = True)
    response.resolve()
    return response.text


################################################################################################

# Streamlit UI
#st.title("MindFeed")
#positioning the title
st.markdown("<h1 style='text-align: center; color: white;'>MindFeed 🧠</h1>", unsafe_allow_html=True)
#st.write("Treat your mind to the latest news articles.")
#positioning the subtitle
st.markdown("<h3 style='text-align: center; color: white;'>A Treat for you mind.</h3>", unsafe_allow_html=True)
st.write("_" * 50)


if st.button("Get News"): 
    newsTitle = getTitle()
    newsDescription = getDescription()
    newsUrl = getURL()
    newsImage = getImage()
    card()
    with st.spinner('✨Thinking...'):
            summary = ai_summary(newsTitle, newsDescription)

            st.write(summary)
            st.write("Read more [here](" + newsUrl + ")")
