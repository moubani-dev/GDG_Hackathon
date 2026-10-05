from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from gemini_service import analyze_message, analyze_screenshot


app = FastAPI(
    title="ScamShield AI API",
    description="AI-powered scam detection backend",
    version="1.0"
)

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "ScamShield AI"
    }
    



# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "https://scamshield-ai-shud.onrender.com"
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

    try:
        result = analyze_message(
            request.message,
            request.language
        )

        return result

    except Exception as e:
        print(f"Gemini analysis error: {e}")

        return {
            "error": "AI analysis is temporarily unavailable. Please try again shortly."
        }

@app.post("/analyze-screenshot")
async def analyze_screenshot_endpoint(
    file: UploadFile = File(...),
    language: str = Form("English")
):
    # Check file type
    allowed_types = ["image/png", "image/jpeg", "image/jpg"]

    if file.content_type not in allowed_types:
        return {
            "error": "Please upload a PNG or JPEG image."
        }

    # Read file
    image_bytes = await file.read()

    # Limit file size to 5 MB
    max_size = 5 * 1024 * 1024

    if len(image_bytes) > max_size:
        return {
            "error": "Image is too large. Please upload an image smaller than 5 MB."
        }

    if not image_bytes:
        return {
            "error": "The uploaded image is empty."
        }

    # Analyze with Gemini
    try:
        result = analyze_screenshot(
            image_bytes,
            file.content_type,
            language
        )

        return result

    except Exception as e:
        print(f"Gemini screenshot analysis error: {e}")

        return {
            "error": "AI screenshot analysis is temporarily unavailable. Please try again shortly."
        }
