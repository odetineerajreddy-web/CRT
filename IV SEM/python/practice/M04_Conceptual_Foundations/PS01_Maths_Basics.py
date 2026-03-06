##1write python code to print all the airthmetic operations(+,-,*,/,//,%,**)?
print(abs(-54))
print(round(5.478))
print(min(5,10,15))
print(max(5,10,15))
print(sum([5,10,15]))
print(pow(5,3))

#1find the GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a