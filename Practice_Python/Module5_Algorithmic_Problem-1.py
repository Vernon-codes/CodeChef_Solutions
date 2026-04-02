#Learning SQL Problem
r,c,e=map(int,input().split())
r+=e
print(r*c)

#Parking Charges Problem
x,y,h=map(int,input().split())
total_charges=0
if h<=1:
    total_charges=x*h
else:
    total_charges=x+y*(h-1)
print(total_charges)  