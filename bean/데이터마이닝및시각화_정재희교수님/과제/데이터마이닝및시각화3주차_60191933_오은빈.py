#데이터마이닝및시각화 3주차 과제
#정보통신공학과 60191933 오은빈
import numpy as np

def main():
    Score = np.random.randint(100, size = (10, 4))  # 10명의 4과목 점수를 랜덤으로 생성
    Math(Score)  # 1번 함수 실행
    Score_sum(Score)  # 2번 함수 실행
    Student(Score)  # 3번 함수 실행
    Transpose(Score)  # 4번 함수 실행

# 모든 학생의 수학 점수만 출력하는 함수
def Math(score):
    print('#1번')
    for i, x in enumerate(score, 1):  #각 학생에게 1번부터 10번까지 번호를 매기고, 수학 점수인 2열(3번째 열)을 출력
        print('{}번째 학생의 수학 점수는 {}'.format(i, x[2]))
    print()

# 각 학생의 총 합 점수를 구하는 함수
def Score_sum(score):
    print('#2번')
    for i, x in enumerate(score):  #sum 함수를 이용해 학생의 모든 과목 점수를 더해 출력
        print('{}번째 학생의 과목 총 합 점수는 {}'.format(i + 1, sum(x)))
    print()

# 불린 인덱스를 이용하여 특정 학생의 점수만 출력하는 함수
def Student(score):
    print('#3번')
    #1, 5, 7, 9, 10번째 학생의 데이터만 출력하기 위해 조건을 적은 리스트를 만듦
    condLst = np.array(['P', 'N', 'N', 'N', 'P', 'N', 'P', 'N', 'P', 'P'])
    cond = condLst == 'P'  #P(print)이면 조건을 만족하여 true, N(not)이면 false
    print(score[cond])  #조건을 만족한 학생의 점수만 출력
    print()

# 학생과 과목을 바꾸는 함수
def Transpose(score):
    print('#4번')
    score = score.transpose(1, 0)  #행과 열을 바꿈
    print(score)

main()
