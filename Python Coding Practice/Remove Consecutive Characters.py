#User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, S):
        
        stack = []
        for i in S:
            if not stack or i not in stack[-1]:
                stack.append(i)
        
        return "".join(stack)
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        s = input()
        ob = Solution()
        print(ob.removeConsecutiveCharacter(s))

# } Driver Code Ends
