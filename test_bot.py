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
    #Sets up the bot by creating a bot object
    def setUp(self):
        self.bot = botcode.Bot()

    #This function will test the bots response to a specific questions asked by the user.
    #Please replace get_response parameter with user question and self.assertEqual 2nd parameter with expected answer to unit test
    def test_bot_response(self):
        userQuestion = self.bot.chatterbot.get_response("Which papers are suitable for Software Development major?")
        self.assertEqual(userQuestion, "COMP603 Program Design & Construction, COMP602 Software Development Practice, COMP604 Operating Systems, OR INFS602 Physical Database Design, Any 3 of the following: ENSE701 Software Engineering, COMP719 Applied Human Computer Interaction, COMP721 Web Development, COMP713 Distributed & Mobile Systems")

# Runs all the unit-tests
if __name__ == '__main__':
    unittest.main()
