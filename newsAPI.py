import os
import requests
from dotenv import load_dotenv
import random

# Load environment variables from .env file
load_dotenv()

NEWS_API_KEY = os.getenv('news_api')
NEWS_API_ENDPOINT = 'https://newsapi.org/v2/top-headlines'

random_page = random.randint(1, 10)

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

def main():
    # Fetch news articles from a random page
    articles = fetch_news(NEWS_API_KEY)
    if articles:
        print("Latest news articles:")
        for idx, article in enumerate(articles, start=1):
            title = article['title']
            description = article['description']
            url = article['url']
            image_url = article['urlToImage']

            # Print formatted output
            print(f"{idx}. {title}")
            print(f"   {description}")
            print(f"   URL: {url}")
            print(f"   Image: {image_url}")
            print("=" * 50)  # Separator for readability
    else:
        print("No news articles fetched.")

if __name__ == '__main__':
    main()
