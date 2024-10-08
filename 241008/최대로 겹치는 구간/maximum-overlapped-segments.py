n = int(input())
arr = [0 for _ in range(401)]

for i in range(n):
    x1, x2 = tuple(map(int, input().split()))
    x1 += 100 
    x2 += 100
    arr[x1] += 1 
    arr[x2 + 1] -= 1

max_value = 0
current_value = 0
for i in range(len(arr)):
    current_value += arr[i]
    max_value = max(max_value, current_value)

print(max_value)