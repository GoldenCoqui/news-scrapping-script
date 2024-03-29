"""
Module: save_to_file

This module provides functionality for saving the scraped article content to a text file.

Functions:
- save_to_file(index: int, filePath: str, url: str, headline: str, content_text: str) -> None:
    Saves the headline and content of a news article to a text file.

Input:
- index: int - The index or identifier of the article.
- filePath: str - The path where the text file will be saved.
    - In this format file/path/directory/
- url: str - The URL of the news article.
- headline: str - The headline of the article.
- content_text: str - The content text of the article.

Output:
- Creates text files for the article content and the headline, under the same text file name 

SOLID Principle: Single Responsibility Principle (SRP)
- This module follows the Single Responsibility Principle by focusing on the specific task of saving article content to a file.
- It aims to have only one reason to change: modifications related to the file-saving logic.

"""
import textwrap

def save_to_file(index, filePath, url, headline, content_text):
   try:
       with open(f"{filePath}article_{index}.txt", 'w', encoding='utf-8') as file:
           
           if headline is not None:
               
               file.write(f"Headline: {headline}\n\n\n")
               
               print(f"Article {index} header downloaded sucessfully")

           if content_text is not None:
               
               # Wrap text with a maximum width of 80 characters
               wrapped_content = textwrap.fill(content_text, width=80)

               file.write(wrapped_content)

               if url is not None:
                  print(f"Article {index} from {url} downloaded successfully.")
               else:
                    print(f"Article {index} downloaded successfully.")

   except Exception as e:
       print(f"Error saving article {index} from {url} to file: {str(e)}")
