def calHour(h):
    if h < 0:
        return h + 24
    return h

# 입력 시
h, m = map(int, input().split())

# 입력 분 - 45
m -= 45

if m < 0:
    m += 60
    h = calHour(h - 1)


print(f"{h} {m}")