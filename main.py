from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model= OllamaLLM(
    model="llama3.2",
    temperature=0.1,
    max_tokens=10000,
)

template="""
You are an expert in answering questions about a pizza restaurant

Here are some relevant reviews: {reviews}

here is the  question to answer: {question}
"""

prompt= ChatPromptTemplate.from_template(template)
chain=prompt | model

while True:
    print("\n\nWelcome to the Pizza Restaurant Q&A!")
    try:
        question = input("Enter your question (or type 'q' to quit): ")
        if question.lower() == 'q':
            break
        reviews = retriever.invoke(question)
        result = chain.invoke({"reviews": reviews,"question": question})
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")

