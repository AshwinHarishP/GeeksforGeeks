def strstr(s, x):
    n = len(s)
    m = len(x)

    if m > n:
        return -1

    for i in range(n - m + 1):
        j = 0
        while j < m and s[i + j] == x[j]:
            j += 1

        if j == m:
            return i

    return -1

            


#{ 
 # Driver Code Starts
#Contributed by : Nagendra Jha

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        s,p =input().strip().split()
        print(strstr(s,p))


# } Driver Code Ends
