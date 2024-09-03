# 최댓값 설정
cnt = int(input())
nums = list(map(int, input().split()))

max = -1000001
min = 1000001

# 반복 돌려서 입력 받기
for i in nums:
    if i > max:
        max = i
    if i < min:
        min = i

# 출력
print(f"{min} {max}")