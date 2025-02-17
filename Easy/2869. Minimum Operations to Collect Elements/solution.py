class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        collection = []
        needed_collection = [i for i in range(1, k + 1)]
        result = 0
        
        for num in nums[::-1]:
            result += 1
            if num not in collection:
                collection.append(num)
                collection.sort()
            if collection[:k] == needed_collection:
                return result