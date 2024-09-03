# 연도가 주어진다.
year = int(input())

# 윤년이면 1 아니면 0 출력
# 윤년은 (4의 배수 and !100의 배수) or 400의 배수
r = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
print(int(r))