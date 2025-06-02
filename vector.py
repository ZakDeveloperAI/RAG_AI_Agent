from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df= pd.read_csv("realistic_restaurant_reviews.csv")
embeddings= OllamaEmbeddings(model="mxbai-embed-large")

db_location= "./chrome_langchain_db"
add_documents= not os.path.exists(db_location)

if add_documents:
    documents=[]
    ids=[]
    
    for i, row in df.iterrows():
        document=Document(
            page_content=row['Title']+" "+row['Review'],
            metadata={"rating": row['Rating'], "date": row['date']},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document) 
        
vector_