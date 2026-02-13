'''
li=[1,2,3,4,5]
res=[]
for i in li:
    if i%2 == 0:
        res.append(i)
print(res)
'''
'''
li=[1,2,3,4,5]
print([i for i in li if i%2==0])
'''
'''
#joining Strings


li1=['a','b','c']
res=" "
for ch in li1:
    res=res+ch+" "
print(res)
print(" ".join(li1))
'''
'''
#1.Pyramid
n=int(input())
for i in range(1,n+1):
    for sp in range(n-i):
        print(" ",end=" ")
    for j in range(i*2-1):
        print("*",end=" ")
    print()
'''
         #or

'''n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
'''
'''
#inverted Pyramid
n=int(input())
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)
'''

'''#diamond
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i)
print() 
'''
#5 palidrome Pattern

