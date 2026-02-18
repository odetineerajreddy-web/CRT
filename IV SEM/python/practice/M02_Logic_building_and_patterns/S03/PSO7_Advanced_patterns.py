'''#1.Pascal Triangle 
n=int(input())
for i in range(n):
    num=1
    for j in range(i+1):
        print(num,end=" ")
        num=num*(i-j)//(j+1)
    print()
'''
#2.Butterfly Pattern
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    print("*" * i, end=" " * (2 * (n - i) + 1))
    print("*" * i)
for i in range(n, 0, -1):
    print("*" * i, end=" " * (2 * (n - i) + 1))
    print("*" * i)
