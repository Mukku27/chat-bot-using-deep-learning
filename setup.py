import os

# Define the directory structure
directories = [
    "chatbot-app/",
    "chatbot-app/backend/",
    "chatbot-app/frontend/",
    "chatbot-app/frontend/public/",
    "chatbot-app/frontend/src/",
    "chatbot-app/frontend/src/components/",
    "chatbot-app/backend/chat_bot_model/"
]

# Define the files (without content)
files = [
    "chatbot-app/backend/app.py",
    "chatbot-app/backend/intents.json",
    "chatbot-app/frontend/public/index.html",
    "chatbot-app/frontend/src/App.js",
    "chatbot-app/frontend/src/index.js",
    "chatbot-app/frontend/src/index.css",
    "chatbot-app/frontend/src/tailwind.config.js",
    "chatbot-app/README.md",
    "chatbot-app/.gitignore"
]

# Create the directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Create the empty files
for filepath in files:
    open(filepath, 'a').close()

print("Directories and files created successfully!")
