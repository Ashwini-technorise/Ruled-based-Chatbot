# basic rule-based chatbot
def chatbot():
    while True:
        user = input("You: ").lower()
        if user == "hello":
            print("Bot: Hii!")
        elif user == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user == "bye":
            print("Bot: Goodbye, Have a nice day!")
            break
        else:
            print("Bot: I don't understand.")

chatbot()