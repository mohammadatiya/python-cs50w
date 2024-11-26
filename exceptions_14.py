import sys #this for closing the program 
try:
    x =  int(input("x: "))
    y =  int(input("y: "))
except ValueError: # this is for words!
    print("Erorr: latter detected, use numbers only!")
    sys.exit(1)

#*How to solve isuue(0) :
try: #this for trying !
    result = x / y 
except ZeroDivisionError: # if the program crash in this Erorr
    print("Erorr: Connot divide by 0.")
    sys.exit(1) # (1) means somthing went wrong in the program

print(f"{x} / {y} = {result}")

#*The exceptions is issue (0) : 
#x: 5
#y: 0

    #results = x /y
#ZeroDivisionError: division by zero
