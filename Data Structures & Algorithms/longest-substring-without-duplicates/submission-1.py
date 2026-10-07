class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #two ways i am thinking of doing it append elements into the array and then pop when they are not and return the length of the window
        #OR use an integer to calulcate the length the whole time
        left = 0
        res= 0 
        charSet = set()
        for right in range(len(s)):
            #add right to the window state
   
            while s[right] in charSet:
                #remove arr[left] from the window state
                charSet.remove(s[left])
                left +=1
            charSet.add(s[right])
            res = max(res, right - left + 1)

        #record answer, window is valid there
        return res

        