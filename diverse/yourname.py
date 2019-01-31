# YourName.py
name = input("What is your name?\n")
print("Hi, ", name)
my_age = input("How old are you?\n")
city = input("Where are you born?\n")
print(name + " is " + my_age + ' years old, and are born in ' + city)

age_brother = input("How old are your brother?\n")

if int(age_brother) > int(my_age):
    print("Hi little brother!")
else:
    print("Hi big brother!")
