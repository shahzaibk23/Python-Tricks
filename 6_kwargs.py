#-------------------------- **kwargs ----------------

dict = {"a":1, "b":2, "c":3}

def aFunction(a,b,c):
    print(a + b +c)

#these do the same thing
aFunction(1,2,3)
aFunction(**dict)
