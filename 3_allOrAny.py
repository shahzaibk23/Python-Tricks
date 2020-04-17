#---------- All or Any ------------

lst = [True, True, False]

if any(lst):
    print("Atleast one is True")

if all(lst):    # lst = [True,True,True]
    print("all are True")

if any and not all(lst):
    print("atleast one True and one False")
