#!/usr/bin/python3
"""
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
