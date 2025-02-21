class Solution:
    def findTheArrayConcVal(self, nums: list[int]) -> int:
        value = 0
        
        while len(nums) > 0:
            if len(nums) == 1:
                value += nums[0]
                nums.pop()
            else:
                value += int(str(nums[0]) + str(nums[-1]))
                nums.pop(0)
                nums.pop()
        
        return value

print(Solution().findTheArrayConcVal([7, 52, 2, 4]))