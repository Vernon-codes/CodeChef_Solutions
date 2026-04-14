#MOVIE-2X
x=int(input())
y=int(input())

if y%2==0:
    x=x-y
    z=y//2 #2x speed means half the time
else:
    print("Invalid Input")
print("Total Minutes Spent: ",x+z)