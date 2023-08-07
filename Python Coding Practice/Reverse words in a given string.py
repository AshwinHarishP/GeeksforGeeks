# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        S = S.split(".")
        new_str = ""
        
        for i in range(len(S)-1, -1, -1):
            new_str += S[i] +"."
        return "".join(new_str).strip(".")


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends
