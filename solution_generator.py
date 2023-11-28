def copy_list():
    mylist = []
    with open('modded_words.txt', 'r') as file:
        for line in file:
            word = line.replace('\n', '')
            mylist.append(word)
    print("list Copied: " + str(len(mylist)) + ' words')
    return mylist


def build_1_list(word_list):
    return [word for word in word_list if len(set(word)) == 12]


def build_2_list(word_list):
    option_list = []
    for x in word_list:
        for y in word_list:
            if x != y:
                if x[-1] == y[0]:
                    if len(set((x + y))) == 12:
                        option_list.append([x,y])
    return option_list


def execute():
    word_list = copy_list()
    word_lists = build_1_list(word_list) or build_2_list(word_list)
    for x in word_lists:
        print(x)
    print(str(len(word_lists)) + " options generated!")
