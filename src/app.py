import re
import streamlit as st
from src.rag_pipeline import load_rag_pipeline

st.set_page_config(page_title="NAU Smart Campus Assistant", page_icon="🎓")

st.title("🎓 NAU Smart Campus Assistant")
st.write("Ask me anything about Northern Arizona University — admissions, programs, research, and more!")

# Load RAG pipeline
@st.cache_resource
def get_chain():
    return load_rag_pipeline()

retriever, llm = get_chain()

query = st.text_input("Enter your question:")

def is_valid_query(query: str) -> bool:
    """Basic checks to see if the query looks valid."""
    if not query or query.strip() == "":
        return False

    # Check if it's just numbers or symbols
    if not re.search(r'[a-zA-Z]', query):
        return False

    # Too short (e.g., one word or < 3 chars)
    if len(query.split()) < 2:
        return False
    
if query:  
    if not is_valid_query(query):
        st.warning("sorry i cannot assist you with that, please ask me something related to nau") 
    else:
        with st.spinner("Please wait while fetching the data..."):
            retrieved_docs = retriever.invoke(query)
            context = ' '.join([doc.page_content for doc in retrieved_docs])

            prompt = f"""
                        You are a knowledgeable assistant. 
                        Please explain in depth, step by step, using detailed reasoning.

                        Context:a
                        {context}

                        Question: {query}
                        Answer:"""
            answer = llm.invoke(query)
            st.write("**Answer:**", answer)
