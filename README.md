[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/07tV9k7q)
# tPythonListsAndDicts01
Python List and Dictionary Program

Use the attached sample code to help with Python Program Three - Lists and Dictionaries

More sample code will be pushed to this template repo throughout the week as students ask for help.

Python Program Three - Exploring Python Data Structures with Lists and Dictionaries

Course: Python Programming (CIT-95)
Professor: Dennis Mohle
Fresno City College, Fresno, California

Description:

In this assignment, you will continue to build your Python programming skills by exploring and manipulating various Python data structures, including lists, strings, and dictionaries. You have been learning Python for five weeks, and this assignment will challenge you to apply your knowledge effectively. The goal is to reinforce your understanding of Python data structures and how to create user-defined methods to solve real-world problems.

Deliverables:

Python Program Three Script: A well-documented Python script named "python_program_three.py" that contains your code for this assignment.

ReadMe on GitHub Classroom: Use the ReadMe file in your GitHub Classroom remote repository to summarize your program, its functionality, and the approach you took to solve the problem. 

Verbose Comments: Explain and comment each section of your code. Explain your thought process, reasoning, and any assumptions made during the implementation.

Testing Results in ReadMe: In the same ReadMe file on GitHub Classroom, include a section where you describe the test cases you created to ensure the correctness of your program. List the test cases and their outcomes. Explain how your program handles different scenarios and any improvements you would make if you had more time.

Assignment Details:
You are tasked with developing a Python program that simulates a basic contact management system. Your program should allow users to add, view, and search for contacts. Each contact will have a name, phone number, and email address. You will use Python lists, strings, and dictionaries to implement this system.

Requirements:

Create an empty list called contacts to store contact information. Each contact should be represented as a dictionary with the following keys:

'name': The name of the contact (a string).
'phone': The phone number of the contact (a string).
'email': The email address of the contact (a string).

Implement a function called add_contact() that takes user input to add a new contact to the contacts list. Ensure that each contact has a unique name.

Implement a function called view_contacts() that displays the list of all contacts in a user-friendly format.

Implement a function called search_contact() that takes a name as input and searches for the contact by name. If found, display the contact's details. If not found, display a message indicating that the contact was not found.

Use string formatting and string methods (e.g., format(), split(), strip(), etc.) to format and validate user input as necessary.

Additional Guidelines:

Basic: Make sure to create user-defined methods for adding, viewing, and searching for contacts.

Basic: Commit to your GitHub Classroom repo whenever you create a program update. This shows me that you're working and learning, and also earns you commits on your GitHub profile!

Advanced: Your program will provide a menu with options to add a contact, view all contacts, search for a contact, and exit the program.

Advanced: Implement error handling to handle invalid user input.

Advanced: Use Python file i/o to output your list of contcts to a text file on your local machine. 

Submission:

Submit your "python_program_three.py" program and update the ReadMe.md file in your GitHub Classroom remote repository by the specified deadline.

Grading Criteria:

You will be assessed based on the following criteria:

Correctness of the program's functionality.
Proper use of Python data structures (lists, dictionaries, strings).
Clarity and organization of your code.
Comprehensive and well-structured summary of your program in the ReadMe.md file.
Adherence to Python coding conventions and best practices.

Good luck, and enjoy working on this assignment! If you have any questions or need clarification, reach out during weekend office hours or via the Canvas inBox.


9/17/2023-Create a summary of python-program-three project:
I began the program by initializing an empty list under 'contacts' which is where the contacts and their information will be stored.
I then proceeded to define the function : add contact(), which was implemented to add a contact into the 'contacts' list. 
Within the add contact () function, I added additional lines of code that each included the following variables: 'name', 'email', and 'phone' in order to store inputs for
the contact's name, e-mail address, and phone number. 
I then proceed to create a new dictionary under new_contact = {'name': name, 'phone': phone, 'email': email} that contains keys (under 'name' 'phone' and 'email') that would
be associated with the values that are inputted by the user. 
Afterwards, I would append the 'new contact' dictionary to the 'contacts' list that would essentially add any new contacts to 
the contact list. 
I then went ahead and implemented two additional functions. The view_contacts() function was implemented to display a list of all of the contacts that are
stored within the 'contacts'list. I then added the search_contact () function to allow the user to search a contact by their name.
I then went added and added a main menu that would allow the user to navigate through the Contact Main Menu, with the use of a 'while' loop. 
The user would have the choice of entering option 1, 2, 3, or 4 and depending on the user's choice would determine whether the 'add_contact()', 'view_contacts()', 
or the 'search_contact()' functions would appear or if the user would like to exit the program. In addition, I went ahead and implemented an error message should
the user fail to enter a valid option in the main menu. 