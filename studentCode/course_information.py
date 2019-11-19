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
    courses = {num : {'Room': room, 'Instructor': inst, 'Time' : time} for num, room, inst, time in zip(course_numbers, course_rooms, course_instructors, course_meet_times)}
    # initialize the dictionaries
    # course_2_rooms = {}
    # course_2_instructor = {}
    # course_2_meet_times = {}
    # initialize an index accumalator at 0
    # index = 0
    # # iterate through the course_numbers
    # for course in course_numbers:
    #     # add the values of rooms, instructors, and meet times to their respective dictionaries with the course number as the key
    #     course_2_rooms[course] = course_rooms[index]
    #     course_2_instructor[course] = course_instructors[index]
    #     course_2_meet_times[course] = course_meet_times[index]
    #     # Increment the index accumalator for the next course numbers data
    #     index += 1
    print('Available courses:', end=' ')
    for course in courses.keys():
        print(course, end=', ')
    # Prompt user for course number they need information for
    course_selection = input('\nEnter a course number for additional information: ')
    # Re-prompt for a course selection that exists in the dictionary keys
    # while course_selection not in course_2_rooms.keys():
    while course_selection not in courses.keys():
        # course_selection = input(f'Invalid Course Number!\nAvailable courses are {course_2_rooms.keys()}\nEnter a course number for additional information: ')
        course_selection = input(f'Invalid Course Number!\nAvailable courses are {courses.keys()}\nEnter a course number for additional information: ')
    
    # Display the course information
    print(f'\nCourse Number:          {course_selection}')
    # print(f'Course Instructor:      {course_2_instructor[course_selection]}')
    print('Course Instructor:     ', courses[course_selection]['Instructor'])
    # print(f'Course Room:            {course_2_rooms[course_selection]}')
    print('Course Room:           ', courses[course_selection]['Room'])
    # print(f'Course Meeting time:    {course_2_meet_times[course_selection]}')
    print('Course Meeting time:   ', courses[course_selection]['Time'])

# Call the program
school_course_information()