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
    """

    # TODO: Add Code for Product class (Constructor, Properties, & Methods)


    # Constructor
    def __init__(self, product_name, product_price):
        """
        Init function for the class. Defines product standard price and product name for use within the object.
        """
        # Establish initial variables for class and define types
        #product_name = ""
        #product_price = 0.0
        lst_product = []
        try:
            if str(product_name).isnumeric():
                raise ValueError
            else:
                self.product_name_str = product_name.title()
        except ValueError as v:
            print(v)
            print("Product name must be alphabet characters only.")

        self.product_price_flt = product_price



# Data -------------------------------------------------------------------- #

    @staticmethod
    def product_list(product_name, standard_price):
        """
        Object that takes in the product name and the product price. Creates a list, and appends data to the list
        everytime time it is used. Able to be recalled when writing to a file. List is used to store data when reading
        in from a file.
        """



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
    pass
    # TODO: Add Code to process data from a file
    # TODO: Add Code to process data to a file

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

    # TODO: Add code to show the current data from the file to user

    # TODO: Add code to get product data from user

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
