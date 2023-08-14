# Function should return an integer value
def convertFive(n):
    n = list(str(n))
    for i in range(len(n)):
        if n[i] == "0":
            n[i] = "5"
    return (int("".join(n)))


#{ 
 # Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        print (convertFive(int(input().strip())))
# } Driver Code Ends
