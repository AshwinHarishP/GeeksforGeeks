#User function Template for python3

def binarySearch(arr,low,high):
    while low <= high:
        mid = (low + high)//2
        
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        print(binarySearch(arr,0,n-1))
# } Driver Code Ends
