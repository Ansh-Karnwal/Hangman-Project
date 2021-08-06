import random
class Hangman:

    def __init__(self) -> None:
        pass

    def start_menu(self):
        start_game = int(input("To start the Hangman Game please press 1. To exit please press 0: "))
        while start_game > 1 or start_game < 0:
            print("Invalid number!")
            start_game = int(input("To start the Hangman Game please press 1. To exit please press 0: "))
        if start_game == 0:
            quit()
        if start_game == 1:
            self.word_print_logic()

    def read_data(self):
        with open("words.txt", "r") as words_file:
            words_strings = words_file.read().splitlines()

        word_position = random.randint(0, len(words_strings)-1)
        random_word = words_strings[word_position]
        return random_word

    def hang_man_ui(self, invalid_counter):
        hangman = ['''
                            +---+
                            |   |
                                |
                                |
                                |
                                |
                            =========''', '''
                            +---+
                            |   |
                            O   |
                                |
                                |
                                |
                            =========''', '''
                            +---+
                            |   |
                            O   |
                            |   |
                                |
                                |
                            =========''', '''
                            +---+
                            |   |
                            O   |
                           /|   |
                                |
                                |
                            =========''', '''
                            +---+
                            |   |
                            O   |
                           /|\  |
                                |
                                |
                            =========''', '''
                            +---+
                            |   |
                            O   |
                           /|\  |
                           /    |
                                |
                            =========''', '''
                            +---+
                            |   |
                            O   |
                           /|\  |
                           / \  |
                                |
                            =========''']
        return hangman[invalid_counter]
        
    def word_print_logic(self):
        random_word = self.read_data()
        word_str = random_word
        random_word = list(random_word)
        for lowercase in range(len(random_word)):
            random_word[lowercase] = random_word[lowercase].lower()
        word_line = "_" * len(random_word)
        letter_lst = []
        word_lst = []
        has_guessed = False
        invalid_counter = 6
        print(random_word)
        print(self.hang_man_ui(invalid_counter))
        length_word = len(random_word)
        print(f"The length of the word is {length_word} letters long")
        print("Enter the letters or word below\n")
        while invalid_counter > 0 and not has_guessed:

            guess_letter = input("Enter the letter or word: ")

            while not guess_letter.isalpha():
                print("Please enter a valid number!")
                guess_letter = input("Enter the letter or word: ")

            if len(guess_letter) == 1 and guess_letter.isalpha():
                if guess_letter in letter_lst:
                    print(f"You have already guessed {guess_letter}!")
                elif guess_letter not in random_word:
                    invalid_counter -= 1
                    print(f"{guess_letter} is the wrong Letter!")
                    letter_lst.append(guess_letter)
                    invalid_string = str(letter_lst)[1:-1]
                    if invalid_counter > 0:
                        print(self.hang_man_ui(invalid_counter))
                        print(f"You have only {invalid_counter} guesses left. You have guessed the wrong letter(s) {invalid_string}")
                    if invalid_counter == 0:
                        print(self.hang_man_ui(invalid_counter))
                        print("You have ran out of guesses!")  
                    
                else:
                    print(f"The letter you guessed, {guess_letter} is in the word!")
                    letter_lst.append(guess_letter)
                    word_lst = list(word_line)
                    guess_temp = [x for x, letaer in enumerate(random_word) if letaer == guess_letter]
                    for pos in guess_temp:
                        word_lst[pos] = guess_letter
                    word_line = "".join(word_lst)
                    if "_" not in word_line:
                        has_guessed = True
                    
            elif len(guess_letter) == len(random_word) and guess_letter.isalpha():
                if guess_letter in word_lst:
                    print(f"The word, {guess_letter} has already been entered!")
                elif guess_letter != word_str:
                    print(f"The word, {guess_letter} is not the word!")
                    invalid_counter -=1
                    word_lst.append(guess_letter)
                else:
                    has_guessed = True
                    word_line = random_word
            else:
                print("Error")
            print(self.hang_man_ui(invalid_counter))
            print(word_line)
            
            if invalid_counter == 0:
                print("You lost!")
                game_val = input("Want to play again? Type Y to play again. Type N to exit. (Y/N): ")
                if game_val  == "Y" or "y":
                    self.start_menu()
                else:
                    quit()

            if has_guessed:
                print("You Won!")
                game_val = input("Want to play again? Type Y to play again. Type N to exit. (Y/N): ").lower()
                if game_val == "y":
                    self.start_menu()
                else:
                    quit()

hangman = Hangman()
hangman.start_menu()