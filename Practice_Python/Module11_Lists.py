#elements size in lists
import sys
myNumbers = [10, 20, 30, 40, 50]
size_of_int = sys.getsizeof(myNumbers[2])
print(size_of_int)

#list elements are mutable
letters = ['A', 'B', 'C']
letters[2] = 'D'
print(letters[2])  

#size evaluation of list elements
import sys
values = [1, 2, 3, 4, 5]
size_in_bytes = sum(sys.getsizeof(item) for item in values)/sys.getsizeof(values[0])
print(size_in_bytes)

# Multiply the first and third elements of a list of integers by taking list as input
a=list(map(int,input().split()))
print(a[0]*a[2])

#shopping List
a=list(input().split())
to_check=input("Enter the item to check: ")
if to_check in a:
    print("YES")
else:
    print("NO")

# shopping List
a=list(input().split())
to_check=input("Enter the item to check: ")
for i in a:
    if i==to_check:
        print("YES")
        break
else:    
    print("NO")