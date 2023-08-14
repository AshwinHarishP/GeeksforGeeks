class Height:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

def findMax(arr, n):
    max_height = 0
    for i in range(n):
        height_in_inches = (arr[i].feet * 12) + arr[i].inches
        if height_in_inches > max_height:
            max_height = height_in_inches
    return max_height

t = int(input())
while t > 0:
    n = int(input())
    arr = []
    for i in range(n):
        tmp1, tmp2 = map(int, input().split())
        arr.append(Height(tmp1, tmp2))
    res = findMax(arr, n)
    print(res)
    t -= 1
