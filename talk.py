#!/usr/bin/python

# @author BBerryNZ
# Simple Chatbot prototype

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

class Talk:

    #Later on we can read the converstaion from a file rather than storing in a function, returns a list of the convo
    def listofConversation(self):
        # Using this we can train the chatterbot, this is a list of a converstaion
        conversation = [
            "Hi",
            "Hey",
            "Hello",
            "Hi there!",
            "How are you doing?",
            "I'm doing great.",
            "That is good to hear",
            "Thank you.",
            "You're welcome."
        ]
        return conversation

    def convo(self, chatterbot):
        while True:
            # User input is asked
            userInput = input("Ask the Skynet a question or q to quit: ")
            # gets the response from the bot according to the userInput given
            response = chatterbot.get_response(userInput)
            # Quits if user enters q
            if userInput == 'q':
                break
            # Prints the response.
            print(response)

            return userInput

def main():
    #Creats a ChatBot object, the bot is named Skynet
    chatterbot = ChatBot("Skynet")

    #Creates a object Talk object
    talk = Talk()

    conversation = talk.listofConversation()

    # The bot gets trained
    chatterbot.set_trainer(ListTrainer)

    # The bot can have a simple Conversation after being trained with the list of Conversation
    chatterbot.train(conversation)
    talk.convo(chatterbot)


if __name__ == '__main__':
    main()
