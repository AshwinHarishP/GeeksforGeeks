#User function Template for python3

class Solution:
    def PartyType(self, a, n):
        set_a = list(set(a))
        
        if len(set_a) == len(a):
            return "GIRLS"
        return "BOYS"


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.PartyType(a, n))

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends
