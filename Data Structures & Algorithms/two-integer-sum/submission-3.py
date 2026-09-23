from collections import defaultdict, Counter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #for each item in the nums, subtract it from the target
        #store that difference in the hashmap + the index
        #if the element is already in the hashmap
        #return the indices

        hmap = {}
        diff = 0
        for i, num in enumerate(nums):
            diff = target  - num

            if num in hmap:
                return [hmap[num], i]
            else:
                hmap[diff] = i

        