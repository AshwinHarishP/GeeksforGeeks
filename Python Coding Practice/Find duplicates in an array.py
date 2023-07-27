from collections import Counter

class Solution:
    def duplicates(self, arr, n): 
    	
        arr_count = Counter(arr)
        
        duplicate_element = []
        for keys,values in arr_count.items():
            if values > 1:
                duplicate_element.append(keys)
        
        if len(duplicate_element) == 0:
            return [-1]
        
        return sorted(duplicate_element)

#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends
