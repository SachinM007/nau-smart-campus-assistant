from setuptools import setup, find_packages

setup(
    name="nau-smart-campus-assistant",
    version="0.1.0",
    description="A Retrieval-Augmented Generation chatbot for Northern Arizona University",
    author="Sachin Miryala",
    packages=find_packages(),
    install_requires=[
        "langchain",
        "sentence-transformers",
        "faiss-cpu",
        "streamlit",
        "transformers",
        "langchain-community"
    ],
)
