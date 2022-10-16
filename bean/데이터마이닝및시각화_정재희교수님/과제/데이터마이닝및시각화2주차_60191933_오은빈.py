#데이터마이닝및시각화 2주차
#정보통신공학과 60191933 오은빈
import random

def main():
    print('#문제 1')
    concatenate_list()  #문제1 실행
    print()
    print('#문제 2')
    calculateGrade()  #문제2 실행

#문제 1
def concatenate_list():
    lst1 = [random.randint(1, 100) for i in range(20)]  #첫 번째 리스트 생성
    lst2 = [random.randint(1, 100) for i in range(20)]  #두 번째 리스트 생성
    lst = lst1 + lst2  #생성한 두 리스트를 합쳐 원소가 40개가 되도록 만듦
    lst = list(set(lst))  #set을 사용해 중복 값을 제거(=중복 값을 하나만 사용)
    for x in lst:
        print(x, end = ' ')  #중복 값을 제거한 리스트의 값을 출력
    print()

#문제 2
def calculateGrade():
    lst = ['A', 'B', 'C', 'D', 'E']  #가능한 답의 경우를 저장
    student = [[random.choice(lst) for _ in range(10)] for _ in range(8)]  #8명의 학생의 답을 랜덤하게 생성하여 리스트에 저장
    answer = ['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D']  #질문에 대한 정답

    for index, lst in enumerate(student):
        cnt = 0  #정답 수를 카운트할 변수
        for i in range(10):  #10개의 질문에 대하여 반복
            if lst[i] == answer[i]:
                cnt += 1  #정답인 경우 카운트 증가
        print('%d 번 학생의 정답 문항의 개수는 %d 입니다.' % (index, cnt))    
    
main()
