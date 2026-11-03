#for loop practice
# range [a, b]

number_seq = range(6)
print(number_seq)
print(type(number_seq))

number_list = list(number_seq)
print(number_list)
print(type(number_list))

#
list2 = list(range(50))
print(list2)

# task 81-200
list3 = list(range(81, 200))
print(list3)

# task conditional increment
list3 = list(range(81, 200,2))
print(list3)

list3 = list(range(81, 200,5))
print(list3)

EvenNumber = list(range(2, 200,2))
print(EvenNumber)

ReverseNumber = list(range(5, 205, -5))
print(ReverseNumber)


ReverseNumber = list(range(200, 0, -5))
print(ReverseNumber)

#print(reversed(ReverseNumber))


# print 0 to 100 using for loop
for i in range(101):
  print(i)


for i in range(2, 21, 2):
  print(i)
print(f"Final number is: " , i)



# calculate sum from  1 to 10
total = 0
print("Addition of numbers 1 to 10")
for number in range(1, 11):
  total = total + number
  print(f"adding {number}, running total is: {total}")
print(f"Cumulative of total is:", total)
