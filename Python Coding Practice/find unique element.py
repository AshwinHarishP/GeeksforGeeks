from collections import Counter

class Solution:
    def findUnique(self, a, n, k): 
        a_count = Counter(a)
        for keys,values in a_count.items():
            if values % k != 0:
                return keys


#{ 
 # Driver Code Starts
import sys 

if __name__=='__main__':
    T = int(input())

    for _ in range(T):
        n,k=[int(x) for x in input().split()]
        a = [int(x) for x in input().split()]

        print(Solution().findUnique(a,n,k))
# } Driver Code Ends
