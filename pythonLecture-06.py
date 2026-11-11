# Lists, Tuples and Dictioneries
mylist = ["apple", "banana", "cherry"]
print(mylist)
print(len(mylist))
print(type(mylist))


# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# Tuple practices
mytuple = ("apple", "banana", "cherry")
print(mytuple)
print(len(mytuple))
print(type(mytuple))

# SET Practices
myset = {"apple", "banana", "cherry"}
print(myset)
print(len(myset))
print(type(myset))


# Dictioneries practices
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(len(thisdict))
print(type(thisdict))

# ---------------------------------------------------
# Lecture started on list
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(fruits[0])
# print(fruits[-1])
print(fruits[2:5])
print(fruits[:4])
print(fruits[2:])
print(fruits[-4:-1])

fruits.append("Kamranga") #add items at last position
print(fruits)

fruits.insert(1, "lemon")
print(fruits)

fruits.remove("kiwi")
print(fruits)

fruits.pop()
print(fruits)

del fruits[0]
print(fruits)

fruits.clear()
print(fruits)

# Print list with for loop
for element in fruits:
  print(element)

# Print list with while loop
i = 0
while i < len(fruits):
  print(fruits[i])
  i = i + 1

# List with numeric
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(numbers)) # len = length of the list -- how many item
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sum(numbers)/len(numbers)) # need average by installing library

print(numbers[2:])
print(numbers[:6])

# list [start:stop:step]
print(numbers[::2])
print(numbers[1::2])
print(numbers[1:6:2])

# ------------ Tuple-------------
#Tuple practices
info = ("Manik", 28, "Engineer")
print(info[1])
print(len(info))
print(type(info))

for element in info:
  print(element)

# ---------------------------------------------------
# packing and unpacking
person = ("Manik", 28, "Engineer")
name, age, profession = person
print(name)
print(age)
print(profession)


# ------------------ dictiony----------
# Dictioneries practices
studentDictionary = {
  "name": "Frog",
  "age": 23,
  "email": "pqr@xyz.com"
}
print(studentDictionary["name"])
print(studentDictionary)
print(len(studentDictionary))
print(type(studentDictionary))