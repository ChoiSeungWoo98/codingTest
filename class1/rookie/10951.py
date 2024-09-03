import sys

# 여러 입력을 한번에 받기 위한 함수
lines = sys.stdin.readlines()
for line in lines:
    a, b = map(int, line.split())
    print(a + b)