def diagonalDifference(arr):
    # Write your code here
    dia1 = 0
    dia2 = 0
    for ar in arr:
        m = arr.index(ar)
        dia1 += ar[m]
        dia2 += ar[-m-1]
    return abs(dia1-dia2)

# n = int(input().strip())

# arr = []

# for _ in range(n):
#     arr.append(list(map(int, input().rstrip().split())))
arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

result = diagonalDifference(arr)

print (result)
