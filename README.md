# Internship-Project

🔐 Cybersecurity Projects Portfolio
1. Web Application Vulnerability Scanner
2. Ethical Phishing Simulation Platform
📌 Overview

This repository contains two cybersecurity-focused projects designed to demonstrate practical skills in web security testing and user awareness simulation. These projects align with real-world penetration testing and ethical hacking practices.

🛡️ 1. Web Application Vulnerability Scanner
🎯 Objective

To build a Python-based scanner that detects common web application vulnerabilities based on the OWASP Top 10.

🚀 Features
Detects vulnerabilities like:
Cross-Site Scripting (XSS)
SQL Injection (SQLi)
CSRF
IDOR
Insecure Data Exposure
Crawls web pages and extracts input fields
Injects payloads and analyzes responses
Generates structured scan results
User-friendly Flask-based UI
Export reports (HTML/PDF)
🛠️ Tools & Technologies
Python
Flask
Requests
BeautifulSoup
Regex
OWASP Top 10
⚙️ How It Works
User enters target URL
Scanner crawls web pages
Extracts forms and parameters
Injects malicious payloads
Analyzes responses for vulnerability patterns
Displays results in dashboard
▶️ How to Run
pip install -r requirements.txt
python app.py

🎣 2. Ethical Phishing Simulation Platform
🎯 Objective

To simulate phishing attacks in a controlled environment for educational and awareness purposes.

🚀 Features
Custom phishing page templates
Login credential capture (for simulation only)
Admin dashboard to view results
Tracks user interaction (clicks, submissions)
Educational use only
🛠️ Tools & Technologies
Python
Flask
HTML/CSS
JavaScript
SQLite / File-based storage
⚙️ How It Works
Admin launches phishing simulation
Users are presented with a phishing page
Inputs are captured and logged
Admin views results in dashboard
Used for awareness training
▶️ How to Run
pip install -r requirements.txt
python app.py

🔍 Use Cases
Cybersecurity learning and practice
Penetration testing demonstration
Awareness training for phishing attacks
Academic and internship projects

👨‍💻 Author

Sri Jnaneswari Dasina
Cybersecurity Enthusiast | Ethical Hacking Learner

⭐ Future Enhancements
Advanced vulnerability detection (RCE, SSRF)
Real-time scanning dashboard
Email phishing campaign simulation
Improved UI/UX
Integration with security tools
