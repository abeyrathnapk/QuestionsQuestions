## Wikipedia Data with Python

[[Image description: Here's alt text for the image:

A slide presentation title reads, "Get the data:Wikimedia," in a large, bold font against a white background.  Below, smaller text indicates the course as "TOOLS IN DATA SCIENCE," the instructor as "ANAND S," and the tutorial instructor as "DIBU PHILIP." The bottom of the slide features a solid, light-blue bar. In the top right corner is a circular logo for IIT Madras Online Degree, showing a gold seal with dark text.  The overall color scheme is predominantly white with dark text and accents of gold and light blue.]](https://youtu.be/b6puvm-QEY0)

You'll learn how to scrape data from Wikipedia using the `wikipedia` Python library, covering:

- **Installing and Importing**: Use pip install to get the Wikipedia library and import it with import wikipedia as wk.
- **Keyword Search**: Use the search function to find Wikipedia pages containing a specific keyword, limiting results with the results argument.
- **Fetching Summaries**: Use the summary function to get a concise summary of a Wikipedia page, limiting sentences with the sentences argument.
- **Retrieving Full Pages**: Use the page function to obtain the full content of a Wikipedia page, including sections and references.
- **Accessing URLs**: Retrieve the URL of a Wikipedia page using the url attribute of the page object.
- **Extracting References**: Use the references attribute to get all reference links from a Wikipedia page.
- **Fetching Images**: Access all images on a Wikipedia page via the images attribute, which returns a list of image URLs.
- **Extracting Tables**: Use the pandas.read_html function to extract tables from the HTML content of a Wikipedia page, being mindful of table indices.

Here are links and references:

- [Wikipedia Library - Notebook](https://colab.research.google.com/drive/1-w8Jo6xcQs2jK0NxNddPW4HVCZhXmTBe)
- Learn about the [`wikipedia` package](https://wikipedia.readthedocs.io/en/latest/)

**NOTE**: Wikipedia is constantly edited. The page may be different now from when the video was recorded. Handle accordingly.
