class Flight () : 
    def __init__ (self, capacity) :
     self.capacity = capacity   
     self.passengers = [] #[] for creating an empty list: to store a seqance of valus 
     
    def add_passengers(self, name,): #this is a function to add the passengers with there names
        if not self.open_seats():
          return False 
        self.passengers.append(name) #this to let the name go to the list passengers by using append : add a value to the end of exesting list 
        return True 
 
    def open_seats(self): #  calculates and returns the number of seats available in an object
         return self.capacity - len(self.passengers) # - : s the subtraction operator, and it is used to calculate the remaining seats by subtracting the number of occupied seats (self.passengers) from the total capacity (self.capacity). && and len to get the number of passengers are in the list
         
flight = Flight (3) # Flisght: class so (3) is for the capacity & flight: an object

people = ["Harry", "Jack", "Masty", "winte"]
for person in people:
 success = flight.add_passengers(person)
 if success:
    print(f"Welcome Ms/Mr {person} in board there is an open seat for you!")
 else:
    print(f"Sorry Ms/Mr {person} there is no open seat at the moment becouse the capacity of the seats is 3 only.")


    # this is a prif about how the oop can be in Python