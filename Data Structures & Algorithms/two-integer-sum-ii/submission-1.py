class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #my intuition is basically have 2 pointers left and right and move the left and right based on the sum you have
        #so if the current sum is greater than target move the right so its less and if it is less move the left so that it is larger

        l, r = 0, len(numbers) -1
        while l < r:
            currSum = numbers[l] + numbers [r]

            if currSum == target:
                return [l +1, r+ 1]
            if currSum > target:
                r -=1
            else:
                l +=1
            

        