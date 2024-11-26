#name = "Harry"
#print(name[2]) #*its will print the letter 2 where it taks the name as a sequence 

#names = ["Harry", "Ron", "Hermione"]   #*its deals with the valus inside the [] as a sequnence so every name is have a namber not every letter
#print(names[0])

#*List: An ordered, mutable collection of elements that allows duplicates and supports indexing.
#*Tuple: An ordered, immutable collection of elements that allows duplicates and supports indexing.
#*Set: An unordered collection of unique elements, useful for membership testing and removing duplicates.
#*Dictionary: A collection of key-value pairs where keys are unique and used to access corresponding values.
#***Where its possiople to have a dict inside of a list and so on and on ....

from PIL import Image #*pip install pillow: this how to instal the libary by writing this in the command or in the termeneal if its not dawnloaded yet 
# Open and display a local image
image = Image.open(r"C:\Users\Hp\Desktop\cs50W\3 Python\4 sequences img.png")#when writing the path of an img its not gonna open as it is to make it work and open: is to add r before the "" which is :Raw Strings (r"...") or or : puting anther \with every exested \
image.show()#this is to open th img from its path

#*Tuple:
coordinateX = 10.0
coordinateY = 20.0

coordinate = (10.0, 20.0)

#*in files 5,6,7,.  gonna be examples for the List,Tuple, Set, Dictionary/dict
