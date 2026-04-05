#Chefs First contest Problem
# N, A, B = map(int, input().split())
# rated_users = N - A
# high_rating_users = N - A - B
# print(rated_users, high_rating_users)

#determine the number of black cells in chess board
a=6*6  # 36 balck cells in 6*6 chess board and 36 white cells in 6*6 chess
print(a//2)

# Black cells in a chessboard
n=int(input())
if n%2==0:
    print(n*n//2)
else:
    print("Invalid Input")

#AB difference
A,B=map(int,input().split())
c=A*B
d=A+B
absolute_difference=abs(c-d)
print(absolute_difference)  

