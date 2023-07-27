Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #User function Template for python3
... 
... 
... class Solution:
...     def firstElementKTime(self,  a, n, k):
...         Max = max(a) +1
...         c_arr = [0] * Max
...         
...         for i in range(n):
...             c_arr[a[i]] += 1
...                 
...             if c_arr[a[i]] == k:
...                 return a[i]
...         return -1
... 
... 
... 
... #{ 
...  # Driver Code Starts
... #Initial Template for Python 3
... 
... def main():
... 
...     T = int(input())
... 
...     while(T > 0):
...         sz = [int(x) for x in input().strip().split()]
...         n, k = sz[0], sz[1]
...         a = [int(x) for x in input().strip().split()]
...         ob = Solution()
...         print(ob.firstElementKTime(a, n, k))
... 
...         T -= 1
... 
... 
... if __name__ == "__main__":
...     main()
... 
