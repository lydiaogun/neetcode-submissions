class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hset = {}
        for i,v in enumerate(nums):
            complement= target - v

            if complement in hset:
                return  [hset[complement], i]
            else:
                hset[v] = i