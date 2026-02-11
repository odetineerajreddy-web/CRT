#Number sereies:Sequential order of numbers in a particuler pattern
'''#1. Print first N natural numbers
n=int(input("Enter the number:"))
for i in range(1,n+1):
    print(i)
    '''
'''#print n even numbers
n=int(input("Enter the number:"))
for i in range(2,n*2+1,2):
    print(i)
    '''
'''#print n odd numbers
n=int(input("Enter the numbers:"))
for i in range(1,n*2,2):
    print(i)
'''    '''
#fibonacci series
n=int(input("Enter the number:"))
a,b=0,1
for i in range(n):
    print(a)
    a,b=b,a+b
    '''

'''
#multiplication table of a number
n=int(input("Enter the number:"))
for i in range(1,21):
    print(n,"*",i,"=",n*i)
 '''  
'''
 
#print squares of first n natural numbers
n=int(input("Enter the number:"))
for i in range(1,n+1):
    print(i**2)
   '''

'''
#Print cubes of first n natural numbers

n=int(input("Enter the number:"))
for i in range(1,n+1):
    print(i**3)
    '''
'''
#alternative series
n=int(input("Enter the number:"))
for i in range(1,n+1):
    if i%2==0:
        print(-i)
    else:
        print(i)
'''
