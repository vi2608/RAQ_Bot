from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

def load_file():

    pdf_paths = ["./data/f1.pdf", "./data/f2.pdf"]
    all_pages = []
    for path in pdf_paths:
        loader = PyPDFLoader(path)
        pages = loader.load()
        all_pages.extend(pages)
        print(f"Loaded {len(pages)} pages from {path}")
    print(f"Total pages loaded: {len(all_pages)}")

    raw_text = ''
    for i, doc in enumerate(all_pages):
        text = doc.page_content
        if text:
            raw_text += text
            
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap  = 100,
    )

    docs = text_splitter.split_text(raw_text)
    
    return docs