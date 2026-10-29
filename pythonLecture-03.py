# boolean conditions
is_sunny = True
is_rainy = False
print(is_sunny)
print(is_rainy)

temperature = 9
if temperature >= 25:
  print("It's a hot day")
else:
  print("It's not a hot day")

# Logical conditions
mark = 99
if 80<=  mark <=100:
  print("Excellent Studnet")
elif 75<=  mark <=80:
  print("Good Studnet")
else: print("Average Studnet")


## task -> from book, 3.3 & 3.4


## Logical operator
Apple = True
Banana = False
print(Apple and Banana)
print(Apple or Banana)
print(not Apple)
print(not Banana)

A = True
B = False
print(A and B)
print(A or B)
print(not A)
print(not B)

#------------for and --------------------
age = 25
has_license = True
if age> 20 and has_license:
  print("You can drive a car")
else:
  print("You cannot drive a car")


#------------for OR --------------------
dayName = ["Saturday", "Friday"]
isHoliday = True
if dayName == "Saturday" or dayName == "Friday" or isHoliday:
  print("Holiday")
else:
  print("working day")

