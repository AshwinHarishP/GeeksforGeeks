#User function Template for python3

# arr is the array
# n is the number of element in array
def SumArray(arr,n):
    int_arr = []
    for element in arr:
        element = int(element)
        int_arr.append(element)
        
    result_list = []
    
    for i in range(n):
        result = sum(int_arr[:i] + int_arr[i+1:])
        result_list.append(result)
        
    arr[:] = result_list
        
    return arr

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():
    t = int(input())
    
    while(t >= 1):
        n = int(input())
        arr = input().split();
        SumArray(arr,n)
        print(*arr)
        t -= 1
        
if __name__ == '__main__':
    main()
# } Driver Code Ends
