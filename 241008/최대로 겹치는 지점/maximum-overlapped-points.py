from collections import defaultdict

n = int(input())
arr = defaultdict(int)

for _ in range(n):
    x1, x2 = map(int, input().split())
    arr[x1] += 1
    arr[x2 + 1] -= 1

max_value = 0
current = 0

for key in sorted(arr.keys()):
    current += arr[key]
    max_value = max(max_value, current)

print(max_value)