'''Loads the NAU web data and builds FAISS vectorstore'''

from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import os


def build_vectorstore():
    urls = [
        "https://nau.edu/admissions/",
        "https://nau.edu/graduate-college/",
        "https://nau.edu/siccs/",

    ]

    loader = WebBaseLoader(urls)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter()
    chunks = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)
    os.makedirs("vectorstore",exist_ok=True)
    vectorstore.save_local("vectorstore")
    print("Vector store built and saved")

if __name__ == "__main__":
    build_vectorstore()

