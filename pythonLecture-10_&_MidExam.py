# --------- Mid Exam -------------
# Answer to the Question No-1

numbers = [4, 10, 13, 15, 22, 25, 8]
sum = 0
for num in numbers:
    if num % 5 == 0:
        sum += num
print(sum)

# Answer to the Question No-2

for i in range(4, 0, -1):
    print('*' * i)

# Answer to the Question No-3

user_input = input("Enter a word: ")
while user_input != 'stop':
    print("You Entered: ", user_input)
    user_input = input("Enter a word: ")


# Answer to the Question No-4

examFee = int(input("Enter Exam Fee: "))
attendance = int(input("Enter Attendance: "))


if examFee == 1:
    if attendance >= 75:
        print("Congratulations! You are eligible for the exam.")
    else:
        print("Sorry, insufficient attendance.")
else:
    print("Exam fee payment required.")


# Answer to the Question No-5

def show_order(product_name, quantity):
    print(f"You ordered {quantity} {product_name}s")
show_order(product_name = input("Enter Product Name: "), quantity = int(input("Enter Quantity: ")))
