'''Loads the NAU web data and builds FAISS vectorstore'''

from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from src.config import MODEL_NAME
import os

def build_vectorstore():
    urls = [
        "https://nau.edu/admissions/",
        "https://nau.edu/graduate-college/",
        "https://nau.edu/siccs/",
        "https://catalog.nau.edu/Catalog/details?plan=CSMS"

    ]

    #loading the data
    docs = [WebBaseLoader(url).load()[0] for url in urls]

    #splitting text into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap=200, separators = ["\n\n", "\n", " ", ""])
    chunks = splitter.split_documents(docs)

    #Generate embeddings
    embeddings = HuggingFaceEmbeddings(model_name=MODEL_NAME)
    
    #Build FAISS vectorstore
    vectorstore = FAISS.from_documents(chunks, embeddings)
    os.makedirs("vectorstore",exist_ok=True)
    vectorstore.save_local("vectorstore")
    print("Vector store built and saved")

if __name__ == "__main__":
    build_vectorstore()

