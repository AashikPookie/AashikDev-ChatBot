def show_welcome():
    print("┌" + "─" * 50 + "┐")
    print("│" + " " * 50 + "│")
    print("│" + " " * 15 + "🤖 AASHIKDEV CHATBOT 🤖" + " " * 15 + "│")
    print("│" + " " * 50 + "│")
    print("│" + " " * 10 + "🚀 Your AI Coding Companion!" + " " * 11 + "│")
    print("│" + " " * 50 + "│")
    print("│" + " " * 8 + "Created by: AashikDev (Age 15)" + " " * 9 + "│")
    print("│" + " " * 50 + "│")
    print("│" + " " * 12 + "Type 'bye' to quit anytime" + " " * 13 + "│")
    print("│" + " " * 50 + "│")
    print("└" + "─" * 50 + "┘")
    print()
    print("🔹 Ask me about: Python, Coding, Motivation, IIT, AI!")
    print("═" * 52)

def show_exit():
    print()
    print("┌" + "─" * 50 + "┐")
    print("│" + " " * 50 + "│")
    print("│" + " " * 12 + "🚀 CHATBOT SESSION ENDED 🚀" + " " * 12 + "│")
    print("│" + " " * 50 + "│")
    print("│" + " " * 10 + "Thanks for chatting with me! 😊" + " " * 10 + "│")
    print("│" + " " * 50 + "│")
    print("│" + " " * 8 + "Remember: Keep Coding, Keep Learning!" + " " * 7 + "│")
    print("│" + " " * 50 + "│")
    print("│" + " " * 12 + "👨💻 Created by: AashikDev" + " " * 13 + "│")
    print("│" + " " * 50 + "│")
    print("│" + " " * 14 + "See you next time! 👋" + " " * 15 + "│")
    print("│" + " " * 50 + "│")
    print("└" + "─" * 50 + "┘")

responses = {
    # 👋 GREETINGS
    "hello": "Hey bro! What's up? Ready to chat? 😄",
    "hi": "Hello there! How can I help you today? 👋",
    "hey": "Yo! What's cooking? 🔥",
    "good morning": "Morning! Hope you have an awesome day ahead! ☀️",
    "good evening": "Evening! How was your day? 🌙",
    
    # 🤖 ABOUT CHATBOT
    "who are you": "I'm AashikDev's AI Chatbot! Created to help and chat! 🤖",
    "what is your name": "I'm ChatBot v1.0, but you can call me BroBot! 😎",
    "who created you": "I was created by AashikDev, a 15-year-old coding legend! 👨💻",
    "what can you do": "I can chat, answer questions, help with coding, and motivate you! 💪",
    
    # 🐍 CODING QUESTIONS
    "what is python": "Python is an awesome programming language! Great for beginners and AI! 🐍",
    "how to learn python": "Start with basics, build projects, and never give up! Practice daily! 💻",
    "python project ideas": "Try: Calculator, Todo list, Weather app, Chatbot (like me!), Game! 🎯",
    "what is github": "GitHub is where developers store and share their code. Like Facebook for coders! 🌐",
    "how to push to github": "git add → git commit → git push! Simple yet powerful! 🚀",
    
    # 🧠 STUDY & MOTIVATION
    "i'm tired": "Take a break bro! Even robots need charging! ⚡ Come back fresh!",
    "motivate me": "You're 15 and building AI projects! You're already ahead of 99%! Keep going! 🏆",
    "how to focus": "Remove distractions, set small goals, use Pomodoro technique! 🍅",
    "exam stress": "Deep breaths! You've prepared well. Trust yourself! You got this! 📚",
    
    # 🎮 FUN & GAMES
    "tell me a joke": "Why do Python programmers prefer dark mode? Because light attracts bugs! 🐛😂",
    "play a game": "Let's play! I'm thinking of a number 1-10. Guess it! 🎲",
    "fun fact": "The first computer bug was an actual insect! A moth stuck in a computer in 1947! 🦋",
    
    # ❤️ FEELINGS
    "i'm sad": "Hey bro, it's okay to feel sad. Want to talk about it? I'm here for you! ❤️",
    "i'm happy": "That's awesome! Share that happiness with others! Spread good vibes! ✨",
    "i'm bored": "Let's code something! Boredom is just creativity waiting to happen! 💡",
    
    # 🏆 FUTURE GOALS
    "iit preparation": "Focus on basics, practice consistently, and believe in yourself! IIT is possible! 🎓",
    "ai engineer": "Great goal! Start with Python, learn math, build projects. You're on the right path! 🤖",
    "start a company": "Start small, solve real problems, and never stop learning! Future CEO! 🏢",
    
    # 📱 TECHNOLOGY
    "best programming language": "Python for beginners, JavaScript for web, C++ for performance! Choose based on goals! 🎯",
    "how to build an app": "Learn basics → Choose platform (Android/iOS/Web) → Build simple → Improve! 📱",
    "what is ai": "Artificial Intelligence is machines learning to think and act like humans! It's the future! 🧠",
    
    # 🍕 PERSONAL
    "your favorite food": "I don't eat, but I hear pizza is everyone's favorite! 🍕",
    "do you sleep": "Nope! I'm always awake and ready to chat! 24/7 service! ⏰",
    "are you human": "I'm AI, but created with human awesomeness! Best of both worlds! 🤖❤️",
    
    # 👋 GOODBYES
    "bye": "See you later! Keep coding and dreaming big! 👋",
    "goodbye": "Take care! Come back anytime you need help! 🫂",
    "exit": "Shutting down... but I'll be here when you return! 💤",
    "quit": "Alright! Remember: Every expert was once a beginner. Keep going! 🚀",
    
    # 🔧 DEFAULT RESPONSE
    "default": "Hmm, I'm still learning! Can you ask that differently? Or ask me about coding, studies, or motivation! 😊"
}

def bot(userquestion):
    userquestion = userquestion.lower()
    for each in responses:
        if each in userquestion:
            return responses[each]
    return responses["default"]  # Using the default response from dictionary

# ========== CALLING THE FUNCTIONS ==========
show_welcome()  # This calls the welcome function at the start

while True:
    userquestion = input("Please ask your questions: ") 
    reply = bot(userquestion) 
    print("Bot Responses:", reply)
    print("═" * 52)  # Separator line
    
    # Check for exit conditions
    if any(exit_word in userquestion.lower() for exit_word in ["bye", "goodbye", "exit", "quit"]):
        show_exit()  # This calls the exit function
        break

