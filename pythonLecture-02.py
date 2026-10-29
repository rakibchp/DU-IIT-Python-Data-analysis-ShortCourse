# base version--> learning hash as comment in python
a = 10
b = 3
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a//b)

# ---------------------------------------
# -- selected code to run by shortcut --> ctrl+Alt+enter

x = 100
x%=5
print(x)

#----------- arithmetic operators
x, y , z = 10 ,20, 30
x-=4
y*=3
z%=7
# print("Here subtraction of X is: ", z + "test")
print(str("Here subtraction of X is: ") + str(x))
print(str("Here multiplication of Y is: ") + str(y))
print(str("Here modulas of Z is: ") + str(z))

#---------------------- logical operators
p1 = True
Q1 = False
print(p1 and Q1)
print(p1 or Q1)
print(not p1)
print(not Q1)

#---------------- Relational operators
n1 = 10
n2 = 20
print(n1 == n2)
print(n1 != n2)
print(n1 > n2)
print(n1 < n2)
print(n1 <= n2)
print(n1 >= n2)


#-------------------

firstName = " Ahmmed"
lastName = " Imtiaz"
initialization = "My full name is :"

print("My full Name is : ", firstName + lastName)
print(initialization, firstName, lastName)
print(initialization, firstName + lastName)
