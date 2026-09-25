from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from gemini_service import analyze_message, analyze_screenshot


app = FastAPI(
    title="ScamShield AI API",
    description="AI-powered scam detection backend",
    version="1.0"
)


# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AnalyzeRequest(BaseModel):
    message: str
    language: str = "English"


@app.get("/")
def home():
    return {
        "status": "online",
        "message": "ScamShield AI backend is running"
    }


@app.post("/analyze")
def analyze(request: AnalyzeRequest):

    if not request.message.strip():
        return {
            "error": "Please provide a message to analyze."
        }

    result = analyze_message(
        request.message,
        request.language
    )

    return result

@app.post("/analyze-screenshot")
async def analyze_screenshot_endpoint(
    file: UploadFile = File(...),
    language: str = Form("English")
):

    image_bytes = await file.read()

    result = analyze_screenshot(
        image_bytes,
        file.content_type,
        language
    )

    return result