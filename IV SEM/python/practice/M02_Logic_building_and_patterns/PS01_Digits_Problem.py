'''#1.  Count the numbers of digits in a number
n=int(input())
temp=n
count=0
while n>0:
    count+=1
    n//=10
print(count)
print(len(str(temp)))
'''

'''#2.  Sum of digits in a number
n=int(input())
sum=0
while n>0:
    sum+=(n%10)
    n//=10
print(sum)
'''
#Find the digtital root of a number
n=int(input())
while n>0:
    n=sum(list(map(int,str(n))))
print(n)
