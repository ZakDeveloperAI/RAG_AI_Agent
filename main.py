from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

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
        question = input("Enter your question (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            break
        result = chain.invoke({
            "reviews": "The pizza was great! The crust was crispy and the toppings were fresh. I loved the pepperoni and the cheese was perfectly melted. The service was also excellent, very friendly staff.",
            "question": question
        })
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")

