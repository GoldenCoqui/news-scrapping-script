import requests
from bs4 import BeautifulSoup

def scrape_news(url, index):
    try:
        # Add headers to mimic a regular web browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        # Send a GET request to the URL with headers
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the main content of the article (modify this based on the structure of the website)
        article_header = soup.find('h1') and soup.find('div', {'id': 'content'}) and soup.find('div', {'class': 'full-post'})
        article_content = soup.find('div', {'class': 'text-wrap'}) or soup.find('div', {'class': 'content'})
        
        # Check if article_content is not None before accessing its text content
        if article_content:
            # Use more specific selectors to extract text content
            headline = article_header.find('h1').get_text() if article_header else "No headline found"
            paragraphs = article_content.find_all(['p'])
            content_text = '\n'.join(p.get_text() for p in paragraphs)

            # Save the content to a file
            with open(f'articles/article_{index}.txt', 'w', encoding='utf-8') as file:
                file.write(f"Headline: {headline}\n\n")
                file.write(content_text)

            print(f"Article {index} from {url} downloaded successfully.")
        else:
            print(f"No article content found for {url}.")

    except Exception as e:
        print(f"Error downloading article {index} from {url}: {str(e)}")

with open('urls.txt', 'r') as file:
    urls = file.read().splitlines()

for index, url in enumerate(urls, start=1):
    print(f"Scraping Article {index}")
    scrape_news(url, index)
    print('-' * 40)
