"""
Module: run

This module serves as the main program to run the scraper, title_scraper, and file_handler.

Functions:
- main() -> None:
    Main function to execute scraper, title_scraper, and file_handler.

Input:
- urls.txt - textfile filled with urls to the Ring articles

Output:
- None

SOLID Principle: Single Responsibility Principle (SRP)
- This module follows the Single Responsibility Principle by orchestrating the execution of specific functionalities.
- It aims to have only one reason to change: modifications related to the coordination of the scraping and saving logic.

"""

from scraper import scrape_news
from file_handler import save_to_file
from title_scraper import scrape_title

def main():
    # urls is a list of all the urls in the text file
    with open('./Data/raw/urls.txt', 'r') as file:
        urls = file.read().splitlines()

    # goes through all the urls in urls list and starts with the first one.
    # Index is the for loop default variable.
    for index, url in enumerate(urls, start=1):
        print(f"Scraping Article {index}")
        content_text = scrape_news(url, index)
        headline = scrape_title(url, index)

        if content_text is not None:
            save_to_file(index, "Data/processed/", url, None, content_text)

        if headline is not None:
            save_to_file(index,"Data/raw/headlines/", url, headline, None)

        print('-' * 40)

if __name__ == "__main__":
    main()
