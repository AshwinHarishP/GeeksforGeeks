#User function Template for python3
from collections import Counter
class Solution:
    def getOddOccurrence(self, arr, n):
        count_arr = Counter(arr)
        
        for keys, values in count_arr.items():
            if values % 2 != 0:
                return keys


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getOddOccurrence(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
