result = []

while True:
    num = input()
    if num == "0 0":
        break
    a, b = map(int, num.split())
    result.append(a + b)

for i in result:
    print(i)