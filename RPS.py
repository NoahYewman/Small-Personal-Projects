import random

class RockPaperScissors(object):

    def __init__(self):
        self.CHOICE_MAPPING = {
            'scissors': 'paper',
            'rock': 'scissors',
            'paper': 'rock',
        }

    def play(self):
        user_choice = self.get_users_choice()
        computer_choice = self.get_computer_choice()
        print(self.evaluate(user_choice, computer_choice))

    def evaluate(self, user_guess, computer_guess):
        if user_guess == computer_guess:
            return 'DRAW'
        elif self.CHOICE_MAPPING[user_guess] == computer_guess:
            return 'WIN'
        else:
            return 'LOSE'


    def get_users_choice(self):
        return str(input("Rock, Paper or Scissors? ")).lower()

    def get_computer_choice(self):
        return random.choice(list(self.CHOICE_MAPPING.keys()))


play_again = True
while play_again:
    RockPaperScissors().play()
    play_again = str(input("play again? ")).lower()[0] == 'y'
