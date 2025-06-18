## Documentation: Markdown

Markdown is a lightweight markup language for creating formatted text using a plain-text editor. It's the standard for documentation in software projects and data science notebooks.

Watch this introduction to Markdown (19 min):

[[Image description: Here's alt text for the image:

"A promotional graphic for a Markdown Crash Course. The graphic is primarily dark gray with lighter gray accents. A dark gray rectangle at the top contains a lighter gray square with a large white 'M' and a white downward-pointing arrow.  To the right of this, the text 'Markdown Crash Course' appears in white. At the bottom, the website address 'TraversyMedia.com' is visible in white."]](https://youtu.be/HUBNt18RFbo)

Common Markdown syntax:

````
# Heading 1
## Heading 2

**bold** and *italic*

- Bullet point
- Another point
  - Nested point

1. Numbered list
2. Second item

[Link text](https://url.com)
[Image description: [Image description unavailable]]

```python
# Code block
def hello():
    print("Hello")
```

&gt; Blockquote
````

There is also a [GitHub Flavored Markdown](https://github.github.com/gfm/) standard which is popular. This includes extensions like:

```
- [ ] Incomplete task
- [x] Completed task

~~Strikethrough~~

Tables:

| Column 1 | Column 2 |
|----------|----------|
| Cell 1   | Cell 2   |

```

Tools for working with Markdown:

- [markdown2](https://pypi.org/project/markdown2/): Python library to convert Markdown to HTML
- [markdownlint](https://github.com/DavidAnson/markdownlint): Linting
- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one): VS Code extension
- [pandoc](https://pandoc.org/): Convert between formats
