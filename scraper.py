"""
Module: scraper

This module provides functionality for scraping the main content of an article.
(Specifically from the Ring)

Functions:
- scrape_news(url: str, index: int) -> str:
    Scrapes the main content of a news article from the given URL.

Input:
- url: str - The URL of the news article.
- index: int - The index or identifier of the article.

Output:
- str - content text of the article.
- If the scraping is unsuccessful, returns None.

SOLID Principle: Single Responsibility Principle (SRP)
- This module follows the Single Responsibility Principle by focusing on the specific task of scraping article headlines.
- It aims to have only one reason to change: modifications related to the scraping logic for article.

"""
import requests
from bs4 import BeautifulSoup

def scrape_news(url, index):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        article_content = soup.find('div', {'class': 'text-wrap'}) or soup.find('div', {'class': 'content'})

        if article_content:
            paragraphs = article_content.find_all(['p'])
            content_text = '\n'.join(p.get_text() for p in paragraphs)

            return content_text

        else:
            return None

    except Exception as e:
        print(f"Error downloading article {index} from {url}: {str(e)}")
        return None, None
