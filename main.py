from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI(
    title="Zain Ali - AI/ML Engineer Chatbot",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
    status: str = "success"

@app.get("/")
def root():
    return {
        "service": "Zain Ali - AI/ML Engineer Chatbot",
        "status": "running on Replit",
        "version": "1.0.0"
    }

@app.post("/chat")
def chat(request: ChatRequest):
    message = request.message.lower()
    
    # Your system prompt logic
    relevant_keywords = [
        "chatbot", "ai", "ml", "automation", "rag", "python", 
        "bot", "machine learning", "artificial intelligence",
        "workflow", "hire", "project", "consultation", "service"
    ]
    
    is_relevant = any(keyword in message for keyword in relevant_keywords)
    
    if is_relevant:
        if "chatbot" in message:
            response = "Yes, I create custom AI chatbots for businesses! I specialize in RAG systems. Contact me: zaincode20@gmail.com or WhatsApp: +923062020798"
        elif "automation" in message:
            response = "Absolutely! I create automation workflows using Python and AI. Let me know your requirements!"
        elif "rag" in message:
            response = "RAG systems help chatbots answer questions using your specific documents. I build these regularly."
        elif any(word in message for word in ["hire", "project", "consultation"]):
            response = "I'd be happy to discuss your project! Contact me: zaincode20@gmail.com or WhatsApp: +923062020798"
        else:
            response = "I'm Zain Ali, a Python AI/ML Engineer specializing in AI chatbots, automation workflows, and RAG systems. How can I help?"
    else:
        response = "That's outside my area of focus. I specialize in AI/ML solutions. How can I help you with chatbots, automation, or custom AI development?"
    
    return ChatResponse(response=response)

# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
