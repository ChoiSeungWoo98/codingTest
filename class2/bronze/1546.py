# 내 모든 점수를 점수/최댓값 * 100

# 입력
# 시험 과목수
cnt = int(input())

# 성적 리스트
scores = list(map(int, input().split()))
maxScore = max(scores)
result = 0

# 계산
for s in scores:
    result += s / maxScore * 100

# 출력
print(result / cnt)