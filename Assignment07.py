# --------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Demonstrates error handling and pickling.
# ChangeLog (Who,When,What):
# KRozanska,12.13.2020,Created Script
# --------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
import pickle

# Declare variables and constants
strFileName = "NameAndAge.dat"  # name of binary file
strAge = ""  # captures user's age
strName = ""  # captures user's name
lstTable = []  # list that acts as 'table'


class Error(Exception):
    """ Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """ Raised when the input value is too small"""
    pass


class ValueIncludesNumbersError(Error):
    """ Raised when the input includes a number"""
    pass


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def add_data_to_list(name, age, seconds, list_of_rows):
        """ Adds data into a list of dictionary rows

        :param name: (string) with user name:
        :param age: (float) with user age:
        :param seconds: (float) with user age in seconds:
        :param list_of_rows: (list) you will be adding row to
        :return: (list) of rows
        """
        row = [name, age, seconds]
        list_of_rows.append(row)
        return list_of_rows

    @staticmethod
    def pickle_the_data(file_name, list_of_rows):
        """ Pickles the data

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you will pickle:
        :return: (list) of rows
        """
        file = open(file_name, "wb")
        pickle.dump(list_of_rows, file)
        file.close()
        return list_of_rows

    @staticmethod
    def unpickle_the_data(file_name, list_of_rows):
        """ Unpickles the data

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you will unpickle:
        :return: (list) of rows
        """
        print("\nUnpickling list.")
        file = open(file_name, "rb")
        list_of_rows = pickle.load(file)
        print(list_of_rows)


# Presentation (Input/Output)  ---------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def input_age():
        """ Gets the age from user

        :return: float
        """
        while True:
            try:
                age = float(input("Enter your age in years - "))
            except Exception as e:
                print("That is not a valid age!")
                print(e)
                print()
            else:
                return age

    @staticmethod
    def input_name():
        """ Gets the name from user

        :return: string
        """
        while True:
            try:
                name = str(input("What is your name? - ")).strip()
                if len(name) < 2:
                    raise ValueTooSmallError
                elif name.isalpha() is False:
                    raise ValueIncludesNumbersError
            except ValueTooSmallError:
                print("Your name must be longer than one character.\n")
            except ValueIncludesNumbersError:
                print("You're not \"X Æ A-12\"! Enter a name that only has alphabetic characters.\n")
            except (TypeError, ValueError):
                print("Something went wrong! Retype your name.\n")
            else:
                return name

    @staticmethod
    def output_seconds():
        """ Calculates the seconds depending on user input

        :return: integer
        """
        seconds = int(strAge * 365 * 24 * 60 * 60)
        print("\nYou're over", seconds, "seconds old!")
        return seconds

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        input(optional_message)


# Main Body of Script  ------------------------------------------------------- #
print("\n\n\tHow many seconds old do you think you are?!\
      \n\tEnter you name and age to find out!\
      \n\tAt the end this data will be saved to a file.\n")

strName = IO.input_name()  # Captures user name
strAge = IO.input_age()  # Captures user age
strSec = IO.output_seconds()  # Calculates age into seconds
lstTable = Processor.add_data_to_list(strName, strAge, strSec, lstTable)  # Inputs data into a list

IO.input_press_to_continue("Press [Enter] to pickle this data!")
Processor.pickle_the_data(strFileName, lstTable)  # Pickles data

IO.input_press_to_continue("Press [Enter] to confirm data was pickled.")
Processor.unpickle_the_data(strFileName, lstTable)  # Unpickles data

print("\nGoodbye")
input("Press [Enter] to exit.")
