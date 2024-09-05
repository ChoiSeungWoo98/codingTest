total_price = int(input())
type_cnt = int(input())
check_price = 0

for _ in range(type_cnt):
    price, cnt = map(int, input().split())
    check_price += price * cnt

if total_price == check_price:
    print("Yes")
else:
    print("No")