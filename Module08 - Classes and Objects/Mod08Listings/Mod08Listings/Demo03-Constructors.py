# ------------------------------------------------- #
# Title: Demo03-Constructors
# Description: A class with a constructor
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #

class Person(object):
    # --Fields--
    first_name_str = ""

    # -- Constructor --
    def __init__(self, first_name=''):  # The default is an empty string
        # -- Attributes --
        self.first_name_str = first_name

    # -- Properties --
    # -- Methods --


# --End of class--

# --- Use the class ----
objP1 = Person()  # With no arguments
objP1.first_name_str = "Bob"

objP2 = Person(first_name="Sue")  # With one parameter and argument

print(objP1.first_name_str)  # Will be empty because there was no argument
print("-------------")
print(objP2.first_name_str)  # Will have first name of Sue
