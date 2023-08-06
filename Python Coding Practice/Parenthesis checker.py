#User function Template for python3

class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
    
        # Creating stack
        stack = []
        
        # Creating parenthesis dictionary
        p_dict = {
            "{" : "}",
            "[" : "]",
            "(" : ")"
        }
    
        # Iterating through x
        for element in x:
        
            # Case 1: If element is open bracket
            if element in p_dict:
                stack.append(element)
            
            else:
                
                # Case 2: If element is closed bracket and stack is empty
                if len(stack) == 0:
                    return 0
                    
                # Case 3: If element matches stack[-1] element
                elif p_dict[stack[-1]] == element:
                    stack.pop()
                    
                # Case 4: None of the above matches
                else:
                    return 0
                
        return len(stack) == 0
        
        # T: O(n)   S: O(m + n)  
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        #n = int(input())
        #n,k = map(int,imput().strip().split())
        #a = list(map(int,input().strip().split()))
        s = str(input())
        obj = Solution()
        if obj.ispar(s):
            print("balanced")
        else:
            print("not balanced")
# } Driver Code Ends
