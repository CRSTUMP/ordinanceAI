import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from embeddings import huggingface_embeddings

current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

new_dir = "C:\\\\Users\\\\Christopher Stump\\\\Documents\\\\analysis\\\\ordinanceAI" # Replace with the actual path
os.chdir(new_dir)
print(f"Changed to directory: {os.getcwd()}")
# Load pdf files in the local directory
loader = PyPDFLoader("ordinances.pdf")

docs_before_split = loader.load()
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap  = 200,
)
docs_after_split = text_splitter.split_documents(docs_before_split)


vectorstore = FAISS.from_documents(docs_after_split, huggingface_embeddings)
vectorstore.save_local("ordinance_index")
