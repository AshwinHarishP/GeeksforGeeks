#User function Template for python3

class Solution:
    def firstIndex(self, arr, n):
        for i in range(n):
            if arr[i] == 1:
                return i
        return -1




#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstIndex(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends
