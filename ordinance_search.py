from langchain_community.vectorstores import FAISS
from embeddings import huggingface_embeddings

vectorstore = FAISS.load_local("ordinance_index", huggingface_embeddings, allow_dangerous_deserialization = True)
def search_twp(query = """What are the rules around chickens?""", k=3): 
             # Sample question, change to other questions you are interested in.
    relevant_documents = vectorstore.similarity_search(query, k=k)
    result = ""
    for i in range(k):
        output = relevant_documents[i].page_content
        result = result + ' /n ' + output
    return result