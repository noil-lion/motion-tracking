import numpy as np
import math

# 基于滑动窗口的零速检测
def detect(listacc_X, listacc_Y, listacc_Z, listgyo_X, listgyo_Y, listgyo_Z, listangle_R, listangle_P, listangle_Y, time):
    ''' 
    零速状态下窗口加速度均值Z,取窗口大小为10
    # 零速状态时刻前后窗口加速度值的特征差异
    '''
    """sum = 0
    for i in range(time-10, time):
        sum += listacc_X[i]
    before_ave = sum/10
    sum = 0
    for i in range(time, time+10):
        sum += listacc_X[i]
    after_ave = sum/10"""
    before_acc_var = np.var(listacc_X[time-10: time])
    after_acc_var = np.var(listacc_X[time: time+10])
    # print(before_gyo_var / after_gyo_var)
    sum_acc = math.sqrt(listacc_X[time]*listacc_X[time]+listacc_Y[time]*listacc_Y[time]+listacc_Z[time]*listacc_Z[time])
    sum_gyo = math.sqrt(listgyo_X[time]*listgyo_X[time]+listgyo_Y[time]*listgyo_Y[time]+listgyo_Z[time]*listgyo_Z[time])
    # print(sum_gyo)
    Shifting = abs((abs(listangle_R[time])-90) + (abs(listangle_P[time])-0) + (abs(listangle_Y[time])-0))/3
    mode = 0

    if abs(sum_acc)< 0.3 and sum_gyo<30 and (before_acc_var+after_acc_var) <0.2:
        mode = 1
    return mode
    

