import nltk
from nltk.chat.util import Chat,reflections
patterns=[
    (r'hi|hello|hey',
     ['Hello!','Hi there!','Hey!' ]),
    (r'how are you?',
     ['I am good,thank you !',"I am fine,how about you?"]),
    (r'what is your name?',
     ['my name is chatbot!']),
    (r'what can you do for me ?',
     ["I can chat with you and provide information. Just ask me anything!"]),
    ( r'how old are you ?',
     ["I'm just a program, so I don't have an age."]),
    ( r'who created you ?',
     ["I was created by human."]),
    (r'where do you live?',
     ["I am a virtual bot, so I don't have a physical location."]),
    (r'how is weather right now?',
     ["I'm not sure, but I can check online for you."]),
    ( r'quit|bye|goodbye',
     ["Bye! Take care.", "Goodbye, have a great day!", "See you later!"]),
    (r'sorry|apologize',
        ["It's okay, no need to apologize.", "No worries!", "Don't mention it."]),
    (r' I am happy',
        ["That's wonderful to hear!", "I'm glad you're happy.", "It's always great to feel joyful."]),
    (r'thank you|thanks',
        ["You're welcome!", "No problem!", "Glad I could assist."]),
    (r'I need help',
        ["Of course! What do you need help with?", "I'm here to help. What's the issue?", "How can I assist you?"])
]
chatbot=Chat(patterns,reflections)

def main():
    print("Hi there!I am a virtual chatbot,how can i help you?")
    print("Type 'quit' to exit.")
    
    while True:
        user_input=input("you: ")
        if user_input.lower() =='quit':
            break
        
        response=chatbot.respond(user_input)
        print("Bot:",response)
        
if __name__== "__main__":
    main()