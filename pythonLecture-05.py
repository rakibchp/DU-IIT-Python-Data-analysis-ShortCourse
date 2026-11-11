# In range of (1, 50) find out the first sivisible number by 7
for num in range(1, 50):
    if num % 7 == 0:
        print(f"{num} is the first divisible number by 7")
        break

# Print only the odd number from 1 to 20
for oddNumber in range (1, 20, 2):
  print(oddNumber)

#----------- another way ------------
for number in range(1,21):
  if number % 2 == 0:
      continue
  print(number)


# printing a pattern with ( * )
for patternPrinter in range(1,6):
  print(patternPrinter * "*")

# another way of printing a pattern with nested loop
rows = 6
for row in range(1, rows+1):
    for col in range(row):
        print("*", end = " ")
    print("")

# another way of printing a pattern using while loop
rows = 6
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print("*", end = " ")
        j = j + 1
    i = i + 1
    print("")


# print 1 to 10 using while loop
number = 1
while number <= 10:
    print(f" number is : {number}")
    number = number + 1

# print 10 to 1 using while loop (reverse printing)

number = 10
while number >= 1:
    print(f"reverse printing : {number}")
    number = number - 1


# Using while loop print 20 to 5
number = 20
while number >= 5:
    print(f"reverse printing : {number}")
    number = number - 1

# Using while loop, print leap year from 1990 to 2026

number = 1990
while number <= 2026:
    print(f"leap year : {number}")
    number = number + 4

# correct leap year counting 
number = 1990

while number <= 2026:
    if number % 400 == 0 or (number % 4 == 0 and number % 100 != 0):
        print(f"Leap year: {number}")

    number = number + 1

# how to get user input
rows = int(input("How many rows: "))
for row in range(1, rows+1):
    for col in range(row):
        print("*", end = " ")
    print("")


# taking user input and adding/sum them util 0 -- using while loop
userInput = int(input("Enter a number: "))
sum = 0
while userInput != 0:
    sum = sum + userInput
    userInput = int(input("Enter a number: "))
print(f"Cumulative sum is: {sum}")


# ask password while incorrect
password = "iit123"
userInput = str(input("Enter your password: "))
while userInput != password:
    userInput = str(input("You are wrong! Enter your password again: "))
print(f"Congrats!")
print(f"You Entered Correct Password: {userInput}")