from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

RESPONSES = {
    "coding": [
        "Great question about coding! Remember, the best way to learn is by doing. Try breaking the problem into smaller parts.",
        "When debugging, always check your logic step by step. Print statements are your friend!",
        "Keep practicing! Every expert was once a beginner. Consistency is key in programming.",
        "Have you tried searching the documentation? It's often the best resource for understanding how things work.",
        "Don't forget to take breaks! Sometimes stepping away helps you see the solution clearly."
    ],
    "motivation": [
        "You've got this! Every line of code you write makes you a better developer.",
        "Remember, even the best programmers started somewhere. Keep pushing forward!",
        "Challenges are just opportunities in disguise. You're learning with every mistake!",
        "Stay curious and never stop learning. That's the secret to success in tech!",
        "Believe in yourself! Your potential is unlimited."
    ],
    "study": [
        "Try the Pomodoro technique: 25 minutes of focused study, then a 5-minute break.",
        "Create flashcards for concepts you want to remember. Active recall is powerful!",
        "Teach what you learn to someone else. It's the best way to solidify knowledge.",
        "Set clear goals for each study session. What do you want to accomplish today?",
        "Make sure you're getting enough sleep. Your brain consolidates learning while you rest!"
    ],
    "jokes": [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "There are only 10 types of people in the world: those who understand binary and those who don't!",
        "Why did the programmer quit his job? Because he didn't get arrays (a raise)!",
        "A SQL query walks into a bar, walks up to two tables and asks, 'Can I join you?'",
        "Why do Java developers wear glasses? Because they can't C#!"
    ],
    "greeting": [
        "Hey there! I'm AashikDev ChatBot, your AI coding companion! How can I help you today?",
        "Hello! Welcome! I'm here to help with coding, motivation, study tips, and more!",
        "Hi! Great to see you! What would you like to chat about today?"
    ],
    "default": [
        "That's interesting! Tell me more about what you're working on.",
        "I'm here to help! You can ask me about coding, motivation, study tips, or just ask for a joke!",
        "Hmm, let me think about that. In the meantime, is there something specific I can help you with?",
        "Thanks for sharing! Feel free to ask me anything about coding or just chat!"
    ]
}

def get_response(message):
    message_lower = message.lower()
    
    if any(word in message_lower for word in ["hello", "hi", "hey", "greetings"]):
        return random.choice(RESPONSES["greeting"])
    elif any(word in message_lower for word in ["code", "coding", "program", "debug", "error", "bug", "python", "javascript"]):
        return random.choice(RESPONSES["coding"])
    elif any(word in message_lower for word in ["motivate", "motivation", "inspire", "encourage", "sad", "stuck"]):
        return random.choice(RESPONSES["motivation"])
    elif any(word in message_lower for word in ["study", "learn", "tips", "focus", "exam", "homework"]):
        return random.choice(RESPONSES["study"])
    elif any(word in message_lower for word in ["joke", "funny", "laugh", "humor"]):
        return random.choice(RESPONSES["jokes"])
    else:
        return random.choice(RESPONSES["default"])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    bot_response = get_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
