# Simple Rule-Based Chatbot using if-else logic

print("🤖 Chatbot: Hi, I'm ChatBot! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    # Exit condition
    if "bye" in user_input:
        print("🤖 Chatbot: Goodbye! Have a great day 😊")
        break

    # Greetings
    elif "hello" in user_input or "hi" in user_input:
        print("🤖 Chatbot: Hello there! How can I help you today?")

    # Asking name
    elif "your name" in user_input:
        print("🤖 Chatbot: I'm ChatBot, your friendly assistant!")

    # Asking how chatbot is doing
    elif "how are you" in user_input:
        print("🤖 Chatbot: I'm just a program, but I'm doing great! What about you?")

    # Responding to time question
    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"🤖 Chatbot: The current time is {current_time}")

    # Responding to date question
    elif "date" in user_input:
        from datetime import date
        today = date.today()
        print(f"🤖 Chatbot: Today's date is {today}")

    # About creator
    elif "who created you" in user_input or "your developer" in user_input:
        print("🤖 Chatbot: I was created by Om Gupta using Python 🐍")

    # Small talk
    elif "what can you do" in user_input:
        print("🤖 Chatbot: I can chat with you, tell the time or date, and keep you company!")

    # Fallback response
    else:
        print("🤖 Chatbot: I'm not sure how to respond to that. Can you rephrase it?")
