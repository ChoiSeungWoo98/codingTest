# 횟수 입력
cnt = int(input())

# 횟수 만큼 반복 돌리기
for i in range(cnt):
    # 반복 횟수 및 문자열 입력받기
    r, w = map(str, input().split())
    # 사용 할 수 있는 값으로 변겅
    mul = int(r)
    words = list(w)
    result = ""

    # 문자 반복 해서 합치기
    for j in words:
        result += j *  mul
    
    print(result)