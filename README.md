# AI Article Summarizer

The **AI Article Summarizer** is a Python program designed to scrape news articles from provided URLs, extracting relevant content, and saving it to individual text files.  Next, it takes those text files and puts them into Google Gemini API to summarize them, for a more bite size read. This README.md file provides comprehensive instructions on how to set up the environment, run the program, and understand the output.

## Table of Contents

- [Setup](#setup)
  - [Clone the Repository](#1-clone-the-repository)
  - [Create Conda Environment](#2-create-conda-environment)
  - [Get Google Gemini API Key](#3-get-google-gemini-api-key)
  - [Test Gemini API](#4-test-gemini-api)
- [Usage](#usage)
  - [Add URLs to `urls.txt`](#1-add-urls-to-urlstxt)
  - [Run the Program](#2-run-the-program)
- [Output](#output)
- [Additional Information](#additional-information)

## Setup

### 1. Clone the Repository

```bash
git clone -b ai_summary https://github.com/GoldenCoqui/news-scrapping-script.git
```

### 2. Create Conda Environment

```bash
conda env create -f env.yml
conda activate ai-summary
```

### 3. Get Google Gemini API Key
Go to https://ai.google.dev/ to generate your own API key. You will need a google account. `REMEMBER TO KEEP YOUR KEY SECURE`. Put your api key in a .env and set up the .env with the format below. You can leave your .env outside of the src and Data file.

```bash
API_KEY="Your-Actual-API-Key-Goes-Here"
```
### 4. Test Gemini API
Once you have your API key, try this code to see if the Gemini API will give you a response back.  The response should show up in the terminal.

```bash
import google.generativeai as genai
from dotenv import load_dotenv
import os

# loads .env that should hold API key KEEP PRIVATE
load_dotenv()

# configures your session with API key
genai.configure(api_key=os.getenv("API_KEY"))

# selects the gemini-pro model to send prompts to
model = genai.GenerativeModel('gemini-pro')

# sending prompts and saving them in a variable
response = model.generate_content("What country is Tokyo in?")

# prints Gemini response in the terminal
print(response.text)
```

# Usage

### 1. Add URLs to `urls.txt`

This will work best with articles from the Ring website,  a boxing media outlet.

### 2. Run the Program

```bash
python run.py
```
### Output

The program will start scraping the articles. Individual text files will be created in the Data/processed/articles folder, named article_1.txt, article_2.txt, etc.  The program will then start taking those article_#.txt and use Gemini API to summarize them. The summarized articles will then be put in Data/processed/summarized.  The terminal will let the user know what articles are being scrapped and summarized in real time.

# Additional Information

   - The program uses the BeautifulSoup library for web scraping.
   - The program uses Google Gemini API for summarzing the articles.
   - The program uses Python-dotenv to find the .env file to keep API key secure from version control
   - Ensure you have an active internet connection for the program to fetch the articles.

If you encounter any issues or have questions, feel free to open an issue on this repository.
