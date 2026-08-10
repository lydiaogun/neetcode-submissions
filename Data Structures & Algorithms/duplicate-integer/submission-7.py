class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #if any value appears more than once in the array
        #so use a hash set
        hashset = set()

        #iterate through an array and check if an item is an array
        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.add(i)
        return False