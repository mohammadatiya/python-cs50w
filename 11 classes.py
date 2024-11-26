class point(): #Defines a new class named point.
    def __init__(Self, input1, input2): #The __init__ method puts everything together (assigns these values to x and y).
      #The self keyword helps the class distinguish between one (object) and another.
      
      Self.x = input1
      Self.y = input2 #Assign the value of input2 to the object’s y attribute.

p = point(2, 8)
print(p.x) # . dot means go into the point and access data inside the point
print(p.y)

