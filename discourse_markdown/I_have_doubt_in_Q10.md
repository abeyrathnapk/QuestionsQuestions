# I have doubt in Q10

[View on Discourse](https://discourse.onlinedegree.iitm.ac.in/t/i-have-doubt-in-q10/166647)

---
**23f1001806** on 2025-02-09T14:51:52.566Z:

I have doubt in question 10 to convert pdf to markdown  
I am not getting correct markdown  
[@pds_staff](/u/pds_staff)



---
**22f3000092** on 2025-02-09T18:15:12.582Z:

Try using the pymupdf4llm Library  
pip install pymupdf4llm

import pymupdf4llm  
md_text = pymupdf4llm.to_markdown(“input.pdf”)

import pathlib  
pathlib.Path(“output.md”).write_bytes(md_text.encode())

import pymupdf4llm  
llama_reader = pymupdf4llm.LlamaMarkdownReader()  
llama_docs = llama_reader.load_data(“input.pdf”)



