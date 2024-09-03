# 횟수 입력 받기
cnt = int(input())

# 반복 돌리기
for i in range(1, cnt + 1):
    # 별 찍기 : 왼쪽에 공백을 넣기 위해 cnt 변수 사용
    print("{:>{}}".format("*" * i, cnt))