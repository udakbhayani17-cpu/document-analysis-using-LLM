# DocMind — AI PDF Analyzer

A full-stack AI-powered PDF analyzer built with Flask + Claude AI.

## Features
- 📝 Document Summary
- 🔑 Key Points Extraction
- 🎭 Sentiment & Tone Analysis
- 💬 AI Chat Assistant (context-aware with your PDF)
- 🌙 Dark / Light mode toggle
- 📋 Copy to clipboard
- 🖱 Drag & drop PDF upload

---

## Run Locally

### 1. Clone / download this project

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set your API key
```bash
# Mac/Linux
export ANTHROPIC_API_KEY=your_key_here

# Windows
set ANTHROPIC_API_KEY=your_key_here
```

Get your API key at: https://console.anthropic.com

### 4. Run the app
```bash
python app.py
```

Open http://localhost:5000 in your browser.

---

## Deploy on Render (Free)

1. Push this project to a GitHub repository
2. Go to https://render.com and sign up free
3. Click **New → Web Service**
4. Connect your GitHub repo
5. Set these settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
6. Add environment variable:
   - Key: `ANTHROPIC_API_KEY`
   - Value: your API key from https://console.anthropic.com
7. Click **Deploy** — your app will be live in ~2 minutes!

---

## Deploy on Railway (Free tier)

1. Go to https://railway.app
2. Click **New Project → Deploy from GitHub**
3. Connect your repo
4. Add environment variable `ANTHROPIC_API_KEY`
5. Railway auto-detects the Procfile and deploys!

---

## Deploy on Replit

1. Go to https://replit.com and create a new Repl
2. Choose **Import from GitHub** and paste your repo URL
3. In the Secrets tab, add `ANTHROPIC_API_KEY`
4. Click **Run** — Replit will install deps and start the server

---

## Project Structure
```
pdf-analyzer/
├── app.py              # Flask backend + API routes
├── requirements.txt    # Python dependencies
├── Procfile            # For Render/Railway deployment
├── .env.example        # Environment variable template
├── README.md           # This file
└── templates/
    └── index.html      # Full frontend (HTML + CSS + JS)
```

---

## API Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Serve the frontend |
| `/analyze` | POST | Run summary/keypoints/sentiment analysis |
| `/chat` | POST | Multi-turn AI chat with optional PDF context |

---

## Tech Stack
- **Backend:** Python, Flask, Gunicorn
- **AI:** Anthropic Claude (claude-sonnet-4-20250514)
- **Frontend:** Vanilla HTML/CSS/JS (no framework needed)
- **Fonts:** Syne + Inter (Google Fonts)
