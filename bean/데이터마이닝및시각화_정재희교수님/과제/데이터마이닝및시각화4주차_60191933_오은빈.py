#데이터마이닝및시각화 4주차 과제
#정보통신공학과 60191933 오은빈
import numpy as np

def main():
    Score = np.random.randint(100, size = (10, 4))
    score1 = Average1(Score)  #1번 함수 실행, 결과를 리턴
    Grade(Score)  #2번 함수 실행
    Minus_Avg(Score)  #3번 함수 실행
    score4 = Total_Score(score1)  #4번 함수 실행, 1번 함수의 결과를 사용, 결과를 리턴
    Average2(score4)  #5번 함수 실행, 4번 함수의 결과를 사용

#각 과목의 평균을 구하는 함수
def Average1(score):
    print('#1번')
    avg = score.sum(axis = 0) / 10  #각 과목당 10명의 학생에 대한 평균을 구함(열의 평균)
    data = np.vstack((score, avg))  #점수 밑에(행 추가) 평균을 붙임
    print(data)  #평균이 추가된 행렬을 출력
    print()
    return data  #4번 문제에서 사용하기 위해 결과를 리턴

#각 학생에게 성적을 부여하는 함수
def Grade(score):
    print('#2번')
    #A, B, C, D 네 종류의 성적을 부여하기 위해 where 함수를 중첩하여 사용
    data = np.where(score >= 90, 'A', np.where(score >= 80, 'B', np.where(score >= 70, 'C', 'D')))
    print(data)
    print()

#과목별 점수에서 평균 값을 뺀 점수 출력하는 함수
def Minus_Avg(score):
    print('#3번')
    avg = score.sum(axis = 0) / 10  #각 과목에 대한 평균을 구함
    data = score - avg  #각 과목별 점수에서 평균을 뺀 점수
    print(data)
    print()

#각 학생의 총점을 구하는 함수
def Total_Score(score):
    print('#4번')
    total = score.sum(axis = 1)  #행의 합(각 학생에 대한 총합), 1열로 형태를 바꿔야 함
    total = total.reshape(-1, 1)  #행렬에 붙이기 위해 n행 1열로 만들어줌
    data = np.hstack((score, total))  #1번 행렬에 총점을 붙임
    print(data)
    print()
    return data

#각 학생의 평균을 구하는 함수
def Average2(score):
    print('#5번')
    avg = np.expand_dims(score[:,4], axis = 1) / 4  #평균 = 총점 / 4(4과목), expand_dims를 사용했기 때문에 1열로 만들어짐
    data = np.concatenate([score, avg], axis = 1)  #행렬의 열에 평균 붙이기
    print(data)
    print()

main()
