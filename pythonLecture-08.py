# ------------ Lecture started ----------------
# python Function & def
def greet():
  print("Welcome to our class")
greet()

# function with parameter
def greetwithname(name):
  print(f"Hello {name} Welcome to our class")
name = input("Enter your name: ")
greetwithname(name)

# function with return
def greetithname(name):
  return f"Hello {name} Welcome to our class"
name = input("Enter your name: ")
greetwithname(name)

# function to add 2 numbers and print sum
def add(num1, num2):
  sum = num1 + num2
  print(f"The sum of {num1} and {num2} is: {sum}")
add(7,8)

# function with default parameter
def user (name = "Guest"):
  print(f"Hello {name}")
user()
user("Amit Roy")

# function with multiple value return
def getInformation():
  x = 80
  y = 90
  return x,y

print(getInformation())
# print(getInformation([0]))

# function with DocString (Documented String)
def docString(name = "Jui"):
  """ Print a wlcome message to the user"""
  # """ Print a wlcome message to the user"""
  print(f"Hello {name}")
docString()

