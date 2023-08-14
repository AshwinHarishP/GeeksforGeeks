#User function Template for python3

def multiply (arr, n) : 
    sub_length = n//2
    
    #Calculating sum for left
    left_sum = 0
    for left_elements in range(sub_length):
        left_sum += arr[left_elements]
        
    #Calculating sum for right
    right_sum = 0    
    for right_elements in range(sub_length,n):
        right_sum += arr[right_elements]
        
    #Returning as a product 
    return left_sum * right_sum



#{ 
 # Driver Code Starts
#Initial Template for Python 3

    

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = multiply(arr, n)
    print(ans)
# } Driver Code Ends
