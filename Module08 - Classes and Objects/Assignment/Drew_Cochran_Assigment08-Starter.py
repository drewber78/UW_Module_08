# ------------------------------------------------------------------------ #
# Title: Assignment 08 - Final
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Drew Cochran, 06MAR2023,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

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

    # Class variable
    product_tuple = ()


    # Constructor
    def __init__(self, product_name, product_price):
        """
        Init function for the class. Defines product standard price and product name for use within the object.
        """

        # Establishes initial variables
        self._product_name = product_name
        self._product_price = product_price

    # Get to return product name
    @property
    def get_product_name(self):
        return str(self._product_name).title()

    # Setter for the name, then function to check if the value passed is numericly False.
    # @product_name.setter
    def set_product_name(self, value):
        try:
            if str(self._product_name).isnumeric() == False:
                raise ValueError
            else:
                self._product_name = value
        except ValueError as v:
            print(v)
            print("Product name must be alphabet characters only.")

    # Get to return product price
    @property
    def get_product_price(self):
        return float(self._product_price)

    # Setter for product price. Checks to make sure value is numericly True.
    # @product_price.setter
    def set_product_price(self, value):
        try:
            if self._product_price.isnumeric() == True:
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
        return self.to_string()

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

    def ReadFile(self):
        """
        Reads the data from products.txt into lstOfProductObjects for future use.
        """

        # Function to read the file products.txt into memory for manipulation and display later in the program
        # Try for seeing if file is in home dictionary of program
        try:
            objProductsList = open("products.txt", "r")
            for row in objProductsList:
                lstRow = row.split(",")
                dicRow = {"Product": lstRow[0], "Price": lstRow[1].strip()}
                lstOfProductObjects.append(dicRow)
            objProductsList.close()

        # Print error statement prompting user to locate file needed to run program
        except:
            print("File not found. Locate products.txt and ensure file is in the same directory as program.")

    # TODO: Add Code to process data to a file

    def WriteFile(self):
        """
        Writes the data from lstOfProductObjects to products.txt and closes file. Overwrites all existing data.
        """
        # Opens file
        objProductsList = open("products.txt", "w")

        # Iterate through lstOfProductObjects to then write to products.txt. Adds a comma and a new line after each
        # list item pair of product_name and product_price
        for row in lstOfProductObjects:
            objProductsList.write(str(row["Product"]) + ', ' + str(row["Price"]) + '\n')

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
    def UserChoice(self):
        """
        Grabs inputted user's choice and returns value.
        """

        strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
        return strChoice

    # TODO: Add code to show the current data from the file to user
    def print_current_list_items(self):
        """
        Function to display data from lstOfProductObjects.
        """
        # for loop to iterate through lstOfProductObjects
        for row in lstOfProductObjects:
            print(row, sep='\n', end='\n')
        return

    # TODO: Add code to get product data from user
    def input_product_data(self):
        """
        Takes inputed user data and adds to lstOfProductObjects
        """
        while(True):
            print("Type exit at any prompt to exit to main menu.")

            # User input for product name
            strProduct = str(input("What is the product name, one word only? "))
            # if check for use of exit word
            if strProduct.lower == 'exit':
                break

            # User input for product price
            fltPrice = input("What is the product price? ")
            # if check for use of exit word
            if fltPrice.lower == 'exit':
                break
            float(fltPrice)

            # Create Product class object with new user data
            objProduct = Product(strProduct, fltPrice)
            dicRow = {"Product" : objProduct.get_product_name, "Price" : objProduct.get_product_price}
            lstOfProductObjects.append(dicRow)


# Presentation (Input/Output)  -------------------------------------------- #


# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #

