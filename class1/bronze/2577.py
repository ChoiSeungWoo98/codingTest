# 값 입력 받기
mul = list(str(int(input()) * int(input()) * int(input())))
# count를 하기 위한 a 맵 선언
a = {}

# 반복문을 돌면서 한글자씩 출력
for i in mul:
    # 해당 문자열이 키로 있는 값이 있다면 해당 값에 + 1 을 아니라면 0에 + 1을 하도록 구현
    a[i] = a.get(i, 0) + 1

# 0부터 9까지 반복 돌면서 값이 없으면 0을 있으면 해당 값을 출력
for i in range(10):
    print(a.get(str(i), 0))