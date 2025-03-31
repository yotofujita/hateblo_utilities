import sys 
import re
import html


def extract_plain_text(text):
    # Extract the title
    title_match = re.search(r'^TITLE:\s*(.+)', text, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else ''

    # Extract the category
    category_match = re.search(r'^CATEGORY:\s*(.+)', text, re.MULTILINE)
    categories = category_match.group(1).strip() if category_match else ''

    # Extract the body (everything after 'BODY:')
    body_match = re.search(r'^BODY:\s*(.*)', text, re.DOTALL | re.MULTILINE)
    body_raw = body_match.group(1).strip() if body_match else ''

    # Remove all HTML tags
    body_clean = re.sub(r'<[^>]+>', '', body_raw)

    # Optional: Unescape HTML entities (e.g., &gt;, &lt;)
    body_clean = html.unescape(body_clean)

    # Combine title and clean body
    result = f"TITLE: {title}\n\nCATEGORY: {categories}\n\n{body_clean}"
    return result, title, categories, body_clean


export_file_path = sys.argv[1] 

with open(export_file_path, "r") as f:
    export_text = f.read()

splitter = """-----
--------"""
for text in export_text.split(splitter)[:-1]:

    result, title, categories, body_clean = extract_plain_text(text)
    print(result+"\n\n"+"="*50+"\n")