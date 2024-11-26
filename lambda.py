# this is a list inside it is a dect
people =  [ {"name": "Harry", "house": "Gryffindor"}, 
            {"name": "Cho", "house": "Ravenlaw"}, 
            {"name": "Draco", "house": "Slytherin"} 
          ]



#def f(person):
   # return person["house"]
   # people.sort(key=f)

#*how to applay lambda:
people.sort(key=lambda person:person["name"])


print(people)







