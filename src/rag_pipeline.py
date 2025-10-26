from langchain_community.vectorstores import FAISS
from .config import MODEL_NAME, TOP_K
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import GPT4All

def load_rag_pipeline():
    embeddings = HuggingFaceEmbeddings(model_name=MODEL_NAME)
    vectorstore = FAISS.load_local("vectorstore", embeddings, allow_dangerous_deserialization=True)
    retriever = vectorstore.as_retriever(kwargs={"k":TOP_K})
    
    #Loading Hugging Face LLM pipeline
    # model_pipeline = pipeline("text2text-generation", model="google/flan-t5-base", max_length=512)
    # llm = HuggingFacePipeline(pipeline=model_pipeline)

    llm = GPT4All(
        model="qwen2.5-coder-7b-instruct-q4_0.gguf",  
        allow_download=True
    )

    return retriever, llm
