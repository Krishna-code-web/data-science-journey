from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

model = ChatMistralAI(model="mistral-small-2506", temperature=0.9)
response = model.invoke("Write a poem on AI?")
print(response.content)
