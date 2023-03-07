# ------------------------------------------------- #
# Title: Listing06 - Properties
# Description: A class with an attribute
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #

# --- Make the class ---
class Person:
    # --Fields--
    #strFirstName = ""

    # -- Constructor --
    def __init__(self, first_name):
        # Use a property to set the attribute
        self.first_name = first_name
        # The property and parameter can have the same name due to the self context

    # -- Properties --
    @property  # You don't use for the getter's directive!
    def first_name(self):  # (getter or accessor)
        return str(self.__first_name).title()  # Format attribute as Title case

    @first_name.setter  # The @NAME.setter must match the getter's name!
    def first_name(self, value):  # (setter or mutator)
        if str(value).isnumeric() == False:
            self.__first_name = value
        else:
            raise Exception("Names cannot be numbers")

# --End of class--

# --- Use the class ----
objP1 = Person("Bob")

objP1.first_name = 'robert'  # using the Setter property
print(objP1.first_name)  # using the Getter property

try:
    objP1.first_name = '123'  # testing that a number causes a validation ERROR
except Exception as e:
    print(e)