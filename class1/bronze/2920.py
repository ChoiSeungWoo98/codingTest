# 숫자 8개 숫자 입력
beat = list(map(int, input().split()))

# 앞의 값
# front = beat[0]
# del beat[0]
# result = ""

# 1 ~ 8 까지 차례대로 연주 시 ascending
# 8 ~ 1 까지 차례대로 연주 시 descending
# 둘 다 아니라면 mixed
# for b in beat:
#     if front + 1 == b:
#         if(result == "descending"):
#             result = "mixed"
#             break
#         result = "ascending"
#         front = b
#         continue
#     if front - 1 == b:
#         if(result == "ascending"):
#             result = "mixed"
#             break
#         result = "descending"
#         front = b
#         continue
#     result = "mixed"
#     break


# 초기 상태 가정
result = "mixed"

# 오름차순 검사
if beat == list(range(1, 9)):
    result = "ascending"
# 내림차순 검사
elif beat == list(range(8, 0, -1)):
    result = "descending"

print(result)