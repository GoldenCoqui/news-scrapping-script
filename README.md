# [Check my site for information about this Repo](https://goldencoqui.github.io/)

## News Scraper

The **News Scraper** is a Python program designed to scrape news articles from provided URLs, extracting relevant content, and saving it to individual text files. This README.md file provides comprehensive instructions on how to set up the environment, run the program, and understand the output.

## Table of Contents

- [Setup](#setup)
  - [Clone the Repository](#1-clone-the-repository)
  - [Create Conda Environment](#2-create-conda-environment)
- [Usage](#usage)
  - [Add URLs to `urls.txt`](#1-add-urls-to-urlstxt)
  - [Run the Program](#2-run-the-program)
- [Output](#output)
- [Additional Information](#additional-information)

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/news-scraper.git
cd news-scraper
```

### 2. Create Conda Environment

```bash
conda env create -f requirements.yml
conda activate news-scraper-env
```

# Usage

### 1. Add URLs to `urls.txt`

### 2. Run the Program

```bash
python news_scraper.py
```
### Output

The program will start scraping the articles. Individual text files will be created in the articles folder, named article_1.txt, article_2.txt, etc.

# Additional Information

   - The program uses the BeautifulSoup library for web scraping.
   - Ensure you have an active internet connection for the program to fetch the articles.

If you encounter any issues or have questions, feel free to open an issue on this repository.
