 # 🛡️ ScamShield AI

### AI-Powered Scam Detection & Digital Safety Assistant

**ScamShield AI** is an AI-powered digital safety assistant designed to help people identify and understand online scams before they take action.

From fake KYC messages and phishing attempts to UPI fraud, fake job offers, prize scams, and impersonation messages, ScamShield AI analyzes suspicious content and explains **why it may be dangerous** in simple, understandable language.

> **Before you click. Before you pay. Check with ScamShield AI.**

---

## 🚨 Why ScamShield AI?

Online scams are becoming increasingly convincing. Scammers often create a sense of urgency, fear, or excitement to make people act without thinking.

Messages such as:

- "Your KYC has expired."
- "Your bank account will be blocked."
- "You have won a prize!"
- "Click this link to claim your reward."
- "Your job application has been selected."

may look legitimate at first glance.

ScamShield AI helps users pause, analyze the message, understand the manipulation tactics being used, and make a safer decision.





---

## ✨ Key Features

### 🔍 AI Scam Scanner

Paste a suspicious SMS, WhatsApp message, email, or UPI-related message and let the AI analyze it.

The system provides:

- Scam risk score
- Risk category
- Suspicious signals
- Supporting evidence
- Recommended safety actions

---

### 📸 Screenshot Analysis

Users can upload a screenshot of a suspicious message.

ScamShield AI analyzes the content and identifies potential scam indicators without requiring the user to manually type the entire message.

---

### 🧠 Explain the Trap

Instead of simply saying **"This is a scam"**, ScamShield AI explains **how the scam works**.

It highlights common psychological manipulation techniques such as:

- Fear and urgency
- Threats of account blocking
- Fake authority
- Reward-based manipulation
- Social engineering

This helps users recognize similar scams in the future.

---

### 🚨 Emergency Mode

If a user has already clicked a suspicious link, shared information, or transferred money, Emergency Mode provides immediate safety guidance.

It focuses on practical next steps that can help the user respond quickly.

---

### 🌐 Multilingual Support

ScamShield AI is designed to make digital safety more accessible by supporting:

- 🇬🇧 English
- 🇮🇳 Hindi
- বাংলা Bengali

The goal is to make scam awareness understandable beyond English-speaking users.

---

### 📄 Incident Report

Users can generate a structured incident report containing relevant information about a detected scam.

This can help users organize the details of an incident for further reporting or documentation.

---

## 🧩 How It Works

```text
User Input
    ↓
Message / Screenshot
    ↓
ScamShield AI
    ↓
AI Analysis
    ↓
Risk Assessment
    ↓
Suspicious Signals + Evidence
    ↓
Explain the Trap
    ↓
Recommended Safety Actions
```

The system combines a web interface, backend API, and AI-powered analysis to provide an end-to-end scam detection experience.

---

## 🏗️ System Architecture

```text
                ┌─────────────────────┐
                │       User          │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   ScamShield AI     │
                │     Frontend        │
                └──────────┬──────────┘
                           │
                    API Request
                           │
                           ▼
                ┌─────────────────────┐
                │      FastAPI        │
                │      Backend        │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │     Gemini AI       │
                │   Scam Analysis     │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Risk + Evidence +   │
                │ Safety Explanation  │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │      User UI        │
                └─────────────────────┘
```

---

## 🛠️ Tech Stack

### Frontend
- HTML
- CSS
- JavaScript
- Responsive web interface

### Backend
- Python
- FastAPI
- Uvicorn
- REST API
- CORS

### AI
- Google Gemini API
- Prompt-based scam analysis
- Multilingual response generation

### Deployment
- Render
- GitHub

---

## 📁 Project Structure

```text
ScamShield-AI/
│
├── assets/
│   └── scam_girl.png
│
├── data/
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── app.py
├── backend.py
├── emergency.py
├── gemini_service.py
├── prompts.py
├── report.py
├── test_gemini.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/moubani-dev/GDG_Hackathon.git
cd GDG_Hackathon/ScamShield-AI
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

**Never commit your API key to GitHub.**

### 5. Start the backend

```bash
python3 -m uvicorn backend:app --reload
```

The backend will run on:

```text
http://127.0.0.1:8000
```

### 6. Start the frontend

Open another terminal:

```bash
cd frontend
python3 -m http.server 5500
```

Then open:

```text
http://localhost:5500
```

---

## 🔐 Security & Privacy

ScamShield AI is designed as a scam-awareness and educational tool.

Users should **not share sensitive information**, including:

- Passwords
- OTPs
- PINs
- CVV numbers
- Banking credentials
- Private keys

The AI's output should be treated as guidance rather than a guaranteed determination of whether a message is fraudulent.

---

## 🎯 Use Cases

ScamShield AI can help users analyze:

- 🏦 Fake banking/KYC messages
- 💳 UPI fraud attempts
- 📱 SMS phishing
- 💬 WhatsApp scams
- 🎁 Fake prize notifications
- 💼 Job and recruitment scams
- 👤 Impersonation attempts
- 🔗 Suspicious links
- 🚨 Urgent payment requests

---

## 💡 What Makes ScamShield AI Different?

Many scam detection tools simply tell users whether something is **safe or unsafe**.

ScamShield AI focuses on **understanding the scam**.

Instead of only asking:

> **"Is this a scam?"**

the system also helps answer:

> **"Why is this suspicious?"**  
> **"What psychological trick is being used?"**  
> **"What should I do next?"**

This makes the platform not only a detection tool, but also a **digital safety education assistant**.

---

## 🔮 Future Improvements

Potential future improvements include:

- Real-time browser/link analysis
- Voice-based scam detection
- WhatsApp integration
- Email integration
- Phone-call scam detection
- More regional languages
- Scam trend analytics
- Community-driven scam reporting
- Integration with official cybercrime reporting systems

---

🖥️ ScamShield AI Dashboard

<img width="1440" height="812" alt="image" src="https://github.com/user-attachments/assets/be452310-1c1b-4b4b-80f5-00b646eae411" />


## 🏆 Project Goal

The goal of ScamShield AI is simple:

**Help people stop for a moment before trusting a suspicious message, clicking a link, or making a payment.**

With AI-powered analysis and clear explanations, the project aims to make digital safety more accessible to everyday users.

---

## 👩‍💻 Built For

**Hackathon Project — ScamShield AI**

Built with:

**Python • FastAPI • JavaScript • Gemini AI • HTML • CSS • Render**

---

## 📌 Disclaimer

ScamShield AI is an AI-assisted awareness tool and does not guarantee that a message is fraudulent or legitimate.

Always verify suspicious requests through the organization's official website, application, or verified customer-support channels before taking action.

---

### 🛡️ ScamShield AI

**Detect. Understand. Protect.**

> **Before you click. Before you pay.**
> **Think twice. Check with ScamShield AI.**
