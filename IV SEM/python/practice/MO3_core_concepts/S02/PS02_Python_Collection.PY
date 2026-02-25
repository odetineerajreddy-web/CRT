'''
#268 Missing Number
nums=[3,0,1]
n=len(nums)
#res=set(range(n+1))
#print(res-set(nums))
s=(n*(n+1))//2
print(s-sum(nums))
'''
