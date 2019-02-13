"""Name: Sarah Andert
    Course: CMPS 1500
    Lab Section: Tuesday, CMPS 1501-05 11-12.15 pm
    Assignment: lab4pr2-1.py
    Date: 10/01/2018
    Program to read contents of a file into a dictionary, display to user possible choices for working with dictionary entries
    (look up, add, change, delete, display, and quit), and write modified dictionary back to the file.

    (str)->int
    user enters string value for choice, returns integer to call selected function
    

    >>> look_up(majors)
    Enter a name: Harry
    Computer Science
    >>> look_up(majors)
    Enter a name: Ron
    English
    >>> look_up(majors)
    Enter a name: Voldemort
    Not found.

    >>> add(majors)
    Enter a name: Hagrid
    Enter a major: Physics
    >>> majors
    {’Harry’: ’Computer Science’, ’Ron’: ’English’, ’Hagrid’: ’Physics’,
    ’Hermione’: ’Mathematics’}
    >>> add(majors)
    Enter a name: Ron
    Enter a major: Art
    A person with this name already exists in the system.

    >>> change(majors)
    Enter a name: Harry
    Enter the new major: Biology
    >>> majors
    {’Ron’: ’English’, ’Hermione’: ’Mathematics’, ’Harry’: ’Biology’}
    >>> change(majors)
    Enter a name: Voldemort
    That name is not found.

    >>> delete(majors)
    Enter a name: Harry
    >>> majors
    {’Hermione’: ’Mathematics’, ’Ron’: ’English’}
    >>> delete(majors)
    Enter a name: Voldemort
    That name is not found.

    >>> display(majors)
    Hermione is a wizard in Mathematics
    Harry is a wizard in Computer Science
    Ron is a wizard in English

   >>> get_menu_choice()
    Majors of College Students
    ---------------------------
    1. Look up a student’s major
    2. Add a new student
    3. Change a major
    4. Delete a student
    5. Display all students
    6. Quit the program
    Enter your choice: 7
    Enter a valid choice: hello
    Enter a valid choice: 2
    2

    >>> main()
    Majors of College Students
    ---------------------------
    1. Look up a student’s major
    2. Add a new student
    3. Change a major
    4. Delete a student
    5. Display all students
    6. Quit the program
    Enter your choice: 2
    Enter a name: Hagrid
    Enter a major: Computer Science

    Majors of College Students

    ---------------------------
    1. Look up a student’s major
    2. Add a new student
    3. Change a major
    4. Delete a student
    5. Display all students
    6. Quit the program
    Enter your choice:
 """

## look_up
def look_up(d):
    name = input("Enter a name: ")
    if name in d.keys():
        print(d[name])
    else:
        print("Not found.")

## add
def add(d):
    
    name = input("Enter a name: ")
    major = input("Enter a major: ")
    if name in d.keys():
        print("A person with this name already exists in the system.")
        
    else:
        d[name] = major

## change
def change(d):
    name = input("Enter a name: ")
    if name in d.keys():
        major = input("Enter the new major: ")
        d[name] = major

    else:
        print("That name is not found.")

## delete
def delete(d):
    name = input("Enter a name: ")
    if name in d.keys():
        del d[name]
        

    else:
        print("That name is not found.")

## display
def display(d):
    for name, major in d.items():
        print('%s is a wizard in %s' % (name, major))

## get_menu_choice
def get_menu_choice():
    
    print("Majors of College Students")
    print("---------------------------")
    print("1. Look up a student's major\n2. Add a new student\n3. Change a major\n4. Delete a student\n5. Display all students\n6. Quit the program")
    print()

    user_input = ' '
    while user_input not in '123456':
        user_input = input("Enter your choice: ")
    user_input = int(user_input)
    return user_input


## The main part of program

majors = {}
choice = 0

# Open and read the file into dictionary (found suggestion to split line from Stack Overflow)
f = open("majors.txt", "r")

for line in f:
    (name, major) = line.split('\t') # specify split items on tab instead of () or \n to allow for multiple-word majors like "computer science"
    majors[name] = major
f.close()

# This portion of code-- the while loop that calls get_menu_choice-- was provided with lab assignment
while choice != 6:

        choice = get_menu_choice()

        if choice == 1:
            look_up(majors)
        elif choice == 2:
            add(majors)
        elif choice == 3:
            change(majors)
        elif choice == 4:
            delete(majors)
        elif choice == 5:
            display(majors)
        print()


# Write dictionary key-value pairs to the file as strings, separated by tab
f = open('majors.txt', 'w')

for name, major in majors.items():
    f.write('%s\t%s' % (name, major))
    
f.close()












