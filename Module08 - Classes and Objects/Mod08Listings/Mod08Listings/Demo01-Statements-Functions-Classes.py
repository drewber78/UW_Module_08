# ------------------------------------------------- #
# Title: 01-Statements-Functions-Classes
# Description: A statements, functions, and classes
# ChangeLog: (Who, When, What)
# RRoot,1.1.2020,Created Script
# ------------------------------------------------- #

# Modern programs are usually created using these three components:

# Statements
data_int = 123  # Data assignment statement
if data_int == 123:  # Conditional statement
    data_int = 123 + 4  # Processing statement
print(data_int)  # Calling the print() function


# Functions
def organize_statements():
    data_int = 123  # Data assignment statement
    if data_int == 123:  # Conditional statement
        data_int = 123 + 4  # Processing statement
    print(data_int)  # Calling the print() function


# Classes
class organize_functions:

    @staticmethod
    def organize_statements():
        data_int = 123  # Data assignment statement
        if data_int == 123:  # Conditional statement
            data_int = 123 + 4  # Processing statement
        print(data_int)  # Calling the print() function


# ---------------------------

input("Press enter to call the function in the main body of the script")
organize_statements()

# Call the function within the class (aka. Method)
input("Press enter to call the class function (aka. Method)")
organize_functions.organize_statements()
