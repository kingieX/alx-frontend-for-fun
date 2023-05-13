# alx-frontend-for-fun

0. Start a script

Write a script markdown2html.py that takes an argument 2 strings:

First argument is the name of the Markdown file
Second argument is the output file name
Requirements:

If the number of arguments is less than 2: print in STDERR Usage: ./markdown2html.py README.md README.html and exit 1
If the Markdown file doesn’t exist: print in STDER Missing <filename> and exit 1
Otherwise, print nothing and exit 0

1. Headings

mprove markdown2html.py by parsing Headings Markdown syntax for generating HTML:

Syntax: (you can assume it will be strictly this syntax)

Markdown	HTML generated
# Heading level 1	<h1>Heading level 1</h1>
## Heading level 2	<h2>Heading level 1</h2>
### Heading level 3	<h3>Heading level 1</h3>
#### Heading level 4	<h4>Heading level 1</h4>
##### Heading level 5	<h5>Heading level 1</h5>
###### Heading level 6	<h6>Heading level 1</h6>

2. Unordered listing


