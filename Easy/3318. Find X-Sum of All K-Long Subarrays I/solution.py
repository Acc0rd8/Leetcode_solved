class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        subarrays = []
        i = 0
        
        while i + k - 1 < len(nums):
            subarray = nums[i:i + k]
            subarrays.append(sorted(subarray))
            i += 1
        
        x_sum_list = []
        for array in subarrays:
            total = 0
            for _ in range(x):
                max_count = 0
                max_num = 0
                for num in array:
                    if array.count(num) > max_count:
                        max_count = array.count(num)
                        max_num = num
                    if array.count(num) == max_count and num > max_num:
                        max_count = array.count(num)
                        max_num = num
                total += max_count * max_num
                array = list(filter(lambda x: x != max_num, array))
            x_sum_list.append(total)
        return x_sum_list
    
print(Solution().findXSum(nums = [3,8,7,8,7,5], k = 2, x = 2))