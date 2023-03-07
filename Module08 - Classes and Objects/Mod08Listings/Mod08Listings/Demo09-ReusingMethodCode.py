# ------------------------------------------------- #
# Title: Demo-09-Reusing method code
# Description: A class methods
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #

# --- Make the class ---
class Person:

    # -- Constructor --
    def __init__(self, first_name, last_name):
        # Use a property to set the attribute
        self.first_name = first_name
        self.last_name = last_name

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

    @property  # You don't use for the getter's directive!
    def last_name(self):  # (getter or accessor)
        return str(self.__last_name).title()  # Format attribute as Title case

    @last_name.setter  # The @NAME.setter must match the getter's name!
    def last_name(self, value):  # (setter or mutator)
        if str(value).isnumeric() == False:
            self.__last_name = value
        else:
            raise Exception("Names cannot be numbers")

    def to_string(self):
        """  Returns object data in a comma separated string of values

        :return: (string) CSV data
        """
        object_data_csv = self.first_name + ',' + self.last_name
        return object_data_csv

    def __str__(self):
        """  Overrides Python's built-in method to
             return object data in a comma separated string of values

        :return: (string) CSV data
        """
        return self.to_string()
# --End of class--

# --- Use the class ----
objP1 = Person("bob", "smith")
print(objP1.to_string())
print(objP1.__str__())
print(objP1)






































