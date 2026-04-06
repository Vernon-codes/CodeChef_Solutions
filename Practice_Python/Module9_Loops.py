# #Program that converts ASCII codes to characters using a for loop
for c in range(ord('A'), ord('E') + 1):
    print(chr(c), end=" ")  #chr converts the ASCII code back to a character
print()  # for a new line

# #Sum of Multiple of 3
integer = int(input("Enter an integer: "))
total=0
for i in range(1,integer+1):
    print(3*i)
    total+=3*i
print("The sum of the multiples of 3 is:", total)

# # First occurrence
array=[2, 4, 8, 12, 8]
number=int(input("Enter a number to find: "))
count=0
for i in array:
    if i==number:
        count+=1
print(count)

#Write a program that uses a for-each loop to print the square of each element in list of 
# N space separated integers, but skips elements greater than 10
num=list(map(int,input().split()))
for i in num:
    if i>10:
        continue
    print(i**2)
