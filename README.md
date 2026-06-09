# 🚀 ProJournal — AI-Powered Journaling Vault

ProJournal is a modern, premium, and highly secure Single Page Application (SPA) journaling platform engineered for developers. It integrates **Google Gemini AI (via the latest `google-genai` SDK)** to dynamically analyze the emotional tone of journal entries, auto-assigning contextual mood badges. 

The application features secure local authentication alongside enterprise-grade social logins using Google OAuth, state-of-the-art Single-Page AJAX OTP verification for account recovery, and a beautiful fluid user experience engineered using **Django, Tailwind CSS, and Alpine.js**.

---

## ✨ Core Features

- **🧠 Gemini 2.5 Flash Integration**: Real-time contextual semantic analysis of your journal text using Google's latest official `google-genai` SDK package.
- **🔒 Production-Grade Security**: Decoupled environment architecture utilizing standalone `.env` file mapping to protect private keys and API credentials.
- **🔑 Google OAuth 2.0 Single Sign-On (SSO)**: Seamless social authentication layer built using `django-allauth`.
- **✉️ Single-Page AJAX OTP Reset**: Premium Instagram/Swiggy style modern account recovery flow driven by background sessions and Alpine.js asynchronously, avoiding traditional clunky page reloads.
- **📱 Premium UX/UI Layout**: High-fidelity responsive dashboard, auto-expanding distraction-free notion-style editor, fluid sidebar profiles, and secure account status metrics.

---

## 🛠️ Tech Stack & Architecture

- **Backend Framework**: Django 5.x / 6.x (Python 3.11+)
- **AI Core Layer**: Google GenAI SDK (`gemini-2.5-flash`)
- **Frontend Engine**: Tailwind CSS (JIT Engine) & Alpine.js (Reactive Core)
- **Database Layer**: SQLite / PostgreSQL (Managed via Django ORM)
- **Mailing Protocol**: Gmail SMTP Security Protocol over TLS (Port 587)

---

## 💿 Installation & Local Setup

Follow these linear step-by-step instructions precisely to configure your local virtual environment, setup secrets, inject Google API clients, and initiate migrations.

### Step 1: Clone the Repository & Navigate
```bash
git clone [https://github.com/your-username/pro-journal.git](https://github.com/your-username/pro-journal.git)
cd pro-journal
```
on window (command prompt)

python -m venv venv
.\venv\Scripts\activate

on macOS/LINUX

python3 -m venv venv 
source venv/bin/activate

**Production dependencies:**
__________________________
pip install -r requirements.txt
________________________


# ----------------------------------------------------
# 🪐 DATABASE & DJANGO CORE CONFIGURATIONS
# ----------------------------------------------------
SECRET_KEY=django-insecure-your-custom-production-hash-key-here
DEBUG=True

# ----------------------------------------------------
# 🔑 GOOGLE OAUTH CLIENT CREDENTIALS (SSO)
# ----------------------------------------------------
# Generated from Google Cloud Console (APIs & Services -> Credentials)
GOOGLE_CLIENT_ID=your-long-apps-google-client-id-here.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=GOCSPX-your-google-client-secret-string-here

# ----------------------------------------------------
# 🧠 GOOGLE GEMINI AI CONFIGURATION 
# ----------------------------------------------------
# Essential for the modern google-genai SDK engine
GEMINI_API_KEY=AIzaSyYourActualGoogleGeminiDeveloperKeyHere

# ----------------------------------------------------
# ✉️ AUTOMATED SECURITY MAILING (GMAIL SMTP PROTOCOL)
# ----------------------------------------------------
EMAIL_USER=your-registered-gmail-account@gmail.com
EMAIL_PASS=abcdefghijklmnop  # 16-Digit App Password (NOT your normal account password)


​🚀 Database Migrations & Initial Server Launch


# Verify system integrity and generate Django migrations blueprints
python manage.py makemigrations

# Apply system architectures and tables to your local workspace
python manage.py migrate

# Boot up the application server locally
python manage.py runserver

**SYSTEM Folder Structure**
pro_journal/
│
├── pro_journal/            # Project Settings Configurations Module
│   ├── settings.py         # Configured dynamically to read from load_dotenv()
│   ├── urls.py             # Global route maps
│   └── wsgi.py
│
├── journal/                # Core application module
│   ├── ai_service.py       # google-genai Client Engine wrapper (gemini-2.5-flash)
│   ├── models.py           # Entry structural blueprint mapping Title, Content, and Mood Tag
│   ├── views.py            # Dashboard processors & AJAX OTP backend validators
│   └── urls.py
│
├── templates/              # Fluid Interface Core Layouts
│   ├── base.html           # High-fidelity navigation bar with interactive Alpine profile dropdown
│   └── accounts/
│       ├── register.html   # Ultra-compact 2-column register setup with validation filters
│       ├── login.html      # Secure authorization node
│       └── forgot_password.html # Single Page SPA OTP-based recovery node
│
├── .env                    # Decoupled Local Secrets Matrix [RESTRICTED]
├── .gitignore              # Configured with explicit blocks to block tracking on .env & venv/
└── manage.py

---

## 👨‍💻 Developer & Creator

This entire ecosystem—from the secure Django backend and Google Gemini AI integrations to the premium Tailwind/Alpine frontend—was designed and built from scratch by:

**Surendra Pratap Vishwakarma**
- **Role:** Backend & Full-Stack Developer
- **Tech Focus:** Django, AI Integrations (Google GenAI), Workflow Automation

*Built with passion, clean code, and AI intelligence.* 🚀
