'''
#Square Star Problem
n = int(input())
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
'''
'''
#2 Right Angle Triangle 
n=int(input())
for i in range (n):
    for j in range(i+1):
        print("*",end=" ")
    print()
'''
'''
#3. Inverted Triangle 
n=int(input())
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
'''
'''
#4.Number Triangle
n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print(j+1,end=" ")
    print()
'''
'''
#5.Repeated Number Pattern
n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()
'''
'''
#6.Alphabet Triangle
n=int(input())
for i in range(1,n+1):
    ch=65
    for j in range(i):
        print(chr(ch+j),end=" ")
    print()
'''
'''
#7.Floyd Triangle

n = int(input())
num = 1
for i in range(1, n+1):       # rows
    for j in range(1, i+1):   # columns
        print(num, end=" ")
        num += 1
    print()
'''
#8 Hollow Square
n=int(input())
for i in range(n):
    if i==0 or i==n-1 or j==0 or:
print("*",end=" ")



