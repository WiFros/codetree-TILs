import array
n = int(input())
arr = [0 for _ in range(201)]

for i in range(n):
    x1, x2 = tuple(map(int, input().split()))
    x1 += 100
    x2 += 100
    arr[x1-1 : x2] = [x + 1 for x in arr[x1-1 : x2]]

print(max(arr))