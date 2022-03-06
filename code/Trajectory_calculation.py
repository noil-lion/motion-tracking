import math
import Zero_Velocity_Update as ZVU


def integral(listacc_X, listacc_Y, listacc_Z, Z, listgyo_X, listgyo_Y, listgyo_Z, listangle_R, listangle_P, listangle_Y, timestep):
    # 初始速度=0 初始位移0
    V_ling_index = []
    S_ling_index = []
    V = {}
    V_B={}
    S = {}
    V[0] = 0
    V[1] = 0
    V[2] = 0
    V[3] = 0
    V[4] = 0
    V[5] = 0
    V[6] = 0
    V[7] = 0
    V[8] = 0
    V[9] = 0
    S[0] = 0
    satic = []
    mode = 0
    for i in range(10, len(timestep)-10):
        # 0速检测基于当前时刻加速度数据特征
        if ZVU.detect(listacc_X, listacc_Y, listacc_Z, listgyo_X, listgyo_Y, listgyo_Z, listangle_R, listangle_P, listangle_Y, i):
            # satic.append(satisfy.detect(listacc_X, listacc_Y, listacc_Z, i))  # 加速度统计特征
            V[i] = 0
            V_ling_index.append(i)
        else:
            # satic.append(satisfy.detect(listacc_X, listacc_Y, listacc_Z, i))
            V[i] = V[i-1] + ((listacc_X[i]+listacc_X[i-1])*0.01/2.0)
    sample_key_list = []
    Vs = []
    for item in V.keys():
        sample_key_list.append(item)
        Vs.append(V[item])
    
    # V = filters.highpass(Vs)
    # V = filters.kalmanFitler(Vs, 0.001)
    # V = dataProcess.abnormal_discard(Vs, 1)
    V = Vs
    # vision.draw_satic(Vb[0:3000], Vs[0:3000], timestep[0:3000])
    # vision.draw_satic(V, satic, timestep )

    for k in range(1, len(timestep)-10):
        if V[k]==0 and math.acos(abs(Z[k])%1) < 0.5:   # 零速检测+姿态追踪，reset周期动作初始点
            S[k] = 0
            if S[k-1]!= 0:
                S_ling_index.append(k-1)
        else:
            S[k] = S[k-1] + ((V[k]+V[k-1])*0.01/2.0)

    sample_key_list = []
    sample_value_list = []
    for item in S.keys():
        sample_key_list.append(item)
        sample_value_list.append(S[item])
    
    return sample_value_list


def Trajectory_cal(listacc_X, listacc_Y, listacc_Z, Z, listgyo_X, listgyo_Y, listgyo_Z, listangle_R, listangle_P, listangle_Y, timestep):
    Tra_X, V_X = integral(listacc_X, listacc_Y, listacc_Z, Z, listgyo_X, listgyo_Y, listgyo_Z, listangle_R, listangle_P, listangle_Y, timestep)
    Tra_Y, V_Y = integral(listacc_Y, listacc_X, listacc_Z, Z, listgyo_X, listgyo_Y, listgyo_Z, listangle_R, listangle_P, listangle_Y, timestep)
    Tra_Z, V_Z = integral(listacc_Z, listacc_X, listacc_Y, Z, listgyo_X, listgyo_Y, listgyo_Z, listangle_R, listangle_P, listangle_Y, timestep)
    return Tra_X, Tra_Y, Tra_Z, V_X, V_Y, V_Z
