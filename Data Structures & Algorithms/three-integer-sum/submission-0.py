class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

                #my intuition is basically have 2 pointers left and right and move the left and right based on the sum you have
        #so if the current sum is greater than target move the right so its less and if it is less move the left so that it is larger


#then we need another for loop that is for choosing the first number

        res =[]
        nums.sort()
        for i, a  in enumerate(nums):
            #dont want to resuse the same value that we have used before so if element now is equsls to the element before it then skip
            if i > 0 and nums[i] == nums[i-1]:
                continue


            l, r = i + 1, len(nums) -1
            while l < r:
                currSum = a + nums[l] + nums[r]
        
                if currSum == 0:
                    res.append([a, nums[l], nums[r]])
                    l +=1
                    while nums[l] == nums[l - 1] and l < r:
                        l +=1
                elif currSum > 0:
                    r -=1
                else:
                    l +=1

        return res

                
        