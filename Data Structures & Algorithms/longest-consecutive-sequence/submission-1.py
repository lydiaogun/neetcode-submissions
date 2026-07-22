class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            #check if its at the beginning of the list
            if (num - 1) not in numSet:
                length = 1
            #now keep on checking to see if the chain is int the list
                while (num + length) in numSet:
                    length +=1
                longest = max(length, longest)  
        return longest
