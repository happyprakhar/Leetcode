# next greater elment in an array
def fun(nums):
    # putting -1 on stack on stack to avoid empty problem
    # intializing res with -1
    # stack[-1] signifies top of the stack
    stack=[-1]
    res=[-1]*len(nums)
    for curr in range(len(nums)-1,-1,-1):
        if nums[curr]<stack[-1]:
            res[curr] = stack[-1]
        stack.append(nums[curr])
    return res

a=[1,3,4,6,7,2]
b=[5,4,3,2,1]
print(fun(a))
print(fun(b))

Output:
[3, 4, 6, 7, -1, -1]
[-1, -1, -1, -1, -1]
