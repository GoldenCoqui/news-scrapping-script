"""
Module: article_summarizer 

This module is used to summarize the contents of a text file using Gemini 
Generative AI API.

Functions:
- summarize(readFilePath, writeFilePath, index, headlinePath) -> None:
    Summarizes the content of an article and saves the summary.

Input:
- readFilePath (str): Path to the file containing the content to be summarized.
- writeFilePath (str): Path to the file where the summary will be saved.
- index (int): An identifier for the article (used for naming purposes).
- headlinePath (str): Optional path to the file containing the article headline.

Output:
- None (Saves the summary to the specified file)

SOLID Principle: Single Responsibility Principle (SRP)
- This module adheres to the Single Responsibility Principle (SRP) by focusing solely
- on summarizing the content of articles using a generative AI model. 

"""

import os
import google.generativeai as genai
from file_handler import save_to_file
from dotenv import load_dotenv

# loads .env that will hold API key KEEP PRIVATE
load_dotenv()

# API key configuration
genai.configure(api_key=os.getenv("API_KEY"))

# Initialize the generative model
model = genai.GenerativeModel('gemini-pro')

def summarize(readFilePath, writeFilePath, index, headlinePath):
  try:
    
    # reads headline article text file and saves in headline
    if headlinePath is not None:
      with open(f"{headlinePath}article_{index}.txt", 'r', encoding='utf-8') as headerFile:
        headline = headerFile.read()

    # reads text file with the article and saves it in content
    # using content variable and an extra prompt it summarizes article and saves in response
    with open(f"{readFilePath}article_{index}.txt", 'r', encoding='utf-8') as file:
      content = file.read()
      response = model.generate_content(content + "summarize the follwing article to less than 100 words")

    # saves the information in processed folder       
    with open(f"{writeFilePath}article_{index}.txt", 'w', encoding='utf-8') as file:
      save_to_file(index,writeFilePath,None, headline, response.text)

  except Exception as e:
    print(f"Error Summarizing article {index}: {str(e)}")