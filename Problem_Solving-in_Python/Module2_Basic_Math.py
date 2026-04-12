#Burgers
t=int(input())
for i in range(t):
    A,B=map(int,input().split())
    print(min(A,B))

#Air Hockey
T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    print(7 - max(A, B))

