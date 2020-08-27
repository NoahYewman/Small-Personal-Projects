# File where the game commands will be
import urllib.request


def choose_word():
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

    url = "https://randomword.com"
    headers = {'User-Agent': user_agent, }

    request = urllib.request.Request(url, None, headers)
    response = urllib.request.urlopen(request)
    data = str(response.read())

    start_index = data.find('<div id="random_word">') + len('<div id="random_word">')
    end_index = data.find('<div id="random_word_definition">') - 16
    word = data[start_index:end_index]
    # print(word)

    return word

def word_def():
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

    url = "https://randomword.com"
    headers = {'User-Agent': user_agent, }

    request = urllib.request.Request(url, None, headers)
    response = urllib.request.urlopen(request)
    data = str(response.read())

    start_index_def = data.find('<div id="random_word_definition">') + len('<div id="random_word_definition">')
    end_index_def = data.find('<div id="next_random_word" style="margin-bottom:20px">') - 30
    word_def = data[start_index_def:end_index_def]

    return word_def



num_attempts = 6
user_attempts = 0

guess_word = choose_word()


def create_board(word):
    board = "_" * len(word)
    # print(len(board))
    # print(len(word))
    return board


board = create_board(guess_word)


def not_in_word(letter, previous_guesses):
    print("{0} is not in the word".format(letter))
    previous_guesses.append(letter)


def play_again():
    again = input("Would you like to play again? y/n: ")
    if again.lower()[0] == "y":
        guess_word = choose_word()
        board = create_board(guess_word)
        game(board, guess_word)

    else:
        print("Thanks for playing!")


def game(board, word):
    user_attempts = 0
    previous_guesses = []
    guessed = False
    word_definition = word_def()
    while user_attempts <= num_attempts and guessed == False:
        # current state of game
        print(display_hangman(num_attempts - user_attempts))
        print(board)
        print("Attempts remaining: {0}".format(num_attempts - user_attempts))
        print("Previous guesses: {0}".format(previous_guesses))

        new_letter = input("Guess a letter: ")

        if new_letter in word:
            print("{0} is in the word!".format(new_letter))
            previous_guesses.append(new_letter)
            word_as_list = list(board)
            indices = [i for i, letter in enumerate(word) if letter == new_letter]
            for index in indices:
                word_as_list[index] = new_letter
            board = ''.join(word_as_list)
            if "_" not in board:
                guessed = True
                print("{0} is the word. You win!".format(word))

        # Checks if letter has been guessed before
        elif new_letter in previous_guesses:
            print("{0} has already been guessed.".format(new_letter))

        # Checks that it isn't more than 1 char long, and it is a letter
        elif len(new_letter) > 1 or not new_letter.isalpha():
            print("{0} is not a letter!".format(new_letter))

        else:
            not_in_word(new_letter, previous_guesses)
            user_attempts += 1

    if guessed:
        print("You win! The word was {0}".format(word))
        print("The definition of {0} is {1}!".format(word, word_definition))

    else:
        print("You lose. The word was {0}".format(word))
        print("The definition of {0} is '{1}'!".format(word, word_definition))

    # Play again prompt
    play_again()


# Display states taken from https://github.com/kiteco/python-youtube-code/blob/master/build-hangman-in-python/hangman.py
def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # head, torso, both arms, and one leg
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # head, torso, and both arms
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # head, torso, and one arm
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # head and torso
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # head
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # initial empty state
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


game(board, guess_word)
