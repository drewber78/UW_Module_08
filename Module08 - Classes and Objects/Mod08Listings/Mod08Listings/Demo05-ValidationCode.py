# ------------------------------------------------- #
# Title: Demo05- Validation Code
# Description: A class with an attribute
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #

class Person(object):

    # -- Constructor --
    def __init__(self, first_name):
        # Attributes
        self.first_name_str = '' # declare the attributes first
        try:
            if str(first_name).isnumeric():  # test that parameter data is valid
                raise ValueError
            else:
                self.first_name_str = first_name.title()  # set and format attribute
        except ValueError as v:
            print(v)
            print('Names must include at least one alpha character!')

# --End of class--

# --- Use the class ----
objP1 = Person("bob")
print(objP1.first_name_str)
objP1 = Person("123")
print(objP1.first_name_str)

# However, it does not stop us from using numbers later(an issue we will fix shortly!)
objP1.first_name_str = '123'
print(objP1.first_name_str)