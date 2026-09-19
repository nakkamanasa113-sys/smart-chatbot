print("🤖 Chatbot: Hello! Type 'exit' to stop.")

while True:
    user = input("You: ").lower()

    if "hello" in user:
        print("🤖 Chatbot: Hi there! 👋")

    elif "how are you" in user:
        print("🤖 Chatbot: I'm doing great 😊")

    elif "name" in user:
        print("🤖 Chatbot: I am your Smart Chatbot 🤖")

    elif "help" in user:
        print("🤖 Chatbot: You can say hello, ask my name, ask time, or type exit.")

    elif "time" in user:
        import datetime
        print("🤖 Chatbot:", datetime.datetime.now().strftime("%H:%M:%S"))

    elif "bye" in user or "exit" in user:
        print("🤖 Chatbot: Goodbye 👋")
        break

    else:
        print("🤖 Chatbot: Sorry, I didn't understand 😅")
