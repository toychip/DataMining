import numpy as np

def main():
    Score = np.random.randint(100, size = (10, 4))
    avg_subj = problem1(Score)  #1번 문제의 정답을 리턴
    problem2(Score)
    problem3(Score)
    problem4(avg_subj)  #1번 정답을 사용
    problem5(avg_subj)  #1번 정답을 사용

def problem1(score):
    arg = score.mean(axis = 0)  #행 고정 = 열에 대한 평균
    arg = arg.reshape(1, 4)  #밑에 붙여야 되니까 모양을 (1,4)로 변경
    arg_sub = np.concatenate([score, arg], axis = 0)  #행에 대하여 붙이기
    print(arg_sub)
    return arg_sub

def problem2(score):
    grade = np.where(score >= 90, 'A', np.where(score >= 80, 'B', np.where(score >= 70, 'C', 'D')))
    print(grade)

def problem3(score):
    score_mean = score.mean(0)  #열의 평균 구하기
    score_mean_sub = score_mean.reshape((1, 4))  #빼기 위해 모양을 (1,4)로 변경
    score_mean = score - score_mean_sub  #0열은 전부 0열이 빼지고, 1열은 전부 1열이 빼지고 ...
    print(score_mean)

def problem4(arg_subj):
    arg = arg_subj.sum(axis = 1)  #행의 합
    arg = arg.reshape(11, 1)  #옆에 붙이기 위해 (11,1)으로 모양 바꾸기
    arg_score_sum = np.concatenate([arg_subj, arg], axis = 1)  #열에 대하여 붙이기
    print(arg_score_sum)

def problem5(arg_subj):
    total = arg_subj.sum(axis = 1).reshape((11, 1))  #4번과 똑같은 문제
    avg = arg_subj.mean(axis = 1).reshape((11, 1))  #행에 대한 평균
    arg_sub_r = np.concatenate([arg_subj, total, avg], axis = 1)  #점수표에 총합, 평균을 순서대로 붙임
    print(arg_sub_r)

main()