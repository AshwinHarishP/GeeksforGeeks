#User function Template for python3



class Solution:
    def arranged(self,a,n):
        
        possitive_list = []
        negative_list = []
        
        for i in a:
            if i >= 0:
                possitive_list.append(i)
            else:
                negative_list.append(i)
                
        new_arr = []
        
        for j in range(len(possitive_list)):
            new_arr.append(possitive_list[j])
            new_arr.append(negative_list[j])
            
        a[:] = new_arr
        return new_arr
            
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=Solution().arranged(a,n)
    print(*ans)

# } Driver Code Ends
