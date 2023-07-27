#User function Template for python3


class Solution:
    
    def checkIsAP(self, arr, n):
        arr = sorted(arr)
        new_arr = [arr[0]]
        temp = arr[0]
        diff = arr[1] - arr[0]
        
        for i in range(1,n):
            temp += diff
            
            new_arr.append(temp)
            
        
        if new_arr == arr:
            return True
        return False
        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    # l=list(map(int,input().split()))
    # n=l[0]
    # x=l[1]
    # y=l[2]
    a = list(map(int,input().split()))
    ob = Solution()
    ans=ob.checkIsAP(a,n)
    if(ans==True):
        print("YES")
    else:
        print("NO")
# } Driver Code Ends
