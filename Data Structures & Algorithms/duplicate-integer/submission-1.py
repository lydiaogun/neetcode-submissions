class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num2= {}
        resolution = []
        flag = False

        for i in nums:
            if i in num2:
                flag = True
            else:
                num2[i] = 1
        return flag
        