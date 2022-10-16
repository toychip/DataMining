import random

def main():
    concatenate_list()
    calculateGrade()

def concatenate_list():
    print('# 1번')
    lst = [random.randint(1, 100) for i in range(20)]
    lst2 = [random.randint(1, 100) for i in range(20)]
    result_list = lst + lst2
    print(len(result_list))
    print(set(result_list))

def calculateGrade():
    print(); print()
    print('# 2번')
    #아스키 코드가 A~E = 65~69
    answer = ['B', 'D', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D']
    scorematrix = []
    corr_score_matrix = []

    for j in range(8):  #8명의 학생
        corr_score = 0
        score = [chr(random.randint(65, 70)) for i in range(10)]  # 각 학생의 답안 랜덤 작성
        scorematrix.append(score)  #각 학생의 답안을 매트릭스에 추가
        for k in range(10):
            if score[k] == answer[k]:
                corr_score += 1  #n번 학생이 맞춘 정답을 카운트
        corr_score_matrix.append(corr_score)  #n번 학생이 m개를 맞췄다

    print(corr_score_matrix)  #각 학생이 맞춘 개수 출력 
            

main()
