#Adding characters -MCQ
first,second=input().split()
print(ord(first)+ord(second)) # ord gives Unicode(ASCII) value of both the characters and add them

#Area of a circle
radius=float(input())
area=3.142*radius*radius
print(area)

#WAP that takes the two different strings as input and prints them in a single line separated by spaces.
a,b=input().split()
print(a,b)

# Write a program that takes an input string - the name of a person and prints Hello and name of the person with a space between them.
name=input("Enter your name: ")
print("Hello ",name)