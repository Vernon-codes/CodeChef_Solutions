# What is the correct way to check if a number is between 10 (non-inclusive) and 20 (inclusive)?
number = 15
if number>=10 and number<=20:
    pass

#Number divisible by 3 and 5
num=int(input())

if num%3==0 and num%5==0:
    print("Divisible by both 3 and 5")
elif num%3==0:
    print("Divisible by 3")
elif num%5==0:
    print("Divisible by 5")
else:   
    print("Not divisible by 3 or 5")


# Write a program that takes three space separated numbers as input and prints:
# "Increasing" if the numbers are in strictly increasing order,
# "Decreasing" if they are in strictly decreasing order,
# and "Neither" otherwise.

a,b,c=map(int,input().split())
if a<b<c:
    print("Increasing")
elif a>b>c:
    print("Decreasing")  
else:
    print("Neither")

# Write a program that takes two space separated inputs - the age (an integer) and the name of country(a string) and does the following:
# Prints "Eligible" if the age is greater than or equal to 18 and country is India
# Prints "Not Eligible", otherwise.

age,country=input().split()
age=int(age) #type casting 

if age>=18 and country=="India":
    print("Eligible") 
else:   
    print("Not Eligible")