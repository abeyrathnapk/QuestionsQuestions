## Interactive Notebooks: Marimo

[Marimo](https://marimo.app/) is a new take on notebooks that solves some headaches of Jupyter. It runs cells reactively - when you change one cell, all dependent cells update automatically, just like a spreadsheet.

Marimo's cells can't be run out of order. This makes Marimo more reproducible and easier to debug, but requires a mental shift from the Jupyter/Colab way of working.

It also runs Python directly in the browser and is quite interactive. [Browse the gallery of examples](https://marimo.io/gallery). With a wide variety of interactive widgets, It's growing popular as an alternative to Streamlit for building data science web apps.

Common Operations:

```python
# Create new notebook
uvx marimo new

# Run notebook server
uvx marimo edit notebook.py

# Export to HTML
uvx marimo export notebook.py
```

Best Practices:

1. **Cell Dependencies**
   - Keep cells focused and atomic
   - Use clear variable names
   - Document data flow between cells
2. **Interactive Elements**

   ```python
   # Add interactive widgets
   slider = mo.ui.slider(1, 100)
   # Create dynamic Markdown
   mo.md(f"{slider} {"🟢" * slider.value}")
   ```

3. **Version Control**
   - Keep notebooks are Python files
   - Use Git to track changes
   - Publish on [marimo.app](https://marimo.app/) for collaboration

[[Image description: Here's alt text for the image: A screenshot shows a computer screen displaying data analysis related to handwritten digit recognition. The top shows ten small, dark images of the handwritten number "2" in different styles. Below that, the main section of the screen shows data in tables and bar graphs. The tables list numerical indexes, x and y coordinates, and the digit (all "2"s and "8"s in the visible data), showing corresponding values for each handwritten "2".  The bar graphs visually represent the distribution of x, y coordinates, and digits. The colors are mainly shades of green and beige on a light background. The bottom-right corner shows a small video frame of a person presenting at a conference; logos for Meta, Bloomberg, Netflix, and others are visible on the presentation screen.  The text "Here's a preview of the images you've selected:" and "Here's all the data you've selected:" are also present.]](https://youtu.be/9R2cQygaoxQ)
