class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) -1 

        while l < r :

            while (s[l]).isalnum() == False and l < r:
                l +=1

            while  l < r and (s[r]).isalnum() == False:
                r-=1

            #check if the left and right are equals to each other and also it is alphanumeric
            if s[l].lower() == s[r].lower():
                l +=1
                r-=1
            else:
                return False
        return True


