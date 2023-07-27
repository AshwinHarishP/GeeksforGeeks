#User function Template for python3

class Solution:
    def isPrime(self, N):
        if N <= 1:
            return 0

        if N <= 3:
            return 1

        if N % 2 == 0 or N % 3 == 0:
            return 0

        i = 5
        while i * i <= N:
            if N % i == 0 or N % (i + 2) == 0:
                return 0
            i += 6

        return 1

                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.isPrime(N))
# } Driver Code Ends
