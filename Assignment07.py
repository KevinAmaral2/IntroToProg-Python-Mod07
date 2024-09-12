# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   Kevin Amaral,9/11/24,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.


# TODO Create a Person Class
class Person:
    """
       A class representing person data.

       Properties:
           first_name (str): The student's first name.
           last_name (str): The student's last name.
            XX
       ChangeLog:
           - KA, 9/11 Created the class.
       """

#Create a constructor with private attributes for the first_name and last_name data
    def __init__(self, first_name: str = '', last_name: str = ''):
           self.first_name = first_name
           self.last_name = last_name

# TODO Create a getter and setter for the first_name property
    @property  # (Use this decorator for the getter or accessor)
    def first_name(self):
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha() or value == "":  # is character or empty string
            self.__first_name = value
        else:
            raise ValueError("The last name should not contain numbers.")


# TODO Create a getter and setter for the last_name property (Done)
@property
def last_name(self):
    return self.__last_name.title()  # formatting code

@last_name.setter
def last_name(self, value: str):
    if value.isalpha() or value == "":  # is character or empty string
        self.__last_name = value
    else:
        raise ValueError("The last name should not contain numbers.")


# TODO Override the __str__() method to return Person data (done)

    def __str__(self):
        return f'{self.first_name},{self.last_name}'

# TODO Create a Student class the inherits from the Person class (Done)
class Student(Person):
    """
       A class representing Student data.

       Properties:
           first_name (str): The student's first name.
           last_name (str): The student's last name.

       ChangeLog:
           - KA, 9/11 Created the class.
       """

# TODO call to the Person constructor and pass it the first_name and last_name data

    def __init__(self, first_name: str = '', last_name: str = '', course_name: str = ''):
        # self.first_name = first_name
        # self.last_name = last_name
        super().__init__(first_name=first_name, last_name=last_name)
        self.course_name = course_name

    # TODO add the getter for course_name (Done)

    @property
    def course_name(self):
        return self.__course_name

    # TODO add the setter for course_name (Done)
    @course_name.setter
    def course_name(self, value: str):
        try:  # using a try block to capture when an input cannot be changed to a float
            self.__course_name = value
        except ValueError:
            raise ValueError("course must be a numeric value.")

 # @property  # (Use this decorator for the getter or accessor)
    # def first_name(self):
    #     return self.__first_name.title()  # formatting code
    #
    # @first_name.setter
    # def first_name(self, value: str):
    #     if value.isalpha() or value == "":  # is character or empty string
    #         self.__first_name = value
    #     else:
    #         raise ValueError("The first name should not contain numbers.")
    #
    # @property
    # def last_name(self):
    #     return self.__last_name.title()  # formatting code
    #
    # @last_name.setter
    # def last_name(self, value: str):
    #     if value.isalpha() or value == "":  # is character or empty string
    #         self.__last_name = value
    #     else:
    #         raise ValueError("The last name should not contain numbers.")


# TODO add an assignment to the course_name property using the course_name parameter (Done)



# TODO Override the __str__() method to return the Student data (Done)
    def __str__(self):
        return f'{self.first_name},{self.last_name},{self.__course_name}'

# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    KA, 9/11 Created the class
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a json file and loads it into a list of dictionary rows

        ChangeLog: (Who, When, What)
        KA, 9/11 Created the function

        :param file_name: string data with name of file to read from
        :param student_data: list of dictionary rows to be filled with file data

        :return: list
        """

        try:
            file = open(file_name, "r")

            list_of_dictionary_data = json.load(file)  # the load function returns a list of dictionary rows.
            for student in list_of_dictionary_data:
                student_object: Student = Student(first_name=student["FirstName"],
                                                  last_name= student["LastName"],
                                                  course_name=student["CourseName"])
                student_data.append(student_object)

            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        KA, 9/11 Created the function

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be writen to the file

        :return: None
        """

        try:
            list_of_dictionary_data: list = []
            for student in student_data:
                student_json: dict \
                    = {"FirstName": student.first_name, "LastName": student.last_name, "CourseName": student.course_name}
                list_of_dictionary_data.append(student_json)

            file = open(file_name, "w")
            json.dump(list_of_dictionary_data, file)
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    KA, 9/11 Created the class
    KA, 9/11,Added menu output and input functions
    KA, 9/11,Added a function to display the data
    KA, 9/11,Added a function to display custom error messages
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

        ChangeLog: (Who, When, What)
           KA, 9/11 Created the function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        KA, 9/11 Created the function

        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        KA, 9/11 Created the function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        """ This function displays the student and course names to the user

        ChangeLog: (Who, When, What)
        KA, 9/11 Created the function

        :param student_data: list of student object data to be displayed
        :return: None
        """
        message:str = ''
        print("-" * 50)
        for student in student_data:
            message =  "{} {} registered for course {} "
            #print(f'Student {student["FirstName"]} '
             #     f'{student["LastName"]} is enrolled in {student["CourseName"]}')
            print(message.format(student.first_name, student.last_name, student.course_name))
        print("-" * 50)
        print()

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the student's first name and last name, with a course name from the user

        ChangeLog: (Who, When, What)
        KA, 9/11 Created the function

        :param student_data: list of dictionary rows to be filled with input data

        :return: list
        """

        try:
            # Input the data
            student = Student()
            student.first_name = input("What is the student's first name? ")
            student.last_name = input("What is the student's last name? ")
            student.course_name = str(input("What is the student's course? "))
            student_data.append(student)

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data


# Start of main body

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
