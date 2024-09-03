import math
# 티셔츠 한 장 펜 한 자루 를 나눠준다.
# 티셔츠 사이즈 : S, M, L, XL, XXL, XXXL
# 같은 사이즈는 N장의 묶음으로 주문 가능
# 펜은 한 종류로 N 자루씩 묶음 주문 혹은 한 자루씩 주문 가능
# 티셔츠는 남아도 되지만 부족하면 안된다.
# 펜은 정확해야 한다.


# 결론
# 티셔츠는 T장씩 몇 묶음?
# 펜은 묶음 주문 후 개별 주문 몇 개?

# 입력
# 참가자 수
cnt = int(input())

# 티셔츠 사이즈별 신청자 수
# S, M, L, XL, XXL, XXXL - 6가지 인덱스 5
ts = list(map(int, input().split()))

# 정수 티셔츠와 펜의 묶음 수 (티셔츠, 펜)
tb, pb = map(int, input().split())


tbResult = 0

# 구현
# 티셔츠
# 신청자 수 반복
for size in ts:
    # 0인 경우 컨티뉴
    if size == 0:
        continue
    # 티셔츠 묶음 수로 나눈 후 + 1 갯수 추가
    tbResult += math.ceil(size / tb)
# tb_result = sum(math.ceil(size / tb) for size in ts)

# 출력
# 티셔츠 묶음 수 출력
print(tbResult)
# 펜 자루 수 및 개별 자루 수 출력
print(f"{int(cnt / pb)} {cnt % pb}")