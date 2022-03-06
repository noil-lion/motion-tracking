import sys


import vision
import dataProcess
import Coordinate_Transform
import numpy as np
import Trajectory_calculation as TC
from loadData import loadData as LD
from filters import filters as FL


def main(dir):

    # 数据文件目录
    # dir = "D:\\researchSpace\\task\\Data\\qbqq\\210618232419.txt"  # D:\\fes\\Data\\前臂屈伸\\B\\201231162405.txt
    # 数据加载
    loadData = LD(dir)
    listacc_X, listacc_Y, listacc_Z, listgyo_X, listgyo_Y, listgyo_Z, listangle_R, listangle_P, listangle_Y = loadData.get_AGA()   # 加载全部传感器数据。
    timestep = loadData.get_timestep(len(listacc_X))

    # 数据预处理:去除异常值，低通滤波去除高频噪声
    filters = FL()  # 创建过滤器
    listacc_X = dataProcess.abnormal_discard(listacc_X, 0.9)
    listacc_Y = dataProcess.abnormal_discard(listacc_Y, 0.9)
    listacc_Z = dataProcess.abnormal_discard(listacc_Z, 0.9)
    a_listacc_X, a_listacc_Y, a_listacc_Z = filters.LowPass(
        listacc_X, listacc_Y, listacc_Z)

    # 数值可视化
    # vision.draw_acc(listangle_R, listangle_P, listangle_Y, timestep)  # 原始数据绘图
    # vision.comparison(listacc_X, listacc_Y, listacc_Z, a_listacc_X, a_listacc_Y, a_listacc_Z, timestep)  # 预处理前后绘图

    # 初始坐标系校准
    # ---采集时校准：载体坐标系与导航坐标系对齐，且初始点坐标原点重合
    # 坐标变换
    for i in range(0, len(timestep)):
        listacc_X[i], listacc_Y[i], listacc_Z[i] = Coordinate_Transform.transform(
            a_listacc_X[i], a_listacc_Y[i], a_listacc_Z[i], listangle_R[i],
            listangle_P[i], listangle_Y[i])
    # 坐标系转换前后对比
    # vision.comparison(a_listacc_X, a_listacc_Y,  a_listacc_Z, listacc_X, listacc_Y, listacc_Z,timestep)
    # 零偏误差计算分析
    # bias_X, bias_Y, bias_Z = ZBE.Zero_bias_error(listacc_X[0:100], listacc_Y[0:100], listacc_Z[0:100], timestep[0:100])
    # 重力消去,统一单位m/s
    # raw_listacc_X, raw_listacc_Y, raw_listacc_Z = []
    real_listacc_X = []
    real_listacc_Y = []
    real_listacc_Z = []
    for i in range(0, len(timestep)):
        # raw_listacc_X.append(listacc_X[i] * 9.8)
        # raw_listacc_Y.append(listacc_Y[i] * 9.8)
        # raw_listacc_Z.append((listacc_Z[i]) * 9.8)
        real_listacc_X.append((listacc_X[i]) * 9.8)
        real_listacc_Y.append((listacc_Y[i]) * 9.8)
        real_listacc_Z.append(((listacc_Z[i]) - 1.00) * 9.8)
    Tra_X, Tra_Y, Tra_Z, V_X, V_Y, V_Z = TC.Trajectory_cal(real_listacc_X, real_listacc_Y, real_listacc_Z, a_listacc_Y, listgyo_X, listgyo_Y, listgyo_Z, listangle_R, listangle_P, listangle_Y, timestep=timestep)
    # 3D运动轨迹仿真可视化
    vision.Trajectory_simulation(Tra_X, Tra_Y, Tra_Z, 'blue')


if __name__ == '__main__':
    dir = '../Data/211111135320.txt'
    main(dir)
