#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        
        if not arr:
            return -1
        arr.sort()
        
        first_ele = arr[0]
        last_ele = arr[n-1]
        str_ele = ""
        
        for i in range(len(first_ele)):
            if i < len(last_ele) and first_ele[i] == last_ele[i]:
                str_ele += first_ele[i]
            else:
                break
            
        if len(str_ele) > 0:
            return str_ele
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends
