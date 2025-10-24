import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


#model and embeddings
MODEL_NAME = "gpt-4-turbo"
EMBEDDING_MODEL = "text-embedding-3-small"

#number of chunks to retrieve
TOP_K = 4