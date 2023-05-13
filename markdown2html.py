#!/usr/bin/python3
"""
<<<<<<< HEAD
A script markdown2html that takes ana argument
"""
import sys
import markdown
import os

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    with open(input_file, "r") as f:
        markdown_content = f.read()

    html_content = markdown.markdown(markdown_content)

    with open(output_file, "w") as f:
        f.write(html_content)

    sys.exit(0)
=======
A script markdown2html.py that takes an argument 2 strings
"""
import sys
import hashlib

# Check if the number of arguments is correct
if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

# Read the input file
try:
    with open(sys.argv[1], 'r') as f:
        markdown_text = f.read()
except FileNotFoundError:
    print(f"Missing {sys.argv[1]}", file=sys.stderr)
    sys.exit(1)

# Convert the Markdown to HTML
html_text = ""

# Split the Markdown text into paragraphs
paragraphs = markdown_text.split('\n\n')

for paragraph in paragraphs:
    # Check for bold syntax
    paragraph = paragraph.replace('**', '<b>').replace('__', '<em>').replace('**', '</b>').replace('__', '</em>')

    # Check for [[...]] syntax
    start_index = paragraph.find('[[')
    while start_index != -1:
        end_index = paragraph.find(']]', start_index)
        if end_index != -1:
            content = paragraph[start_index+2:end_index]
            hashed_content = hashlib.md5(content.encode('utf-8')).hexdigest()
            paragraph = paragraph[:start_index] + hashed_content + paragraph[end_index+2:]
        start_index = paragraph.find('[[', start_index+1)

    # Check for ((...)) syntax
    start_index = paragraph.find('((')
    while start_index != -1:
        end_index = paragraph.find('))', start_index)
        if end_index != -1:
            content = paragraph[start_index+2:end_index]
            replaced_content = content.replace('i', 'ihi')
            paragraph = paragraph[:start_index] + replaced_content + paragraph[end_index+2:]
        start_index = paragraph.find('[[', start_index+1)

    # Generate the HTML for the paragraph
    html_text += f"<p>\n    {paragraph.replace('\n', '<br />\n    ')}\n</p>\n"

# Write the HTML to the output file
with open(sys.argv[2], 'w') as f:
    f.write(html_text)

# Exit with success status
sys.exit(0)
>>>>>>> 097011da7eebda4c0dee79f0557975303611421d
