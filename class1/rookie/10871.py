# 자연수 A, B 입력
a = list(map(int, input().split()))
numList = list(map(int, input().split()))

for i in numList:
    if(i < a[1]):
        print(i)