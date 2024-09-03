# 최댓값 설정
max = 0
maxIdx = -1

# 반복 돌려서 입력 받기
for i in range(1, 10):
    temp = int(input())
    if max < temp:
        max = temp
        maxIdx = i

# 최댓값 및 인덱스 출력
print(max)
print(maxIdx)