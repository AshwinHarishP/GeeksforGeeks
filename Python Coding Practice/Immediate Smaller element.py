Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #User function Template for python3
... class Solution:
... 
... 	def immediateSmaller(self,arr,n):
... 	    List = []
... 		for i in range(len(arr)-1):
... 		    
... 		    if arr[i] > arr[i+1]:
... 		        List.append(arr[i+1])
... 		    else:
... 		        List.append(-1)
... 		        
... 	    List.append(-1)
... 	    arr[:] = List
... 	    return arr
... 
... 
... #{ 
...  # Driver Code Starts
... if __name__ == '__main__':
...     tcs=int(input())
... 
...     for _ in range(tcs):
...         n=int(input())
...         arr=[int(x) for x in input().split()]
...         ob = Solution()
...         ob.immediateSmaller(arr,n)
...         for x in arr:
...             print(x, end=" ")
...         print()
