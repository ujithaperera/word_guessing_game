words = []
filename = 'dictionary.txt'

hidden_word = []
remaining_guesses = 0
low = 0

def begin():
    with open(filename) as ins:
        for line in ins:
            words.append(line.rstrip('\n'))

    global remaining_guesses
    global low

    low = ask_length_of_the_word()
    number_of_guesses = ask_number_of_guesses()
    remaining_guesses = number_of_guesses
    print str(low)
    game_words = get_game_words(words, low)
    guessing_word(game_words)


def ask_length_of_the_word():
    global low
    user_given_length = raw_input("Enter length of the word: ")
    user_given_length = int(user_given_length)
    if 0 < user_given_length <= getMaxWordSize(words):
        return user_given_length
    else:
        print "Invalid charactor length in dictionary\n"
        ask_length_of_the_word()


def ask_number_of_guesses():
    nog = raw_input("Enter Number of guessses you want: ")
    nog = int(nog)
    if 27 > nog > 0:
        return nog
    else:
        print "Invalid guesses amount !. Try again\n"
        ask_number_of_guesses()


def getMaxWordSize(words):
    if len(words) > 0:
        l = 0
        for word in words:
            if l < len(word):
                l = len(word)

        return l
    else:
        print "dictionary is empty !\n"


def get_game_words(words, length):
    game_words = []
    global hidden_word
    for i in range(length):
        hidden_word.append("*")
        print '*',
    for word in words:
        if (length == len(word)):
            game_words.append(word)

    return game_words


def get_a_character():
    # limit repeating same letter  and validation
    char = raw_input("\nenter a character : ")
    return char


def all_characters_revealed():
    global hidden_word
    b = True
    for c in hidden_word:
        if c == '*':
            b = False
    if b:
        print "You Won the Game !!!"
        return True
        # NEW Begin
    else:
        return False



def is_finished():
    global remaining_guesses
    remaining_guesses -= 1

    print "\nRemaining number of guesses : " + str(remaining_guesses)
    if remaining_guesses == -1:
        print "Sorry !\nAvailable guesses count is 0\n You lost the game\n"
        return True
    elif all_characters_revealed():
        print "\nYou Won !!!\n"
        return True
    else:
        return False


def print_current_hidden_word():
    global hidden_word
    for c in hidden_word:
        print c,

def show_character(char, result):
    global hidden_word
    for r in result:
        if hidden_word[int(r)] == "*":
           hidden_word[int(r)] = char


def guessing_word(current_list):
    char = get_a_character()  # develop this func
    not_have_list = []
    have_list = []
    for word in current_list:
        if word.find(char) == -1:
            not_have_list.append(word)
        else:
            have_list.append(word)

    if len(not_have_list) > 0:
        if not is_finished():
            print_current_hidden_word()
            guessing_word(not_have_list)

    else:
        single_list = []
        multi_list = []
        for word in have_list:
            result = get_indexes(char, word)
            if len(result) > 1:
                multi_list.append(word)
            else:
                single_list.append(word)

        if len(single_list) > 0:
            # last selection should be done
            result = get_indexes(char, single_list[0])
            show_character(char, result)

            if not is_finished():
                next_list = []
                next_list.append(single_list[0])
                print_current_hidden_word()
                guessing_word(next_list)

        else:
            result = get_indexes(char, multi_list[0])
            show_character(char, result)
            if not is_finished():
                next_list = []
                next_list.append(multi_list[0])
                print_current_hidden_word()
                guessing_word(next_list)


def get_indexes(char, word):
    index_list = []
    for i, c in enumerate(word):
        if c.find(char) > -1:
            index_list.append(i)

    return index_list

begin()
