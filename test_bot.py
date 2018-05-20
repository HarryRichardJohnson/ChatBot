#Imports bot.py as botcode
import bot as botcode
import unittest
from chatterbot.trainers import ListTrainer

#@author BBerry.NZ

"""
This class will Test bot.py
Right now the brain of the bot is being tested(db.sqlite3)
"""
class TestBotClass(unittest.TestCase):
    #Sets up the bot
    def setUp(self):
        print("The function setUp is running.............")
        self.chatterbot = botcode.ChatBot("Skynet")
        self.bot = botcode.Bot()
        # Gets the list of conversations
        conversations = self.bot.getConversations()
        # The bot gets trained, DON'T NEED TO TRAIN THE BOT FOR UNIT_TESTS, (Its already trained)
        #self.chatterbot.set_trainer(ListTrainer)
        # The bot is trained by taking a list of statements that represent a conversation
        #self.chatterbot.train(conversations)

    #This function will test the startTalking function, since we cant test startTalking straight away I have decided test the bots response to a specific questions.
    #In this case this unit test is successfull.
    #When the user asks, to test more of the user stories (questions) replace "User: Which papers are suitable for a Software Engineer?" with the question to test and,
    #replace "Bot: Contemporary Methods in Software Engineering, Software Development Practice, Programming Languages" with the expected answer.
    def test_bot_response(self):
        print("The function test_startTalking started running.............")
        userQuestion = self.chatterbot.get_response("Which papers are suitable for a Software Engineer?")
        self.assertEqual(userQuestion, "Bot: Contemporary Methods in Software Engineering, Software Development Practice, Programming Languages.")

# Runs all the unit-tests
if __name__ == '__main__':
    unittest.main()
