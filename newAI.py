import streamlit as st
import requests, json
import time
import google.generativeai as genai
from dotenv import load_dotenv
import os
from newsAPI import fetch_news, getNews, getTitle, getURL, getImage, getDescription
load_dotenv()


st.title("GET NEWS NOW! ☁️")

#configure the API key and the model
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')




# ## initializing the message history
# if "messages" not in st.session_state:
#     st.session_state.messages = []



def generate_summary():
    news = getDescription()
    print(news)
    context = """ You are an expert news analyst and you have been asked to summarize the news. Here is the news:{news} """
    summary = model.generate_content(context)
    st.write(summary)




if st.button("Generate Summary"):
    generate_summary()
    st.write("Summary Generated Successfully")