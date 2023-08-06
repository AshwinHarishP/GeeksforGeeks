#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        count_ele = {}
        
        for elements in A:
            
            if elements in count_ele:
                count_ele[elements] = count_ele.get(elements, 0) + 1
            else:
                count_ele[elements] = 1
                
        Max = max(count_ele.values())
        
        if Max <= N / 2:
            return -1
        
        else:
            for key, values in count_ele.items():
                if values == Max:
                    return key
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
