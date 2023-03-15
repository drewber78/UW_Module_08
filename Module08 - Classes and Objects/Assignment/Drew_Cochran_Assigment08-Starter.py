# ------------------------------------------------------------------------ #
# Title: Assignment 08 - Final
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudocode to start assignment 8
# Drew Cochran, 06MAR2023,Modified code to complete assignment 8
# Drew Cochran 11MAR2023, Completed Product, FileProcessor, and IO class; need to write main body script
# Drew Cochran, 13MAR2023, Changed code to work through objects rather than a dictionary of objects; completed
#                       main body of script; ready for debugging.
# Drew Cochran, 14MAR2023, Debugging file save and reading features, print list of items, and various other issues
#
# ------------------------------------------------------------------------ #

# imports into code
import os

# Data -------------------------------------------------------------------- #

strFileName = 'products.txt'
lstOfProductObjects = []
strExit = 'exit'


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name

        product_price: (float) with the product's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Drew Cochran, 06MAR2023, Modified code to complete assignment 8
        Drew Cochran, 08MAR2023, Continued modifying class to complete assignment 8
    """

    # TODO: Add Code for Product class (Constructor, Properties, & Methods)

    # Constructor
    def __init__(self, product_name, product_price):
        """
        Init function for the class. Defines product standard price and product name for use within the object.
        """

        # Establishes initial variables
        self._product_name = product_name
        self._product_price = product_price

    # Get to return product name
    # @property
    def get_product_name(self):
        return self._product_name.title()

    # Setter for the name, then function to check if the value passed is numerically False.
    # @product_name.setter
    def set_product_name(self, value):
        try:
            if str(self._product_name).isnumeric() is False:
                raise ValueError
            else:
                self._product_name = value
        except ValueError as v:
            print(v)
            print("Product name must be alphabet characters only.")

    # Get to return product price

    def get_product_price(self):
        return float(self._product_price)

    # Setter for product price. Checks to make sure value is numerically True.

    def set_product_price(self, value):
        try:
            if self._product_price.isnumeric() is True:
                self._product_price = value

            else:
                raise ValueError

        except ValueError as v:
            print(v)
            print("Product price must be a numeric value.")

# Data -------------------------------------------------------------------- #

    # @staticmethod
    # def product_list(product_name, standard_price):
    #     """
    #     Object that takes in the product name and the product price. Creates a list, and appends data to the list
    #     everytime time it is used. Able to be recalled when writing to a file. List is used to store data when reading
    #     in from a file.
    #     """
    #
    #     # Adds data from Product class object product_name and product_price to lstOfProductObjects

    @staticmethod
    def to_string(self):
        """
        Returns the product name and product price as a string with a comma and space inbetween..
        """
        object_data = self._product_name + ', ' + self._product_price
        return object_data

    def __str__(self):
        """
        Returns to_string. Overrides default Python string function.
        :return: to_string function
        """
        return self.to_string(self)


# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """

    # TODO: Add Code to process data from a file

    def __init__(self):
        """
        Init for class
        """

    @staticmethod
    def read_data_from_file():
        """
        Reads the data from products.txt into lstOfProductObjects for future use.
        """

        # Function to read the file products.txt into memory for manipulation and display later in the program
        # Try for seeing if file is in home dictionary of program

        # if check to see if file exists; else, file is created via append
        isExisting = os.path.exists(os.getcwd() + "/" + os.path.normpath(strFileName))
        if isExisting is True:
            try:
                objProductsList = open(os.getcwd() + "/" + strFileName, "r")
                for row in objProductsList:
                    lstRow = row.split(",")
                    objRow = Product(lstRow[0], lstRow[1])
                    lstOfProductObjects.append(objRow)
                objProductsList.close()

            # Print error statement prompting user to locate file needed to run program
            except TypeError as v:
                print(v)
                print("File not found. Locate products.txt and ensure file is in the same directory as program.")

        else:
            objProductsList = open(os.getcwd() + "/" + os.path.normpath(strFileName), "a")
            objProductsList.close()

    # TODO: Add Code to process data to a file
    @staticmethod
    def save_data_to_file():
        """
        Writes the data from lstOfProductObjects to products.txt and closes file. Overwrites all existing data.
        """

        # Opens file
        objProductsList = open(os.getcwd() + "/" + os.path.normpath(strFileName), "w")

        # Iterate through lstOfProductObjects to then write to products.txt. Adds a comma and a new line after each
        # list item pair of product_name and product_price
        for row in lstOfProductObjects:
            name = str(row.get_product_name())
            price = str(row.get_product_price())
            objProductsList.write(name + ', ' + price + '\n')

        # closes file and prints success statement
        objProductsList.close()
        print("Items saved successfully to products.txt")


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """  A class for performing Input and Output

    methods:
        print_menu_items():

        print_current_list_items(list_of_rows):

        input_product_data():

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class:
    """

    def __int__(self):
        """
        Init for class
        """

    # Add code to show menu to user (Done for you as an example)
    @staticmethod
    def print_menu_items():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current data
        2) Add a new item.
        3) Save Data to File
        4) Exit Program
        ''')
        print()  # Add an extra line for looks in the terminal window

    # TODO: Add code to get user's choice
    @staticmethod
    def UserChoice():
        """
        Grabs inputted user's choice and returns value.
        """

        strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
        return strChoice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def print_current_list_items():
        """
        Function to display data from lstOfProductObjects.
        """
        # for loop to iterate through lstOfProductObjects
        for row in lstOfProductObjects:
            printName = row.get_product_name()
            printPrice = row.get_product_price()
            print("%s, %d" % (printName, printPrice), sep='\n', end='\n')
        # return

    # TODO: Add code to get product data from user

    def input_product_data(self, strProduct, fltPrice):
        """
        Takes inputted user data and adds to lstOfProductObjects
        """

        # Create Product class object with new user data
        objProduct = Product(strProduct, fltPrice)
        lstOfProductObjects.append(objProduct)
        print("Product data successfully added to list")


# Presentation (Input/Output)  -------------------------------------------- #


# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body

# Load data from file into a list of product objects when script starts
FileProcessor.read_data_from_file()

# Show user a menu of options
while True:
    IO.print_menu_items()
    # Get user's menu option choice
    choice_str = IO.UserChoice()

    # if checks for user selected menu option
    # Show user current data in the list of product objects
    if choice_str.strip() == '1':
        showLst = IO()
        showLst.print_current_list_items()
        continue

    # Let user add data to the list of product objects
    elif choice_str.strip() == '2':
        choice_two = IO()
        # While loop to allow user to continue inputting items until "exit" is typed
        while True:
            print("Type exit at any prompt to exit to main menu.")

            # User input for product name
            strProduct = str(input("What is the product name, one word only? "))
            # if check for use of exit word
            if strProduct.lower() == strExit:
                break

            # User input for product price
            fltPrice = input("What is the product price? ")
            # if check for use of exit word
            if fltPrice.lower() == strExit:
                break

            else:
                float(fltPrice)

            choice_two.input_product_data(strProduct, fltPrice)

        continue

    # let user save current data to file and exit program
    elif choice_str.strip() == '3':
        choice_three = FileProcessor()
        choice_three.save_data_to_file()
        print("Data saved.")
        continue

    # Exit program
    elif choice_str.strip() == '4':
        print("Goodbye!")
        break

    # else for if the user inputted anything other than 1, 2, 3, or 4
    else:
        print("Selection must be 1 thru 4.")

# Main Body of Script End  ---------------------------------------------------- #
