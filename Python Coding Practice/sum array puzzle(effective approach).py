#User function Template for python3

# arr is the array
# n is the number of element in array
def SumArray(arr,n):
    
    int_arr = []
    for elements in arr:
        elements = int(elements)
        int_arr.append(elements)
        
    Sum = sum(int_arr)
    result_list = []
    for i in int_arr:
        result_list.append(Sum - i)
    
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
