#Apples and oranges
X=int(input("Amount Bob has: "))
A,B=map(int,input("Cost per/kg of Apples and Oranges: ").split())
orange_Bob_can_buy = (X - A) 
if X>=A and orange_Bob_can_buy>=B:
    print("YES")    
else:
    print("NO")

#speciality
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if x>y and x>z:
        print("Setter")
    elif y>x and y>z:
        print("Tester")
    else:        
        print("Editorialist")
    

  