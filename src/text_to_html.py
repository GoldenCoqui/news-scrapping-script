from xml.etree import ElementTree as ET
import os

def html_head_tags(root):
    head = ET.SubElement(root, "head")
    title = ET.SubElement(head, "title")
    title.text = "My News Aggregation Site"

def html_tags_content(root, header, paragraph):
    # Find or create the body element
    body = root.find("body")
    if body is None:
        body = ET.SubElement(root, "body")

    # Create header and paragraph elements in body
    h1 = ET.SubElement(body, "h1")
    h1.text = header
    p = ET.SubElement(body, "p")
    p.text = paragraph

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

    # Extract header and paragraph, since you will be having multiple articles the logic will
    # change for the code given below. 
    header = content[0].strip()
    paragraph = "".join(content[1:]).strip()

    if os.path.exists(html_file):
        tree = ET.parse(html_file)
        root = tree.getroot()
    else:
        root = ET.Element("html")

    # Create head and body elements if they don't exist
    if root.find("head") is None:
        html_head_tags(root)

    # Add header and paragraph content to the HTML file
    html_tags_content(root, header, paragraph)

    # Write HTML tree to file
    with open(html_file, 'wb') as f:
        tree = ET.ElementTree(root)
        tree.write(f, encoding='utf-8', xml_declaration=True)


# Example usage:
# txt_file = "my_text.txt"
# html_file = "all_news_articles.html"
# txt_to_html(txt_file, html_file)
# print(f"Converted text file '{txt_file}' to HTML file '{html_file}'.")
