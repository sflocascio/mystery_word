import random 

#play_again = True
#while play_again:
def play_game():
    difficulty_word_list = []

    with open("words.txt") as x:
        y = x.readlines()
        y = [x.replace('\n','').lower() for x in y]

    user_setting = input(str("welcome to MYSTERY WORD!, select 'easy' 'medium' or 'hard' to play..."))

    for word in y:
        if (str(user_setting) == "easy"):
            if len(word) == 3 or len(word) == 4:
                difficulty_word_list.append(word)
        if (str(user_setting) == "medium"):
            if len(word) == 5 or len(word) == 6:
                difficulty_word_list.append(word)
        if (str(user_setting) == "hard"):
            if len(word) > 7:
                difficulty_word_list.append(word)
        # else: 
        #     print("so")

    new_word = random.choice(difficulty_word_list)


    print("NUMBER OF CHARACTERS IN WORD = ", len(new_word))

    word = new_word
    # print(word)

    guesses = []
    correct_guesses = []
    attempts_left = 8

    # if len(correct_guesses) == len(word):
    #     print("you win!")

    while attempts_left != 0:
        guess_a_letter = str(input("GUESS A LETTER...").lower())
        guesses.append(guess_a_letter)
        print("these are your guesses: ", guesses)
        if guess_a_letter not in word:
            attempts_left -= 1
            print("attempts left = ", attempts_left)
        def print_word(letter, guess):
            if letter in guess:
                correct_guesses.append(guess_a_letter)
                return letter
            else:
                return "_"
        result = [print_word(letter, guesses) for letter in word]
        print(' '.join(result))
    else:
        print("SORRY FRIEND... the mystery word was", word)
        new = input(str("want to play again? yes to play no to leave"))
        if new == "yes":
            play_game()


play_game()
