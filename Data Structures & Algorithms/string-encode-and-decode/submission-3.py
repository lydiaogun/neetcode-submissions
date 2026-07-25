class Solution:
    #cant we like simply use a for loop for each element in the array then add it into a string
    #we need something to tell us hey the next string starts here - thats the part i missed
    #so add the length of the string , then a delimeter, then the string
    def encode(self, strs: List[str]) -> str:
        encoded_string =""
        for i in strs:
            encoded_string += str(len(i))
            encoded_string += "#"
            encoded_string += i
        return encoded_string
        
    #decoded is a bit harder  
    #we need a result variable and also an index counter  
    def decode(self, s: str) -> List[str]:
        #first things first we want to go through the string and stop when we get to the end and also we want the variable that we are going to store the decoded string

        res= []
        i = 0

        #now while the curent index is not at the end of the string

        while i < len(s):
            #we are going to have another index for taking count of the delimeter and stuff
            j = i
            while s[j] != "#":
                j += 1
            #now we have j at the delimeter so we want the length of the string to be able to understand how far we want to skip ahead to the next string
            length = int(s[i:j])
            res.append(s[j+1: j + 1 + length]) # j + 1 is at the delimeter so we need the string there --------- all the way to the end of the length
            i  = j + 1 + length
        return res