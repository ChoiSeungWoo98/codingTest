# map 선언
dupl = {}

# 10개의 숫자를 입력 받는다
for i in range(10):
    # 이를 42로 나눈 나머지를 구한다.
    num = int(input()) % 42
    dupl[num] = 1

# 서로 다른 값이 몇 개 가 있는지 출력한다.
print(len(dupl))