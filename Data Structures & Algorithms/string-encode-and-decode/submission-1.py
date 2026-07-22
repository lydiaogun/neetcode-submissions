class Solution:
    #cant we like simply use a for loop for each element in the array then add it into a string
    #we need something to tell us hey the next string starts here - thats the part i missed
    #so add the length of the string , then a delimeter, then the string
    def encode(self, strs: List[str]) -> str:
        encoded_string =""
        for i in strs:
            encoded_string += str(len(i)) + "#" + i
        return encoded_string

    #decoded is a bit harder  
    #we need a result variable and also an index counter  
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        #continue iterating until we get to the end of the string
        while i < len(s):
            #we need another while loop so we can iterate in each subsection of the string and also so we can jump in and jump out of the string
            j = i
            #while the letter we are on is not the delimeter continue iterating - we are trying to get to the end of the list
            while s[j] != "#":
                j+=1
            #how many following characters we have to read after j in order to get every character of string

            length = int(s[i:j]) #okay this is basically used to find out what the length is - the purpose of encoding the length of the string so its like the number before the #
            res.append(s[j + 1 : j + 1 + length ] ) # j points to the # so j + 2 points to the letter past it
            i = j + 1 + length
        return res
