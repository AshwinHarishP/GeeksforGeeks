#User function Template for python3

def game_with_number (arr,  n) : 
    new_arr = []
    elements = 0
    
    while elements <= n-2:
        new_arr.append(arr[elements] | arr[elements+1])
        elements += 1
    
    new_arr.append(arr[-1])
    return new_arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = game_with_number(arr, n);
    print(*res)




# } Driver Code Ends
