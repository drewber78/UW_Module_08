# ------------------------------------------------- #
# Title: Demo04 - Attributes
# Description: A class with an attribute
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #

class Person(object):
    # --Fields--
    # first_name_str = ""  <- Delete this. Python does not use fields for instance data

    # -- Constructor --
    def __init__(self, first_name):
        #Attributes
        self.first_name_str = first_name  # You use attributes instead!
        # Note that attributes can have the same name as parameter
        # due to the context determined by the self keyword.

# --End of class--

# --- Use the class ----
objP1 = Person("Bob")
print(objP1.first_name_str)
