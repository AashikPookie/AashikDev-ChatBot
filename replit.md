# AashikDev ChatBot

## Overview
AashikDev ChatBot is an AI coding companion - a Python-based conversational chatbot that helps with coding questions, motivation, study tips, and programming jokes.

## Project Architecture

### Tech Stack
- **Backend**: Python 3.11 with Flask
- **Frontend**: HTML, CSS, JavaScript
- **Template Engine**: Jinja2

### Directory Structure
```
/
├── main.py              # Flask application entry point
├── templates/
│   └── index.html       # Chat interface template
├── static/
│   ├── style.css        # Styling for the chat interface
│   └── script.js        # Client-side chat functionality
├── README.md            # Project description
└── replit.md            # This file
```

### Key Features
- Interactive chat interface
- Responses for: coding help, motivation, study tips, jokes
- Real-time message sending and receiving
- Responsive design

### Running the Application
The application runs on port 5000. Start it with:
```
python main.py
```

### API Endpoints
- `GET /` - Serves the chat interface
- `POST /chat` - Accepts JSON with `message` field, returns bot response

## Recent Changes
- December 19, 2025: Initial setup with Flask web interface
