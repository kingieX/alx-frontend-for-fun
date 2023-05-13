#!/usr/bin/python3
"""
Simple Markdown to HTML converter using built-in modules
"""

import sys
import os
import re
import html

def convert_markdown_to_html(markdown_text):
    # Convert headers
    markdown_text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', markdown_text, flags=re.MULTILINE)

    # Convert emphasis (italics)
    markdown_text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', markdown_text)

    # Convert strong emphasis (bold)
    markdown_text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', markdown_text)

    # Convert inline code
    markdown_text = re.sub(r'`(.+?)`', r'<code>\1</code>', markdown_text)

    # Convert paragraphs
    paragraphs = re.split(r'\n{2,}', markdown_text)
    paragraphs = [f'<p>{html.escape(p)}</p>' for p in paragraphs]
    html_text = '\n'.join(paragraphs)

    return html_text

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, "r") as f:
            markdown_content = f.read()

        html_content = convert_markdown_to_html(markdown_content)

        with open(output_file, "w") as f:
            f.write(html_content)

        sys.exit(0)

    except FileNotFoundError:
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)
