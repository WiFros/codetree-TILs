def print_square(n):
    for i in range(n):
        print(' '.join(str((j + i * n) % 9 + 1) for j in range(n)))

# 입력 받기
N = int(input())
print_square(N)