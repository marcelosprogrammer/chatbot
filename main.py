from datetime import time
import time
time.clock = time.time # ccorrige o erro de time.clock
from chatterbot import ChatBot

chatbot = ChatBot("ChatbotSenac")

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")