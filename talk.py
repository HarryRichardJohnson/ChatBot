#!/usr/bin/python

# @author BBerryNZ
# Simple Chatbot prototype

#Will neaten up the code a bit later and add more complex stuff, but before since this is just a prototype/mini bot, this is all for now

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

class Talk:

    #Later on we can read the converstaion from a file rather than storing in a function, returns a list of the convo
    def listofConversation(self):
        """
        #Here you can read the conversationList from a file and store in a list rather than putting in function.
        #For example put the following in the file:
            "Hi",                                  #Question 1
            "Hey",                                  #Answer 1
            "Hello",                                #Question 2
            "Hi there!",                            #Answer 2
            "How are you doing?",                   #Question 3
            "I'm doing great.",                     #Answer 3 and so on....
            "That is good to hear",
            "Thank you.",
            "You're welcome."
        covoList = list()
        with open("conversation.txt", "r") as q:
            convoList.append(q)
        return convoList
        """
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
            userInput = input("Ask Skynet the bot a question or q to quit: ")
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
