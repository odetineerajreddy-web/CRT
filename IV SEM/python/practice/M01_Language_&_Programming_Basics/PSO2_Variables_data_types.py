'''
1.Data Types :
 1. Integer
 2. Float
 3. String
 4. Boolean
 5. complex

2.Collections of:
    1. List
    2. Tuple
    3. Set
    4. Dictionary
'''
x = 12
y=12.45
z=4+5j
print(x , type(x))
print(y , type(y))
print(z , type(z))


f1=3e2 #e=10^
f2=4E3 #E=10^
print(f1 , type(f1))# scientific notation
print(f2 , type(f2))

c1=4+5j
c2=complex(2,-3)
print(c1 + c2 )
print(c1-c2)
print(c1 * c2)
print(c1/c2)

print(c1.real)# real part
print(c1.imag)# imaginary part

s="python"
print(s[2])
print(s[::])
print(s[::2])
print(s[::-1])