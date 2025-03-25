from ordinance_search import search_twp
from config import config
from llm import llm

def chat_twp(query, mode = 'search'):
    
    chat_config = config[mode]
    search_result = search_twp(query, k = chat_config['k'])
    
    messages = [
        ("system", "You are a helpful ordinance analysis tool."),
        ("human", chat_config['prefix'] + search_result + chat_config['suffix']),
    ]
    return(print(llm.invoke(messages).content))
    