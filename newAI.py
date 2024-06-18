import streamlit as st
import requests, json
import time
import google.generativeai as genai
from dotenv import load_dotenv
import os
from newsAPI import getTitle, getURL, getImage, getDescription
load_dotenv()


print("Fetching news articles...")
print(getTitle())
print(getDescription())