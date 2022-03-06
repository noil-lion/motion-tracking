import math
import numpy as np


# 旋转矩阵构建
def transform(acc_X, acc_Y, acc_Z, angle_P, angle_R, angle_Y):
    '''
    导航坐标系：东北天坐标系（ENU）:X-东， Y-北， Z-垂直平面指向天
    载体坐标系：右前上系：X-右， Y-前， Z-垂直平面指向上
    欧拉角是描述旋转的一种方式，定义姿态角为偏航（Yaw），俯仰（Pitch），横滚（Roll）
    右前上坐标系下，Z对应偏航，Y对应横滚，X对应俯仰。所以在常用的姿态旋转顺序（Yaw-Pitch-Roll）中，对应的旋转方式为（Z-X-Y）
    旋转轴分绕固定坐标系旋转和绕动坐标系旋转，前者称为外旋，后者称为内旋。 - Fixed Angles 外旋 - Euler Angles 内旋
    旋转矩阵(DCM)又称为方向余弦矩阵
    '''

    sin_P = math.sin(math.radians(angle_P))
    cos_P = math.cos(math.radians(angle_P))
    sin_R = math.sin(math.radians(angle_R))
    cos_R = math.cos(math.radians(angle_R))
    sin_Y = math.sin(math.radians(angle_Y))
    cos_Y = math.cos(math.radians(angle_Y))
    transX_martrix = np.array(
                             [[1, 0 , 0],
                             [0, cos_P, -1*sin_P],
                             [0, sin_P, cos_P]])
    transY_martrix = np.array(
                             [[cos_R, 0, sin_R],
                             [0, 1 , 0],
                             [-1*sin_R, 0, cos_R]])
    transZ_martrix = np.array(
                             [[cos_Y, -1*sin_Y, 0],
                             [sin_Y, cos_Y, 0],
                             [0, 0 , 1]])
    tensor = np.array([acc_X, acc_Y, acc_Z]).T
    result = np.dot(transX_martrix, tensor)
    result = np.dot(transY_martrix, result)
    result = np.dot(transZ_martrix, result)
    return result[0], result[1], result[2]
