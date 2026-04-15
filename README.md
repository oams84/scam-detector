# 🛡️ Scam Detector Web App

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-WebApp-black)
![Status](https://img.shields.io/badge/Status-Live-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 Overview

The **Scam Detector Web App** is a Python-based cybersecurity tool designed to identify phishing, scam messages, and social engineering attempts using rule-based analysis and risk scoring.

The application simulates a **Security Operations Center (SOC)** workflow by analyzing suspicious messages and classifying them into risk categories.

---

## 🌐 Live Demo

👉 Web App:  
https://web-production-ac098.up.railway.app

---

## 🚀 Features

- 🔍 Detects scam and phishing messages using keyword and pattern analysis  
- ⚠️ Risk scoring system (Low Risk / Suspicious / Likely Scam)  
- 🔗 Detects links, urgency language, and financial requests  
- 🧠 Identifies social engineering patterns  
- 📊 Tracks scan history  
- 🖥️ User-friendly web interface  
- 🔌 REST API for integration with other systems  

---

## 🧠 Detection Logic

The tool analyzes messages based on:

- Suspicious keywords (e.g., *verify, password, bank account*)  
- Urgency indicators (e.g., *now, immediately*)  
- Financial triggers (e.g., *payment, transfer, refund*)  
- External links (URLs)  
- Phone number patterns  

Each factor contributes to a **risk score (0–100)** used to classify the message.

---

## 🖥️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/oams84/scam-detector.git
cd scam-detector
```
## 2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```
## 3. Install dependencies
```bash
pip install -r requirements.txt
```
## 4. Run the app
```bash
python app.py
```
## 5. Open in browser
```bash
http://127.0.0.1:5000
```
## 🔌 API Usage
Endpoint
POST /api/analyze
---
Example Request
```bash
curl -X POST https://web-production-ac098.up.railway.app/api/analyze \
-H "Content-Type: application/json" \
-d '{"message":"Your bank account is suspended! Click here to verify: http://fake-bank.com"}'
```
---
```bash
Example Response
{
  "message": "Your bank account is suspended!",
  "verdict": "Likely Scam",
  "risk_score": 82,
  "reasons": [
    "Contains suspicious phrase: 'verify'",
    "Contains suspicious phrase: 'bank account'",
    "Contains a link"
  ]
}
```
--- 
## 📁 Project Structure
```bash
scam_detector/
├── app.py
├── detector.py
├── main.py
├── requirements.txt
├── Procfile
├── templates/
│   ├── index.html
│   └── history.html
├── data/
│   └── history.json
└── README.md
```
---
📊 Key Capabilities
- Real-time scam detection
- Browser-based analysis interface
- Persistent scan history
- API-based integration
- Cloud deployment (Railway)
---

⚠️ Limitations
- Uses rule-based detection (not ML yet)
- History stored locally (may reset on redeploy)
- No user authentication (yet)
---
🔮 Future Improvements
- Machine learning / NLP-based detection
- Database integration (PostgreSQL)
- User authentication system
- Dashboard analytics
- Mobile app integration
- Paid API access (SaaS model)
---
🛠 Technologies Used
- Python 3
- Flask
- HTML / CSS
- JSON
- Gunicorn
- Railway (Deployment)
---
🎯 Skills Demonstrated
- Cybersecurity threat detection
- Web application development (Flask)
- REST API design
- Risk scoring systems
- Cloud deployment
- Secure coding practices
---

📜 License

This project is licensed under the MIT License.

