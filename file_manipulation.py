import solution_generator

def copy_list():
    mylist = []
    with open('words.txt', 'r') as file:
        for line in file:
            word = line.replace('\n', '')
            mylist.append(word)
    print("list Copied: " + str(len(mylist)) + ' words remaining')
    return mylist


def remove_small_words(input_list):
    output = []
    for word in input_list:
        if len(word) >= 3:
            output.append(word)
    print("Small words removed: " + str(len(output)) + ' words remaining')
    return output


def remove_incorrect_letters(input_list, letters):
    output = []
    for word in input_list:
        output.append(word)
        for letter in word:
            if letter not in letters:
                output.remove(word)
                break
    print("bad letters removed: " + str(len(output)) + ' words remaining')
    return output


def remove_duplicates(input_list):
    output = []
    for word in input_list:
        output.append(word)
        for num in range(len(word)):
            try:
                if word[num] == word[num+1]:
                    output.remove(word)
                    break
            except IndexError:
                pass
    print("duplicate letters removed: " + str(len(output)) + ' words remaining')
    return output


def remove_same_side_letters(input_list, letters):
    output = []
    for word in input_list:
        output.append(word)
        for num in range(len(word)):
            try:
                initial_index = letters.index(word[num]) % 4
                second_index = letters.index(word[num+1]) % 4
                if initial_index == second_index:
                    output.remove(word)
                    break
            except IndexError:
                pass
    print("same side letters removed: " + str(len(output)) + ' words')
    return output


def input_letters():
    first_line = input("input the first line: ")
    second_line = input("input the second line: ")
    third_line = input("input the third line: ")
    fourth_line = input("input the fourth line: ")
    output = ''
    for x in range(3):
        output += first_line[x]
        output += second_line[x]
        output += third_line[x]
        output += fourth_line[x]
    return output


def write_new_list(input_list):
    with open("modded_words.txt", 'w') as file:
        for word in input_list:
            file.write(word + '\n')


def execute():
    accepted_letters = input_letters().lower()
    initial_list = copy_list()
    long_word_list = remove_small_words(initial_list)
    correct_letter_list = remove_incorrect_letters(long_word_list, accepted_letters)
    non_duplicate_words = remove_duplicates(correct_letter_list)
    non_same_side_words = remove_same_side_letters(non_duplicate_words, accepted_letters)
    write_new_list(non_same_side_words)
    solution_generator.execute()

execute()
