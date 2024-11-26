# what house each of student of harvard happen to be
#*the way to define Dictionary is by define a key calling a value

houses = {"Harry": "Gryffindor", "Draco": "Slytherin"} 
#Harry & Draco are the key + Gryffindor & Slytherin are the value

houses["Hermino"] = ["Gryffindor"] #means: look up Hermino in the houses Dictionary and when u do that its gonna be = to the value = Gryffindor.

print(f"Harry's House: {houses['Harry']}, Draco's House:{houses['Draco']}, Hermino's House: {houses['Hermino']}.") #means:got to Dictionary of houses and give me the value of the key Harry and the same for Draco
#*The print() function outputs the result to the console.
#** The f at the beginning tells Python to treat the string as an f-string. Anything inside the curly braces {} will be evaluated and then inserted into the string
#***Using houses['Harry'] and houses['Draco'] to get values from the houses dictionary.

 