#User function Template for python3

class Solution:
    def sortIt(self, arr, n):
        odd_array = []
        even_array = []
        
        for i in range(n):
            if arr[i] %2 != 0:
                odd_array.append(arr[i])
            else:
                even_array.append(arr[i])
    
        odd_array = sorted(odd_array, reverse=True)
        even_array = sorted(even_array) 
        
        arr[:] = odd_array + even_array
        
        return(arr)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sortIt(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends
