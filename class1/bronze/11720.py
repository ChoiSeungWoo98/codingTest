# 숫자 갯수 입력 받기
cnt = int(input())
numList = list(input())
result = 0

# 반복 돌리기
for i in numList:
    result += int(i)

print(result)