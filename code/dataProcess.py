from numpy import *
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline
import pandas as pd


# 输出数据包括系统测量噪声[4] ,且噪声主要为高频信号。为了减少信号的干扰噪声,须对信号进行滤波。本文对加速度信号用中值滤波器滤除数据中的噪声。
# 中值滤波


# 去重
def interpolation(xArray, yArray, num):
    new_x = []
    new_y = []

    new_x = np.linspace(mat(xArray).min(), mat(xArray).max(), num)
    # print(len(new_x))
    # print(new_x)
    spl = make_interp_spline(xArray, yArray, k=3)
    new_y = spl(new_x)
    return new_x, new_y


# 异常值去除
def abnormal_discard(data,threshold):
    '''
    计算上界下界，并剔除异常值，返回新数据，被剔除数据用左右两侧的均值代替
    输入：原始数据
    返回：剔除异常值的数据
    '''
    ret = data.copy()
    data = sorted(data)
    percentile = np.percentile(list(set(data)), (25, 50, 75), interpolation='linear')
    Q1 = percentile[0]
    Q3 = percentile[2]
    IQR = Q3 - Q1  #四分位距
    ulim = Q3 + threshold * IQR
    llim = Q1 - threshold * IQR
    for i in range(len(ret)):
        if ret[i] > ulim or ret[i] < llim:
            ret[i] = 0
    for i in range(len(ret)):
        if ret[i] == 0:
            k = 1
            while True:
                if  i+k > len(ret)-1:
                    ret[i] = ret[i-1]
                    break
                elif ret[i+k] != 0:
                    replaced_value = ret[i-1] + ret[i+k]
                    ret[i] = replaced_value / 2
                    break
                else:
                    k = k + 1
    return ret
