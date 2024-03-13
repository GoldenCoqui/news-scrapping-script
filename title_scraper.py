"""
Module: title_scraper

This module provides functionality for scraping the headline of an article.
(Specifically from the Ring)

Functions:
- scrape_title(url: str, index: int) -> str:
    Scrapes the main content of a news article from the given URL.

Input:
- url: str - The URL of the news article.
- index: int - The index or identifier of the article.

Output:
- str - headline of the article.
- If the scraping is unsuccessful, returns None.

SOLID Principle: Single Responsibility Principle (SRP)
- This module follows the Single Responsibility Principle by focusing on the specific task of scraping article headlines.
- It aims to have only one reason to change: modifications related to the scraping logic for headlines.

"""
import requests
from bs4 import BeautifulSoup

def scrape_title(url, index):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        article_header = soup.find('h1') and soup.find('div', {'id': 'content'}) and soup.find('div', {'class': 'full-post'})

        if article_header:
            headline = article_header.find('h1').get_text() if article_header else "No headline found"

            return headline

        else:
            return None

    except Exception as e:
        print(f"Error downloading article {index} from {url}: {str(e)}")
        return None
