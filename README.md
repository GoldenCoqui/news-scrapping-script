# AI Article Summarizer

The **AI Article Summarizer** is a Python program designed to scrape news articles from provided URLs, extracting relevant content, and saving it to individual text files.  Then taking those text files and putting them into Google Gemini API to summarize them, for a more bite size read. This README.md file provides comprehensive instructions on how to set up the environment, run the program, and understand the output.

## Table of Contents

- [Setup](#setup)
  - [Clone the Repository](#1-clone-the-repository)
  - [Create Conda Environment](#2-create-conda-environment)
  - [Get Google Gemini API Key](#3-get-google-gemini-api-key)
- [Usage](#usage)
  - [Add URLs to `urls.txt`](#1-add-urls-to-urlstxt)
  - [Run the Program](#2-run-the-program)
- [Output](#output)
- [Additional Information](#additional-information)

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/GoldenCoqui/news-scrapping-script/tree/ai_summary
```

### 2. Create Conda Environment

```bash
conda env create -f env.yml
conda activate ai-summary
```

### 3. Get Google Gemini API Key
In the ai_summary.py where it asks for an API_KEY insert your own API_KEY. `REMEMBER TO KEEP YOUR KEY SECURE`.

# Usage

### 1. Add URLs to `urls.txt`

This will work best with articles from the Ring website.  A boxing media outlet.

### 2. Run the Program

```bash
python run.py
```
### Output

The program will start scraping the articles. Individual text files will be created in the articles folder, named article_1.txt, article_2.txt, etc.  The program will then start taking those article_#.txt and use Gemini API to summarize them.

# Additional Information

   - The program uses the BeautifulSoup library for web scraping.
   - The program uses Google Gemini API for summarzing the articles.
   - Ensure you have an active internet connection for the program to fetch the articles.

If you encounter any issues or have questions, feel free to open an issue on this repository.
