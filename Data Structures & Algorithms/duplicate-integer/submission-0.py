class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = 0
        newList = []
        for i in nums:
            if i in newList:
                return True
            newList.append(i)
        return False

        