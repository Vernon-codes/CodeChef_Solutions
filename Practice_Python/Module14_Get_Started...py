#increase the integer 
test_cases=int(input())
for i in range(test_cases):
    n=int(input())
    print(n+1)

#even or odd
def isEven(n):
    return n % 2 == 0

test_cases = int(input())
for i in range(test_cases):
    num = int(input())
    if isEven(num):
        print("Even")
    else:
        print("Odd")