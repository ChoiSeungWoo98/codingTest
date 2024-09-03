# 시험 점수 학점으로 반환하는 함수
def get_grade(score):
    if score >= 90:
        print("A")
        return
    if score >= 80:
        print("B")
        return
    if score >= 70:
        print("C")
        return
    if score >= 60:
        print("D")
        return
    print("F")

# 시험 점수 입력
score = int(input())
get_grade(score)