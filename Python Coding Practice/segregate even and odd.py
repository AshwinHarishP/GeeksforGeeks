#User function Template for python3
class Solution:

	def segregateEvenOdd(self,arr, n):
		even_arr = []
		odd_arr = []
		
		i = 0
		while i <= n-1:
		    if arr[i] % 2 == 0:
		        even_arr.append(arr[i])
		    i += 1
        
        even_arr = sorted(even_arr)
        
        j = 0
        while j <= n-1:
            if arr[j] % 2 != 0:
                odd_arr.append(arr[j])
            j += 1
        odd_arr = sorted(odd_arr)
        

        arr[:] = even_arr + odd_arr
        
        
        

        
#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.segregateEvenOdd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
