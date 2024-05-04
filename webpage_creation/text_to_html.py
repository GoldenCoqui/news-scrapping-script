from xml.etree import ElementTree as ET  # Import ElementTree module as ET for ease of use
import os  # Import os module for file handling operations

def html_head_tags(root):
    """
    Add head tags to the HTML tree.

    Args:
        root (Element): The root element of the HTML tree.
    """
    head = ET.SubElement(root, "head")  # Create 'head' element under root
    title = ET.SubElement(head, "title")  # Create 'title' element under 'head'
    title.text = "My News Aggregation Site"  # Set text content of 'title' element

def html_tags_content(root, header, paragraph):
    """
    Add content (header and paragraph) tags to the HTML tree body.

    Args:
        root (Element): The root element of the HTML tree.
        header (str): The header text.
        paragraph (str): The paragraph text.
    """
    # Find or create the body element
    body = root.find("body")
    if body is None:  # If body element doesn't exist, create one
        body = ET.SubElement(root, "body")

    # Create header and paragraph elements in body
    h1 = ET.SubElement(body, "h1")  # Create 'h1' element under 'body'
    h1.text = header  # Set text content of 'h1' element
    p = ET.SubElement(body, "p")  # Create 'p' element under 'body'
    p.text = paragraph  # Set text content of 'p' element


def txt_to_html(txt_file, html_file):
    """
    Converts a text file with header and paragraph to an HTML file.
    Make necessary changes for multiple news articles. This script is
    only for one news article.

    Args:
        txt_file (str): Path to the text file.
        html_file (str): Path to the output HTML file.
    """
    # Read text file content
    with open(txt_file, 'r') as f:
        content = f.readlines()

    header = content[0].strip()  # Get the header text and remove leading/trailing whitespaces
    paragraph = "".join(content[1:]).strip()  # Get the paragraph text and remove leading/trailing whitespaces

    if os.path.exists(html_file):  # Check if HTML file exists
        tree = ET.parse(html_file)  # Parse HTML file to get the tree
        root = tree.getroot()  # Get the root element of the HTML tree
    else:
        root = ET.Element("html")  # Create a new HTML tree if file doesn't exist

    if root.find("head") is None:  # If 'head' element doesn't exist in the tree, add head tags
        html_head_tags(root)

    html_tags_content(root, header, paragraph)  # Add content tags to the HTML tree body

    # Write HTML tree to file
    with open(html_file, 'wb') as f:  # Open HTML file in binary write mode
        tree = ET.ElementTree(root)  # Create an ElementTree with root as the root element
        tree.write(f, encoding='utf-8', xml_declaration=True)  # Write the tree to the file with UTF-8 encoding and XML declaration

def main():
     # urls.txt is a list of all the urls in the text file
    with open('../Data/raw/urls.txt', 'r') as file:
        urls = file.read().splitlines()

    html_file_path = "html_text_file/html_article.html"

    # Check if the file exists before attempting to delete it
    if os.path.exists(html_file_path):
        os.remove(html_file_path)
        print(f"File '{html_file_path}' has been deleted.")
    else:
        print(f"File '{html_file_path}' does not exist.")

    index = 0

    # goes through all the urls in urls list and starts with the first one.
    for index, url in enumerate(urls, start=1):


        print('=' * 100)

        txt_to_html(f"summarized/article_{index}.txt", f"html_text_file/html_article.html")
        print(f"Summarized article_{index}.txt successfully added to article_html.txt")

        print('=' * 100)


if __name__ == "__main__":
    main()
