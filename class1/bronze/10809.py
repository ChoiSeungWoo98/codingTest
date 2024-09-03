import string

# 알파벳 리스트
alphabet_list = list(string.ascii_lowercase)

# 단어 입력 받기
word = input()
check = {}

# 단어에서 각 알파벳의 첫 등장 위치 기록
for i, ch in enumerate(word):
    if ch not in check:
        check[ch] = i

# 알파벳을 순환하면서 check에 해당 값 출력 없으면 -1 출력해서 문자열로 담기
result = [str(check.get(a, -1)) for a in alphabet_list]
print(" ".join(result))