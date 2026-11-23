# Question 01 - add prices above a limit
# A small store has the item prices [12, 25, 7, 30, 18, 40]. Use a laptop to calculate the total prices that are 20 or more.

prices = [12, 25, 7, 30, 18, 40]
total = 0

for price in prices:
    if price >= 20:
        total += price
print("total: ", total)

# Question 02 - The temperature readings are []. Count how many readings are below zero. Do not count zero itself.
count = 0
readings = [6, -3, 0, -1, 8, -5, 2]
for reading in readings:
    if reading < 0:
        count += 1
print("count of less than zeros: ", count)

# Question 03 - Use a for loop to display five rows. In row 1 print 1, in row 2 print 22, continue through row 5. 
# Hint: number multiply with String

for num in range(1,6):
    print(str(num)*num)


# Question 04 - print multiplier of 6 for 6 times 
nums = 6
for num in range(1,6):
    print(nums, "x", num, "=", num*nums)

# Question 05 - Start from 5 and print each number down to 1 using a while loop. After the loop, print Go!

count = 5
while count >= 1:
    print(count)
    count -= 1
print("Go!")

# -------------------------------- with for loop ---------------------------------

for num in range(5, 0, -1):
    print(num)
print("Go!")

# Question 06 - 
value = int(input("Enter a positive number: "))
while value <= 0:
    print("That's not a positive number! Try again.")
    value = int(input("Enter a positive number: "))
print(f"Great - you entered a number over 0 that is: {value}")

# Question 07 - 
number = 345
digit_sum = 0
for digit in str(number):
    digit_sum += int(digit)
print(digit_sum)

# using while loop
number = 345
digit_sum = 0
while number > 0:
    digit = number % 10
    digit_sum += digit
    number //= 10
print("Result is: ",digit_sum)

# Question 08 -
score = int(input("Enter your score: "))
if score >= 80:
    print("Excellent")
elif score >= 80:
    print("Satisfactory")
elif score >= 50:
    print("Needs practice")


# Question - 09
