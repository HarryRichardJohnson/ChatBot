#!/usr/bin/python

# @author BBerryNZ
# Simple Chatbot prototype

#Will neaten up the code a bit later and add more complex stuff, but before since this is just a prototype/mini bot, this is all for now

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

class Bot:

    # This is a constructor is now necessary because it creates a chatterbot object when a bot object is created
    #I have my own reasons to put this here, before it was in the main, I put this here so it makes it easier to unit test so I can access the same object from test_bot class
    #Or else it was very hard to use the same object to test it unless I did it in the same file, bot, results would be different due to using another object and unit tests would fail
    #Note that I fixed a bug, the bug was when I added User: question.... Bot: answer...... it bugged out next time it ran and gave incorrect answers, so I removed that.
    def __init__(self):
        # Creates a ChatBot object, the bot is named Skynet
        self.chatterbot = ChatBot("Skynet")


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
            #print(conversationList)
        return conversationList

    """
    This function keeps on looping until the user enters q to quit, user input is asked and answer is given depending on the user input
    returns the userInput
    """
    def startTalking(self):
        while True:
            # Trying to catch any unhandled exceptions, for now will just break out and leave it
            try:
                # User input is asked
                userInput = input("Ask Skynet the bot a question or q to quit: ")
                # Gets a response from the bot according to the userInput given
                response = self.chatterbot.get_response(userInput)
            except (KeyboardInterrupt, EOFError, SystemExit):
                break

            # Quits if user enters q
            if userInput == 'q' or userInput == 'Q':
                break
            # Prints the response.
            print(response)

def main():
    #Creates a Bot object
    bot = Bot()

    #Gets the list of conversations
    conversations = bot.getConversations()

    # The bot gets trained
    bot.chatterbot.set_trainer(ListTrainer)

    # The bot is trained by taking a list of statements that represent a conversation
    bot.chatterbot.train(conversations)

    #The conversation begins
    bot.startTalking()


if __name__ == '__main__':
    main()
