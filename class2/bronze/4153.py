# 각 변들의 길이가 3, 4, 5 이면 직각 삼각형 이다.
# 입력
# 테스트 케이스 0, 0, 0 입력 시 종료
while True:
    lens = list(map(int, input().split()))
    if all(v == 0 for v in lens):
        break

    a = lens[0] ** 2
    b = lens[1] ** 2
    c = lens[2] ** 2
    
    if  a + b == c or a + c == b or b + c == a:
        print("right")
        continue
    print("wrong")