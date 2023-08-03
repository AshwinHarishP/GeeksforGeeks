#User function Template for python3

class Solution:
    def allPairs(self, A, B, N, M, X):
        j = M - 1
        A.sort()
        B.sort()
        pair_list = []
        i = 0
        j = M - 1
        
        while i < N and j >= 0:
            if A[i] + B[j] == X:
                pair_list.append((A[i], B[j]))
                i += 1
                j -= 1
            elif A[i] + B[j] > X:
                j -= 1
            else:
                i += 1
                
        return pair_list
                
                
            
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        N, M, X = sz[0], sz[1], sz[2]
        A = [int(x) for x in input().strip().split()]
        B = [int(x) for x in input().strip().split()]
        ob=Solution()
        answer = ob.allPairs(A, B, N, M, X)
        sz = len(answer)
        
        if sz==0 :
        	print(-1) 
        
        else: 
            
        	for i in range(sz):
        		if i==sz-1:
        		    print(*answer[i])
        		else:
        		    print(*answer[i], end=', ')
        

        T -= 1


if __name__ == "__main__":
    main()




# } Driver Code Ends
