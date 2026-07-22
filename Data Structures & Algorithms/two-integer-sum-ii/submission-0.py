class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

      l,r = 0, len(numbers) -1
      # we need left and right pointers to keep tracks of the beginning of the list and end of the list

      while l < r: # does not really matter because there is a solution so the pointers will never not cross
        curSum = numbers[l] + numbers[r]
        if curSum > target: # if the current sum is to big move the right pointer left so that we can get to a less big number
            r-=1
        elif curSum < target: # when its to small move it left so that we can get to a bigger number
            l +=1
        else :
            return [l+1, r+1]