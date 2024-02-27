'''
@author: mikaeltunturi
'''
def read_file():
    name = input("Enter the name of the file used.\n")
    vocabulary_file = open(name, "r")
    list = []
    for line in vocabulary_file:
        row = line
        line = line.split(":")
        try:
            if len(line) != 2:
                line = row.rstrip()
                print("ERROR in line: {:s}".format(line))
            elif line[0].rstrip() == "":
                line = row.rstrip()
                print("ERROR in line: {:s}".format(line))
            elif line[1].rstrip() == "":
                line = row.rstrip()
                print("ERROR in line: {:s}".format(line))
            else:
                line[1] = line[1].split("/")
                latter_part = line[1]
                a = 0
                for i in latter_part:
                    if i.rstrip() == "":
                        a += 1
                    else:
                        pass
                if a > 0:
                    line = row.rstrip()
                    print("ERROR in line: {:s}".format(line))
                elif a == 0:
                    list.append(line)    
        except IndexError:
            line = row.rstrip()
            print("ERROR in line: {:s}".format(line))      
    return list

def quiz(list):
    print("Enter the following words in English:")
    next_round = []
    for word in list:
        print(word[0])
        users_answer = input("")
        users_answer = users_answer.upper()
        a = 0
        many_options = []
        while len(word[1]) > a:    
            correct_answer = word[1][a].rstrip()
            correct_answer = correct_answer.upper()
            many_options.append(correct_answer)
            a += 1
        if users_answer in many_options:
            print("Correct!")
        else:
            print("Incorrect, try again!")
            next_round.append(word)
            users_answer = input("")
            users_answer = users_answer.upper()
            if users_answer in many_options:
                print("That was correct.")
            else:
                print("Incorrect again, the correct answer is {:s}".format(word[1][0]))
    if next_round == []:
        return True
    else:
        print("Repeat the words which were incorrect:")
        next_next_round = []
        for word in next_round:
            print(word[0])
            users_answer = input("")
            users_answer = users_answer.upper()
            a = 0
            many_options = []
            while len(word[1]) > a:    
                correct_answer = word[1][a].rstrip()
                correct_answer = correct_answer.upper()
                many_options.append(correct_answer)
                a += 1
            if users_answer in many_options:
                print("Correct!")
            else:
                print("Incorrect, try again!")
                users_answer = input("")
                users_answer = users_answer.upper()
                next_next_round.append(word)
                if users_answer in many_options:
                    print("That was correct.")
                else:
                    print("Incorrect again, the correct answer is {:s}".format(word[1][0]))
    if next_next_round == []:
        return True
    else:
        print("Repeat the words which were incorrect:")
        all_correct = 0
        while len(next_next_round) > all_correct:
            for word in next_next_round:
                print(word[0])
                users_answer = input("")
                users_answer = users_answer.upper()
                a = 0
                many_options = []
                while len(word[1]) > a:    
                    correct_answer = word[1][a].rstrip()
                    correct_answer = correct_answer.upper()
                    many_options.append(correct_answer)
                    a += 1
                if users_answer in many_options:
                    print("Correct!")
                    all_correct += 1
                else:
                    print("Incorrect, try again!")
                    users_answer = input("")
                    users_answer = users_answer.upper()
                    next_next_round.append(word)
                    if users_answer in many_options:
                        print("That was correct.")
                    else:    
                        print("Incorrect again, the correct answer is {:s}".format(word[1][0]))
        return True            
        
def main():
    try:
        print("This is a vocabulary quiz.")
        list = read_file()
        quiz(list)
        print("Well done! The quiz terminates.")
    except OSError:
        print("ERROR in reading the file. The program terminates.")
main()
