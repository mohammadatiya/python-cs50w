# decorators: the idea of it : taking a function and moldfying/add additonal behavior to that function 
# decorators : its a functoin that take the function input and returens a moldfed function '

def announce(f):
    def wrapper():
        print("About to run the function.")
        f() # its for the announce def
        print("Done with the function. ")
    return wrapper


@announce # this is how to add a decorators
def hello():
    print("hello, world")

hello()