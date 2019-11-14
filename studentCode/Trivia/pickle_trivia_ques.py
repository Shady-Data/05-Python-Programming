import pickle
import csv
from random import randint

def main():
    with open('Trivia_v2.csv', 'r') as csv_file:
        csv_read = csv.reader(csv_file)

        csv_list = []
        for line in csv_read:
            csv_list.append(line)

    questions = []
    answers = []
    correct = []
    for line in csv_list:
        questions.append(line[0])
        answers.append([line[1]])
        correct.append(line[1])

    for ans in answers:
        while len(ans) < 4:
            rng = randint(0, len(correct) - 1)
            if correct[rng] not in ans:
                ans.append(correct[rng])

    question_bank = []
    for ind in range(len(questions)):
        quest = []
        quest.append(questions[ind])
        for ans in answers[ind]:
            quest.append(ans)
        quest.append(correct[ind])
        question_bank.append(quest)

    with open('trivia-v2.dat', 'wb') as outfile:
        pickle.dump(question_bank, outfile)

    
main()