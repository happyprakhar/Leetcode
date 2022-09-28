#-------------------Method1-------------------------------------
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        max_ = 0
        nums += nums
        for i in range(len(nums)):
            while stack and nums[i] > stack[-1][0]:
                x = stack.pop()[1]
                if x < len(nums) // 2:
                    nums[x] = nums[i]
            stack.append([nums[i], i])
            if stack:
                for i in stack:
                    nums[i[1]] = -1
        return nums[:len(nums) // 2]
        # print(res)

#--------------------------Method2---------------------------------------------------------
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            stack.append(nums[i])

        # print(stack)
        res = [-1] * len(nums)
        for curr in range(len(nums) - 1, -1, -1):
            while stack and nums[curr] >= stack[-1]:
                stack.pop()

            if stack:
                # print(stack)
                res[curr] = stack[-1]
            stack.append(nums[curr])
        return res


