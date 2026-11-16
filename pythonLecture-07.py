from typing import Concatenate
# Python Lecture - 07
# practicing String operation

data = "python learning & data analysis"
convertion = data.capitalize()
convertion2 = data.swapcase()
print(convertion)
print(convertion2)
print(data.upper())
print(data.swapcase())
print(len(data))


# ---------------Lecture Started------------------------
s1 = "Hello"
s2 = "Pagol"

print(type(s1 + s2))
print(s1 + s2)
print(s1, s2)
print(s1, "", s2)
print(f"{s1}  {s2}")


# ---------------------replace method & Lenth method --------------------------
text = "I love python"
print(text.replace("python", "java"))
print(text.replace("I love python", "love"))
print(len(text))

newText = ""
for i in range(2,7):
    # print(Concatenate(text[i]).join("love"))
    # print(text[i].join())
    # print(join(text[i]))
    newText = newText + text[i]
print(newText)
    # print(join(text[i]))
print(text[2:7])


# ------------ strip method---------------------
s3 = "Hi\n Hello Chagol                pagol \tGoru"
print(s3)
print(s3.strip())

s4 = " \n Hello String Test "
print(s4.strip())
print(s4.lstrip())
print(s4.rstrip())


# ----------------count method ------------------------------
# checking how many character of 'a'
text1 = "bananananana"
print(text1.count("a"))

# multiline String
text2 = '''I hate python, love python, do python, practice python,
I hate python, love python, do python, practice python'''
print(text2.count("python"))
text3 = text2.count("python")
if (text3>1):
  print("Found")
else:
  print("Not Found")

# -------------------------Upper/lower Methods -------------------------------
msg = "He is King Khan"
print(msg.upper())
print(msg.lower())
print(msg.swapcase())


# ------------------------startwith/endswith method ---------------------------
filename = "jasperReport.txt"
print(filename.endswith(".txt"))
print(filename.endswith(".pdf"))
print(filename.startswith("my"))
print(filename.startswith("jas"))