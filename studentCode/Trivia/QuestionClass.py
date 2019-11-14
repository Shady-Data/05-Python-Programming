'''
8. Trivia Game
    In this programming exercise you will create a simple trivia game for two players. The program will 
    work like this:
        • Starting with player 1, each player gets a turn at answering 5 trivia questions. (There
        should be a total of 10 questions.) When a question is displayed, 4 possible answers are
        also displayed. Only one of the answers is correct, and if the player selects the correct
        answer, he or she earns a point.
        • After answers have been selected for all the questions, the program displays the number
        of points earned by each player and declares the player with the highest number of points
        the winner.
    To create this program, write a Question class to hold the data for a trivia question. The
    Question class should have attributes for the following data:
        • A trivia question
        • Possible answer 1
        • Possible answer 2
        • Possible answer 3
        • Possible answer 4
        • The number of the correct answer (1, 2, 3, or 4)
    The Question class also should have an appropriate __init__ method, accessors, and
    mutators.
    The program should have a list or a dictionary containing 10 Question objects, one for
    each trivia question. Make up your own trivia questions on the subject or subjects of your
    choice for the objects.
'''

class Question:
    # define __init__() with question, possible 4 possible answers, and the correct answer number
    def __init__(self, p_question, p_pos_ans_1, p_pos_ans_2, p_pos_ans_3, p_pos_ans_4, p_correct):
        self.__question = p_question
        self.__possible_answer_1 = p_pos_ans_1
        self.__possible_answer_2 = p_pos_ans_2
        self.__possible_answer_3 = p_pos_ans_3
        self.__possible_answer_4 = p_pos_ans_4
        self.__correct_answer = p_correct

    # define accessors
    def get_question(self):
        return self.__question

    def get_possible_1(self):
        return self.__possible_answer_1

    def get_possible_2(self):
        return self.__possible_answer_2

    def get_possible_3(self):
        return self.__possible_answer_3

    def get_possible_4(self):
        return self.__possible_answer_4

    def get_correct(self):
        return self.__correct_answer


class Player:
    def __init__(self, p_name):
        self.__name = p_name
        self.__points = 0

    def add_points(self, p_amount=1):
        self.__points += p_amount

    def get_name(self):
        return self.__name

    def get_points(self):
        return self.__points