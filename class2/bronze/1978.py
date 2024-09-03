# 소수 찾기
# 에라토스테네스의 체 공식 활용
# 2를 제외한 2의 배수 지우기 남은 숫자 중 가장 작은 수를 제외한 배수 지우기...
# 위 사항 반복

# 입력
# 수의 개수
num = int(input())

# 데이터 받기
datas = list(map(int, input().split()))

# 구현
# 최대 숫자 찾기
max_data = max(datas)

# 소수 체크를 위한 리스트 선언
check = [True] * (max_data + 1)

# 0과 1은 소수가 아니기 때문에 False로 바꾼 후 넘기기
check[0] = check[1] = False

# 에라토스테네스의 체 구현
for i in range(2, int(max_data ** 0.5) + 1):
    if check[i]:  # i가 소수인 경우
        for j in range(i * i, max_data + 1, i):
            check[j] = False  # i의 배수를 모두 False로 설정

# 출력
# 데이터를 반복 돌려 체크리스트가 True인 데이터를 1씩 더하기
result = sum(1 for d in datas if check[d])
print(result)