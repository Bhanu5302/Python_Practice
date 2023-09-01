"""
Special Symbols Used for passing arguments in Python:

*args (Non-Keyword Arguments)
**kwargs (Keyword Arguments)

These are used when have a doubt how many arguments are to be pass in to the function
"""
def add(a,b,*args):
    print(a+b)

add(2,3)

#-------------------
def myfunc(*argv):
    for x in argv:
        print(x)

myfunc("bhanu","prakash","mamidi")

#-------**kwargs uses key & value---------

def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")