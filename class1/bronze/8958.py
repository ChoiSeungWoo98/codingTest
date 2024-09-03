# 테스트 케이스 갯수
cnt = int(input())

# 테스트 갯수만큼 반복
for _ in range(cnt):
    # 테스트 데이터 입력받기
    lines = input()

    # 점수와 몇 개 연속인지 체크하는 변수 선언
    score = 0
    cnt = 0

    # 반복 돌려서 O가 중복되는 지 확인 후 최종 값에 더하기
    for char in lines:
        if char == "O":
            cnt += 1
            score += cnt
        else:    
            cnt = 0

    print(score)