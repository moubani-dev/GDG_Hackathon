import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_message(message, language="English"):

    prompt = f"""
You are ScamShield AI, an AI-powered digital safety assistant.

Analyze the following message for potential scam indicators.

MESSAGE:
{message}

RESPONSE LANGUAGE:
{language}

Return ONLY valid JSON.

Use exactly this structure:

{{
    "risk_score": 0,
    "risk_level": "LOW",
    "scam_category": "Unknown",
    "signals": [],
    "evidence": [],
    "manipulation_tactics": [],
    "safe_actions": [],
    "emergency_guidance": false
}}

Rules:

- risk_score must be a number from 0 to 100.
- risk_level must be one of:
  LOW, MEDIUM, HIGH, CRITICAL
- scam_category should describe the likely scam type.
- signals should contain suspicious indicators.
- evidence should contain specific parts or patterns from the message.
- manipulation_tactics should explain psychological techniques such as urgency, fear, authority, reward, etc.
- safe_actions should contain practical safety steps.
- emergency_guidance should be true only when the situation may require immediate protective action.
- Do not claim that something is definitely a scam unless the evidence supports that conclusion.
- Do not invent facts that are not present in the message.
- Keep the language simple.
- Return ONLY JSON. No markdown. No explanation outside JSON.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    try:
        return json.loads(response.text)
    except json.JSONDecodeError:
        return {
            "risk_score": 0,
            "risk_level": "UNKNOWN",
            "scam_category": "Unable to analyze",
            "signals": [],
            "evidence": [],
            "manipulation_tactics": [],
            "safe_actions": [],
            "emergency_guidance": False,
            "raw_response": response.text
        }
   
def analyze_screenshot(image_bytes, mime_type, language="English"):

    prompt = f"""
You are ScamShield AI, an AI-powered digital safety assistant.

Analyze this screenshot for potential scam indicators.

The screenshot may contain:
- SMS
- WhatsApp messages
- Emails
- UPI/payment requests
- Banking messages
- Links
- Fraud attempts

Response language:
{language}

Return ONLY valid JSON.

Use exactly this structure:

{{
    "risk_score": 0,
    "risk_level": "LOW",
    "scam_category": "Unknown",
    "signals": [],
    "evidence": [],
    "manipulation_tactics": [],
    "safe_actions": [],
    "emergency_guidance": false
}}

Rules:
- risk_score must be a number from 0 to 100.
- risk_level must be LOW, MEDIUM, HIGH, or CRITICAL.
- Do not claim certainty when evidence is insufficient.
- Do not invent information.
- Keep the explanation simple.
- Return ONLY JSON.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=[
            prompt,
            types.Part.from_bytes(
                data=image_bytes,
                mime_type=mime_type
            )
        ]
    )

    try:
        return json.loads(response.text)

    except json.JSONDecodeError:
        return {
            "risk_score": 0,
            "risk_level": "UNKNOWN",
            "scam_category": "Unable to analyze",
            "signals": [],
            "evidence": [],
            "manipulation_tactics": [],
            "safe_actions": [],
            "emergency_guidance": False,
            "raw_response": response.text
        }