# AI-Powered Ticket Triage & Alerting System

An AI-driven support ticket automation system built using n8n and Google Gemini API to classify support requests, assign priorities, and trigger automated alerts for critical issues.

---

# 🚀 Features

- Automatic ticket classification using Google Gemini API
- Categorizes tickets into:
  - Bug
  - Billing
  - Feature Request
  - Other
- Assigns priority levels:
  - Low
  - Medium
  - High
- Event-driven workflow using Webhooks
- Real-time email alerts for high-priority incidents
- Structured JSON output generation
- Custom JavaScript parsing and fallback handling
- Dynamic ticket ID and timestamp generation
- Clean HTML-based email notifications

---

# 🏗️ Workflow Architecture

```text
Webhook → Gemini API → Merge → Code Processing → IF Decision → Email Alert / Response

🛠️ Tech Stack
n8n
Google Gemini API
JavaScript
REST APIs
Webhooks
JSON Processing
Gmail Automation

Sample Input
{
  "subject": "App crash",
  "description": "Application crashes during login"
}

Sample Output
{
  "subject": "App crash",
  "description": "Application crashes during login",
  "category": "bug",
  "priority": "high",
  "summary": "Application crashes during login"
}


High Priority Email Alert
The system automatically sends formatted HTML email alerts for high-severity tickets including:
Ticket ID
Timestamp
Subject
Description
Category
Priority
Summary


Key Implementations:
AI response parsing and JSON cleanup
Fault-tolerant fallback handling for malformed AI responses
Priority-based decision routing
Dynamic expression handling in n8n
HTML email formatting for operational readability


📂 Project Structure
ai-ticket-triage-system/
│
├── workflows/
│   └── ticket-triage-workflow.json
│
├── screenshots/
│   ├── workflow.png
│   ├── email-alert.png
├── ├── postman.png
│
├── sample-data/
│   └── sample-ticket.json
│
└── README.md

⚙️ Setup Instructions

1. Clone Repository
git clone <your-repo-url>


2. Start n8n
docker run -it --rm \
-p 5678:5678 \
-v n8n_data:/home/node/.n8n \
docker.n8n.io/n8nio/n8n


3. Import Workflow
Open n8n
Import workflow JSON from workflows/

4. Configure Credentials
Add:
Google Gemini API Key
Gmail OAuth Credentials
5. Execute Workflow


Send POST request to webhook endpoint:

POST /webhook/ticket
🔮 Future Improvements
Persistent ticket storage using Google Sheets or database
Slack / Teams integration
Retry mechanism for failed API calls
Dashboard for ticket analytics
Multi-agent ticket routing



📌 Learning Outcomes
This project helped in understanding:
AI-powered workflow automation
Event-driven architecture
API integration
JSON parsing and transformation
Workflow orchestration using n8n
Real-time alerting systems


📧 Author
Sudheer Sunkari
