'''
1)find the largest number using (max)
2) check palidrome using reversed()& join())

4)remove duplicates

#1)find the largest number using (max)
arr=[10,23,54,85,20,10]
print(max(arr))

#2) check palidrome using reversed()& join())
word= 'madam'
if word=="".join(reversed(word)):
    print("palidrome")
else:
    print("Not a Palidrome")

#3
arr=[10,23,54,89,10,25]
res=list(filter(lambda x:x%2==0,arr))
print(res)

#4) remove duplicates using set()--> unique collection of data
numbers = [1, 2, 3, 2, 4, 1, 5]

unique_numbers = set(numbers)

print(unique_numbers)
'''



