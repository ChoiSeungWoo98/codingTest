# 고유 번호 받기
num = list(map(int, input().split()))
# 결과 값 계산을 위한 변수 선언
result = 0

# 모든 숫자를 제곱해서 결과 값에 더하기
for i in num:
    result += i ** 2

# 10 으로 나눈 나머지 값을 담기 및 출력
result = result % 10
print(result)