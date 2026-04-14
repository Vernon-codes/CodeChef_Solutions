#MOVIE-2X
x=int(input())
y=int(input())
if y%2==0:
    x=x-y
    z=y//2 #2x speed means half the time
else:
    print("Invalid Input")
print("Total Minutes Spent: ",x+z)

#ROWS AND CELLS
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    if a==c and b==d:
        print(1)
    else:
        print(2)

#TOO MANY FLOORS
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print(abs((x - 1)//10 - (y - 1)//10)) #find the floor no of each and then subract it with abs 

