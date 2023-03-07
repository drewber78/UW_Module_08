# ------------------------------------------------- #
# Title: Listing10 - Class Docstring
# Description: A class with a docstring
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #

class Person:
    """Stores data about a person:

    properties:
        first_name: (string) with the person's first name
    methods:
        static: get_object_count() -> int with number of object instances created
    changeLog: (When,Who,What)
        RRoot,1.1.2030,Created Class
    """
    # pass is used as a temporary placeholder for code that will be added
    pass  # TODO: Add code to the class

# --- Use the class ----


print(Person.__doc__)   # You don't use () for this one, because it actually a field
print(list.__doc__)   # Here is one from the Python programmers.

