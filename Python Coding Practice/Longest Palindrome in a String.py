#User function Template for python3

class Solution:
    def longestPalin(self, S):
        res = ""
        resLen = 0
        
        for i in range(len(S)):
            
            # Odd 
            l,r = i,i
            while l >= 0 and r < len(S) and S[l] == S[r]:
                if (r - l + 1) > resLen:
                    res = S[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            
            # Even
            l, r = i, i+1
            while l >= 0 and r < len(S) and S[l] == S[r]:
                if (r - l + 1) > resLen:
                    res = S[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalin(S)

        print(ans)
# } Driver Code Ends
