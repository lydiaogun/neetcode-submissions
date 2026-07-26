class Solution:
    def isValid(self, s: str) -> bool:

        #couple of rules
            #we can start the stack with as many opening brackets
            #but we cannot start a stack with the closing one because what is it gonna match to

        #okay we need our stack and hashmap
        stack = []
        closeToopen =  {"]": "[", "}": "{", ")": "("}

        #now iterate through the list 
        for i in s:
            #check if its a closing bracket
            if i in closeToopen:
                #check if the stack is not empty and check if the value at the top of the stack has a matching open parenthesis
                if stack and stack[-1] == closeToopen[i]:
                    stack.pop()
                else: #if they dont match each other and the stack is empty
                    return False #the empty line because there is nothing for the closing bracket to match to
            else:
                stack.append(i)
        #return true if the stack is empty 
        return True if not stack else False\
