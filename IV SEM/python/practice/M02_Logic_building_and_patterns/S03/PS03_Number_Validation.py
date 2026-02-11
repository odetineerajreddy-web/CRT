'''
1) write a python code for the factorial
n=int(input("enetr n "))
fact = 1
for i in range(1,n+1):
    fact*=i
print(fact)
'''
'''
#2 write a python code to check whether a number is armstrong or not
#ex: 153-->1,5,3-->(1*3)+(5*3)+(3*3)==153
code:

'''

#3 write a python code to check whether a number is prime or not 
#4 print the prime numbers with a range?
#5  Montonic of an array
'''
arr=list(map(int,input("Enter array el").split()))
inc=true
dec=true
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        inc=false
    if arr[i]<arr[i+1]:
        dec=false 
        if inc or dec         
'''
'''
#reverse integer

x=int(input("Enter a integer: "))
sign = 1
if x<0:
    sign=-1
    x=-x
rev =0
while x>0:
    digit = x%10
    rev = rev * 10 + digit
    x=x//10
rev = rev * sign

if rev < -2**31 or rev>2**31 -1:
    print(0)
else:
    print("Reversed Integer:",rev)
'''
'''
# given a  roman numeral ,convert it to integer

roman=input("Enter a Roman Numeral: ").upper()
values={
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
}
total =0
prev=0
for ch in reversed(roman):
    if values[ch]<prev:
        total-=values[ch]
    else:
        total+=

'''

