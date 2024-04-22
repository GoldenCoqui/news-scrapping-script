"""
Module: title_scraper

This module provides functionality for scraping the headline of an article.
It will also put the headline of the article in a text file using save_to_file()
(Specifically from the Ring)

Functions:
- scrape_title(url: str, index: int) -> str:
    Scrapes the headline of a news article from the given URL.

Input:
- url: str - The URL of the news article.
- index: int - The index or identifier of the article.
- filePath: str - file path for the location of the headline (Example/file/path/)

Output:
- None

SOLID Principle: Single Responsibility Principle (SRP)
- This module follows the Single Responsibility Principle by focusing on the specific task of scraping article headlines.
- It aims to have only one reason to change: modifications related to the scraping logic for headlines.

"""
import requests
from bs4 import BeautifulSoup
from file_handler import save_to_file

def scrape_title(url, index, filePath):
    # Set headers to simulate a web browser for better compatibility
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        # Send a GET request to the URL and check for successful response
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Parse the HTML content of the response
        soup = BeautifulSoup(response.text, 'html.parser')

        # Try to find the headline using two common class names and id names and html tags
        article_header = soup.find('h1') and soup.find('div', {'id': 'content'}) and soup.find('div', {'class': 'full-post'})

        if article_header:
            # Extract all h1 elements within article header
            headline = article_header.find('h1').get_text() if article_header else "No headline found"
            
            # Call a separate function (not shown here) to save the scraped content
            save_to_file(index,filePath,url,headline,None)


    except Exception as e:
        print(f"Error downloading article {index} from {url}: {str(e)}")
        return None
