#User function Template for python3

class Solution:
    def MaxNumber(self, arr, n):

        return "".join(map(str,sorted(arr,reverse = True)))
    




#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.MaxNumber(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends
