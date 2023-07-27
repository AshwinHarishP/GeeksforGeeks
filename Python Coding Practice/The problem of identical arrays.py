#User function Template for python3
from collections import Counter

def check (arr,  brr, n) : 
    
    count_arr = Counter(arr)
    count_brr = Counter(brr)

    
    result = count_arr - count_brr
    if len(result) == 0:
        return 1
    
    else:
        for value in result.values():
            if value != 0:
                return 0
            return 1
     




#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    brr = list(map(int,input().strip().split()))
    
    print(check(arr, brr, n))




# } Driver Code Ends
