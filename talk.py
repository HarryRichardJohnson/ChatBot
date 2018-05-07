#!/usr/bin/python

# @author BBerryNZ
# Simple Chatbot prototype

#Will neaten up the code a bit later and add more complex stuff, but before since this is just a prototype/mini bot, this is all for now

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

class Talk:

    # This is a constructor, not necessary at this stage but may need it later.
    #def __init__(self):


    """
    This function gets a list of the conversation from a file and stores it in a list.
    To train the bot even more add more question answers to the list in same format, right now the conversation list is just an example, modify according to your own needs
    returns conversationList
    """
    def getConversations(self):
        conversationList = list
        with open("conversations.txt", "r") as convo:
            # Reads from the file and store the conversation in a list, removes new line characters (\n)
            conversationList = convo.read().splitlines()
            # Print statement here for debugging purposes, can be removed later if you want.
            print(conversationList)
        return conversationList

    """
    This function keeps on looping until the user enters q to quit, user input is asked and answer is given depending on the user input
    returns the userInput
    """
    def startTalking(self, chatterbot):
        while True:
            # Trying to catch any unhandled exceptions, for now will just break out and leave it
            try:
                # User input is asked
                userInput = input("Ask Skynet the bot a question or q to quit: ")
                # Gets a response from the bot according to the userInput given
                response = chatterbot.get_response(userInput)
            except (KeyboardInterrupt, EOFError, SystemExit):
                break

            # Quits if user enters q
            if userInput == 'q' or userInput == 'Q':
                break
            # Prints the response.
            print(response)

def main():
    #Creats a ChatBot object, the bot is named Skynet
    #This will help solve math problems and give current time etc...... But then stops having proper conversation, need to fix later
    #chatterbot = ChatBot("Skynet", logic_adapters=["chatterbot.logic.MathematicalEvaluation","chatterbot.logic.TimeLogicAdapter"])
    chatterbot = ChatBot("Skynet")
    #Creates a Talk object
    talk = Talk()

    #Gets the list of conversations
    conversations = talk.getConversations()

    # The bot gets trained
    chatterbot.set_trainer(ListTrainer)

    # The bot is trained by taking a list of statements that represent a conversation
    chatterbot.train(conversations)

    #The conversation begins
    talk.startTalking(chatterbot)


if __name__ == '__main__':
    main()
