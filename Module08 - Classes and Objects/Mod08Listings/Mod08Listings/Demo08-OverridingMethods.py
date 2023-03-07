# ---------------------------------------------------------------- #
# Title: Demo-08-Overriding the built-in __str __() method
# Description: A overriding the __str__() method
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ---------------------------------------------------------------- #

class Demo1:
    var1 = "Some Data"

obj1 = Demo1()  # This object uses the default __str__() method
print(obj1.__str__())

class Demo2:
    var1 = "Some Data"
    def __str__(self):
        return '<' + self.var1 + '>'

obj2 = Demo2()  #  object uses the overridden __str__() method
s = str(obj2)
print(str(obj2))  # str() automatically calls the  __str__() method
print(obj2)  # print() function automatically calls the  __str__() method
print(obj2.__str__())  # but you can also call the __str__() method directly

# Python's List class overrides the __str__() method too, but it is not very useful.
data_lst = [1,2,3]
print(data_lst)
