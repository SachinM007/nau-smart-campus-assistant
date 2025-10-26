# 🎓 NAU Smart Campus Assistant

An AI-powered Retrieval-Augmented Generation (RAG) chatbot for Northern Arizona University.
It retrieves and summarizes real information from NAU websites.

## 🧠 Tech Stack
- LangChain
- OpenAI GPT-4
- FAISS Vector Database
- Streamlit UI

## 🚀 Run Locally
1. Clone repo  
2. Install dependencies  
   ```bash
   pip install -r requirements.txt

3. Export your OpenAI key
export OPENAI_API_KEY="your-api-key"

4. Build vectorstore
python app/data_loader.py

5. Run Streamlit
streamlit run app/app.py

