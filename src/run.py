"""
Module: run

This module serves as the main program to run the scraper, title_scraper, and ai_summary.

Functions:
- main() -> None:
    Main function to execute scraper, title_scraper, and ai_summary.

Input:
- urls.txt - textfile filled with urls to the Ring articles

Output:
- None

SOLID Principle: Single Responsibility Principle (SRP)
- This module follows the Single Responsibility Principle by orchestrating the execution of specific functionalities.
- It aims to have only one reason to change: modifications related to the coordination of the scraping and saving logic.

"""

from scraper import scrape_news
from title_scraper import scrape_title
from ai_summary import summarize

def main():

    # urls.txt is a list of all the urls in the text file
    with open('../Data/raw/urls.txt', 'r') as file:
        urls = file.read().splitlines()

    # goes through all the urls in urls list and starts with the first one.
    for index, url in enumerate(urls, start=1):

        print(f"Scraping Article {index}")

        scrape_title(url, index, "../Data/raw/headlines/")
        scrape_news(url, index, "../Data/raw/articles/")

        print('-' * 100)
        
        print(f"Summarizing Article {index}")

        summarize("../Data/raw/articles/","../Data/processed/", index, "../Data/raw/headlines/")

        print('=' * 100)

if __name__ == "__main__":
    main()
