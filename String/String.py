print("hello") # String

# multiline string
a = """ this is a 
multiline string in python"""
print(a)

# looping in a String
for x in "banana":
 print(x)

 # length in string

a = "hello world"
print(len(a))

# check String

txt = "The best things in life are free"
#check if present
print("free" in txt)
b = "thingss" in txt
c = "things" in txt

print(b)
print(c)

#check if not
d = "they" not in txt
e = "The" not in txt
print (d)
print(e)


# print only if "expensive" is NOT present:
txt2 = "The best things in life are free!"
if "expensive" not in txt2 :
 print("this is not so expencive")

