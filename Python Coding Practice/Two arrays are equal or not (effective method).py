from collections import Counter

class Solution:
    # Function to check if two arrays are equal or not.
    def check(self, A, B, N):
        counter_A = Counter(A)
        counter_B = Counter(B)
        is_equal = counter_A - counter_B

        if all(val == 0 for val in is_equal.values()):
            return True
        else:
            return False


# Driver Code
if __name__ == '__main__':
    t = int(input())
    for tc in range(t):
        N = int(input())
        A = [int(x) for x in input().replace('  ', ' ').strip().split(' ')]
        B = [int(x) for x in input().replace('  ', ' ').strip().split(' ')]
        ob = Solution()
        if ob.check(A, B, N):
            print(1)
        else:
            print(0)
