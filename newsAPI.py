import os
import requests
from dotenv import load_dotenv
import random

# Load environment variables from .env file
load_dotenv()

NEWS_API_KEY = os.getenv('news_api')
NEWS_API_ENDPOINT = 'https://newsapi.org/v2/top-headlines'

random_page = random.randint(1, 50)

def fetch_news(api_key):
    # Specify parameters for the API request
    params = {
        'country': 'us',  # Change this to the desired country code
        'pageSize': 1,     # Number of articles to fetch
        'page': random_page
    }
    headers = {
        'Authorization': f'Bearer {api_key}'
    }

    try:
        response = requests.get(NEWS_API_ENDPOINT, params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        articles = data['articles']
        return articles
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return None

# def getNews():
#     # Fetch news articles from a random page
#     articles = fetch_news(NEWS_API_KEY)
#     if articles:
#         print("Latest news articles:")
#         for idx, article in enumerate(articles, start=1):
#             title = article['title']
#             description = article['description']
#             url = article['url']
#             image_url = article['urlToImage']

#             # # Print formatted output
#             # print()
#             # print(f"Header: {title}")
#             # print(f"Description: {description}")
#             # print(f"URL: {url}")
#             # print(f"Image: {image_url}")
#             # print("_" * 50)  # Separator for readability

#             return title, description, url, image_url
#     else:
#         print("No news articles fetched.")

# function to get the title
def getTitle():
    articles = fetch_news(NEWS_API_KEY)
    if articles:
        for idx, article in enumerate(articles, start=1):
            title = article['title']
        return title
    else:
        print("No news articles fetched.")

# function to get the description
def getDescription():
    articles = fetch_news(NEWS_API_KEY)
    if articles:
        for idx, article in enumerate(articles, start=1):
            description = article['description']
        return description
    else:
        print("No news articles fetched.")

# function to get the URL
def getURL():
    articles = fetch_news(NEWS_API_KEY)
    if articles:
        for idx, article in enumerate(articles, start=1):
            url = article['url']
        return url
    else:
        print("No news articles fetched.")

# function to get the image
def getImage():
    articles = fetch_news(NEWS_API_KEY)
    if articles:
        for idx, article in enumerate(articles, start=1):
            image_url = article['urlToImage']
        return image_url
    else:
        print("No news articles fetched.")

# test the functions
print(getTitle())
print(getDescription())
print(getURL())
print(getImage())

