#----------DOCSTRING------------

def myFunc():
    #declaring DOCSTRING
    "This is the description of my function."

#calling DOCSTRING
print(myFunc.__doc__)

#OR
help(myFunc)

#  DOCSTRINGS can also be used wih classes and methods

class myClass:
    "This is the DOCSTRING of my class"

    def myMethod(self):
        "This is the DOCSTRING of my method"

help(myClass)
help(myClass.myMethod)