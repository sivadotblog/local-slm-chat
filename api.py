from fastapi import FastAPI
from pydantic import BaseModel
import openai

app = FastAPI()

# Define the request body
class ChatRequest(BaseModel):
    query: str
    meta: str

# Initialize the OpenAI API
openai.api_key = "your_openai_api_key"

@app.post("/chat")
async def chat(request: ChatRequest):
    # Use the microsoft phi3.5 medium model to generate a response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Meta: {request.meta}\nQuery: {request.query}",
        max_tokens=150
    )
    return {"response": response.choices[0].text.strip()}
