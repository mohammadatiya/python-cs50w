#n = input("Number: ")

#if n > 0:
    #print("n is positive")
#elif n < 0:
    #print("n is negative")    
#else:
    #print("n is 0")
#when the code gonna run its gonna be givin an error
#becouse n is a string no matter what value is gonna be
#but its define as a string and "0" is an int and its can not do the >< with a string and int 
#Solutin: convert n to an int by using a function in PY : int()

n = int (input("Number: "))

if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")    
else:
    print("n is 0")
