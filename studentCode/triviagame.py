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

# import the question and player classes
from QuestionClass import Question, Player
from os import system
import random

clear_screen = system('cls')

def main():
    # generate a dictionary of questions
    questionsbank = generate_questionbank(10)

    # Get the players
    players = get_players()

    # play the game
    play_game(questionsbank, players)
    
def generate_questionbank(p_amount):
    # load a question list
    all_questions = {
        1 : {'question' : 'the actual question', 'possible_answers' : 'possibility','correct' : 'correct answer #'}
    }
    # start an empty list to store the questions
    game_questions = []
    # get random questions until p_amount is hit or all questions is empty
    while game_questions < p_amount and len(all_questions) > 0:
        # RNG
        rdm_index = random.randint(0, len(all_questions) - 1)
        # generate the question
        rdm_q = all_questions.pop(rdm_index)
        gen_question = Question(rdm_q['question'], rdm_q['pos_ans_1'], rdm_q['pos_ans_2'], rdm_q['pos_ans_3'], rdm_q['pos_ans_4'], rdm_q['correct'])
        # add the generated question object to the game questions
        game_questions.append(gen_question)

    # return the game questions list
    return game_questions

def get_players():
    # prompt for a number of players
    try:
        amount = int(input('How many players sill be playing? '))
    except ValueError:
        print('Bad Input: setting to default: 2')
        amount = 2
    # create an empty player list
    players = []
    # add the players
    for num in range(1, amount + 1):
        name = input(f'Enter Player {num}\'s name: ')
        players.append(Player(name))

    # return the list of players
    return players

def play_game(p_questions, p_players):
    # Iterate through the questions
    for num, q in enumerate(p_questions):
        possible_ans = [q.get_possible_1(), q.get_possible_2(), q.get_possible_3, q.get_possible_4()]
        # iterate through the players
        for p in p_players:
            clear_screen()
            # display player's turn
            print(f'\n\n\tIt\'s {p.get_name()}')
            # wait for player input for load the question (maybe add timer)
            input("Press any key to get your question...")
            # display the question
            print(f'\n{num + 1}: {q.get_question()}')
            print('\n')
            # display the possible answers
            for ind, ans in enumerate(possible_ans):
                print(f'\t{ind + 1}) {ans}')
                print()
            # Prompt for player's answer
            play = 0
            while play < 0 or play > 5:
                try:
                    play = int(input(f'{p.get_name()}\'s Answer? (1,2,3,4): '))
                except ValueError:
                    print('Invalid choice!')
                    play = 0
            if play == q.get_correct():
                p.add_points()
    # once all players and questions have been iterated through
    # iterate through the players and print their scores
    highest_score = p_players[0]
    for player in p_players:
        print(f'{player.get_name()} : Scored {player.get_points()} Points')
        if player.get_points() > highest_score.get_points:
            highest_score = player
    # print player win statement
    print(f'{highest_score.get_name()} Wins!')




            


