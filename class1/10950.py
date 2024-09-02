# 반복 횟수
cnt = int(input())

# 반복 횟수 만큼 돌면서 더하기
for i in range(0, cnt):
    a = list(map(int, input().split()))
    print(a[0] + a[1])