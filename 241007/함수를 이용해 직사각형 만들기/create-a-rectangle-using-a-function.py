def print_rect(n,m):
    for _ in range(n):
        print('1' * m)

print_rect(*map(int,input().split(' ')))