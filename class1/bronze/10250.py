# 횟수 입력 받기
cnt = int(input())

# 층, 호수 계산
for i in range(cnt):
    h, w, n = map(int, input().split())
    f = n % h
    r = int(n / h) + 1
    # 나머지가 없는 경우 몫에서 -1을 하고 나머지에 최대 높이를 넣어준다.
    if f == 0:
        f = h
        r -= 1

    if len(str(r)) > 1:
        print(f"{f}{r}")
    else:
        print(f"{f}0{r}")