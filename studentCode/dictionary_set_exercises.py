"""
Write a program that creates a dictionary containing course numbers and the room numbers of the rooms where the 
courses meet. The dictionary should have the following keyvalue pairs:
​
Course Number (key) Room Number (value)
CS101               3004
CS102               4501
CS103               6755
NT110               1244
CM241               1411
​
The program should also create a dictionary containing course numbers and the names of
the instructors that teach each course. The dictionary should have the following key-value
pairs:
​
Course Number (key) Instructor (value)
CS101               Haynes
CS102               Alvarado
CS103               Rich
NT110               Burke
CM241               Lee
​
The program should also create a dictionary containing course numbers and the meeting
times of each course. The dictionary should have the following key-value pairs:
​
Course Number (key) Meeting Time (value)
CS101               8:00 a.m.
CS102               9:00 a.m.
CS103               10:00 a.m.
NT110               11:00 a.m.
CM241               1:00 p.m.
​
The program should let the user enter a course number, and then it should display the
course’s room number, instructor, and meeting time.
​"""

def school_course_information():
    # lazy dictionary creation
    # populate a list containing all of the courses and lists containing their respective values
    course_numbers = ['CS101', 'CS102', 'CS103', 'NT110', 'CM241']
    course_rooms = [3004, 4501, 6755, 1244, 1411]
    course_instructors = ['Haynes', 'Alvarado', 'Rich', 'Burke', 'Lee']
    course_meet_times = ['8:00 a.m.', '9:00 a.m.', '10:00 a.m.', '11:00 a.m.', '1:00 p.m.']
    # initialize the dictionaries
    course_2_rooms = {}
    course_2_instructor = {}
    course_2_meet_times = {}
    # initialize an index accumalator at 0
    index = 0
    # iterate through the course_numbers
    for course in course_numbers:
        # add the values of rooms, instructors, and meet times to their respective dictionaries with the course number as the key
        course_2_rooms[course] = course_rooms[index]
        course_2_instructor[course] = course_instructors[index]
        course_2_meet_times[course] = course_meet_times[index]
        # Increment the index accumalator for the next course numbers data
        index += 1
    
    # Prompt user for course number they need information for
    course_selection = input('Enter a course number for additional information: ')
    # Re-prompt for a course selection that exists in the dictionary keys
    while course_selection not in course_2_rooms.keys():
        course_selection = input(f'Invalid Course Number!\nAvailable courses are {course_2_rooms.keys()}\nEnter a course number for additional information: ')
    
    # Display the course information
    print(f'\nCourse Number:          {course_selection}')
    print(f'Course Instructor:      {course_2_instructor[course_selection]}')
    print(f'Course Room:            {course_2_rooms[course_selection]}')
    print(f'Course Meeting time:    {course_2_meet_times[course_selection]}')

# Call the program
# school_course_information()


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
    states = []
    for key in capitals.keys():
        states.append(key)
    # continuously generate questions until question > quiz
    while question <= quiz:
        # select a random state, by selecting a key from a random integer index number
        rdm_state = states[randint(0, len(capitals) - 1)]
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
        states.remove(rdm_state)
        # increment the question number
        question += 1
    
    # calculate the score by dividing correct by the amount quizzed and multiply it by 100
    score = (correct / quiz) * 100
    # display results
    print(f'\n{correct}/{quiz} Correct.')
    print(f'{score:.2f}%')

# capital_quiz()

'''3. File Encryption and Decryption
Write a program that uses a dictionary to assign “codes” to each letter of the alphabet. For
example:
codes = { 'A' : '%', 'a' : '9', 'B' : '@', 'b' : '#', etc...}
Using this example, the letter A would be assigned the symbol %, the letter a would be
assigned the number 9, the letter B would be assigned the symbol @, and so forth.
The program should open a specified text file, read its contents, and then use the dictionary to 
write an encrypted version of the file’s contents to a second file. Each character in
the second file should contain the code for the corresponding character in the first file.'''

"""4. Unique Words
Write a program that opens a specified text file and then displays a list of all the unique
words found in the file.
Hint: Store each word as an element of a set
​"""

from pprint import pprint

def unique_words():
    # initialize the set variable
    unique = set()
    # open the file to be read
    read_file = open('state_capitals.txt', 'r')
    # iterate through each line in the file
    for line in read_file.readlines():
        # read and split each line into the set (replace calls are specific to file referenced)
        unique.update(line.rstrip('\n').replace(':', '').replace(',', '').replace("\'", "").split(' '))
    # close the file
    read_file.close()
    # Print the unique words
    pprint(unique)

# unique_words()

'''
5. Word Frequency
Write a program that reads the contents of a text file. The program should create a dictionary in which the keys are the individual words found in the file and the values are the
number of times each word appears. For example, if the word “the” appears 128 times,
the dictionary would contain an element with 'the' as the key and 128 as the value.
The program should either display the frequency of each word or create a second file
containing a list of each word and its frequency
'''

def word_frequency():
    # initialze a blank dictionary to fill
    words = {}
    # open the file to read
    in_file = open('turtlehelp.txt', 'r')
    # iterate through each line in the file
    for line in in_file.readlines():
        # iterate each word in the line
        for word in line.split():
            # Check if the word is in the words dictionary keys
            if word in words.keys():
                # increment the value of the word by 1
                words[word] += 1
            else:
                # set the value 1 to the words[word] key
                words[word] = 1
    # close the file being read
    in_file.close()

    # open a file to write the count to
    out_file = open('turtlehelp_word_count.txt', 'w')
    # iterate through the dictionary
    for word, count in words.items():
        # write the word and the count to the file, one entry per line
        out_file.write(f'{word}: {count},\n')
    # close the file being written to
    out_file.close()

word_frequency()

"""
6. File Analysis
Write a program that reads the contents of two text files and compares them in the following ways:
• It should display a list of all the unique words contained in both files.
• It should display a list of the words that appear in both files.
• It should display a list of the words that appear in the first file but not the second.
• It should display a list of the words that appear in the second file but not the first.
• It should display a list of the words that appear in either the first or second file but not both.
Hint: Use set operations to perform these analyses.
"""

def file_analysis():
    # create empty variables to store the information too
    file_1_unique = set()
    file_2_unique = set()
    # open the first file for comparison