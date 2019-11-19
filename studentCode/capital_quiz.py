'''
2. Capital Quiz
Write a program that creates a dictionary containing the U.S. states as keys and their capitals as values. 
(Use the Internet to get a list of the states and their capitals.) The program
should then randomly quiz the user by displaying the name of a state and asking the user
to enter that state’s capital. The program should keep a count of the number of correct and
incorrect responses. (As an alternative to the U.S. states, the program can use the names of
countries and their capitals.)
​'''

from random import randint

def capital_quiz():
    # Populate a dictionary with all of the states and their capitals
    capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
    }
    # initialize a number correct counter
    correct = 0
    # get the number of questions to ask
    quiz = 10
    # initialize a questions counter
    question = 1
    # Populate a list of states to work off of
    states = [state for state in capitals.keys()]
    # for key in capitals.keys():
    #     states.append(key)
    # continuously generate questions until question > quiz
    while question <= quiz:
        # select a random state, by selecting a key from a random integer index number
        rdm_state = states.pop(randint(0, len(states) - 1))
        # Prompt user for the capital of the selected state
        user_answer = input(f'{question}. What is the capital of {rdm_state}?\n')
        # check if the answer is correct
        if user_answer.title() == capitals[rdm_state]:
            # correct message
            print('Correct!')
            # increment the correct counter
            correct += 1
        else:
            print('Incorrect')
        # delete the state from states list to prevent repeat questions
        # states.remove(rdm_state)
        # increment the question number
        question += 1
    
    # calculate the score by dividing correct by the amount quizzed and multiply it by 100
    score = (correct / quiz) * 100
    # display results
    print(f'\n{correct}/{quiz} Correct.')
    print(f'{score:.2f}%')

capital_quiz()