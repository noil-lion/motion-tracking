import matplotlib.pyplot as plt
import matplotlib.font_manager as fm  # 字体管理器

# 加速度数据绘图
def draw_acc(listX, listY, listZ, time_step):
    ln1, = plt.plot(time_step, listX,color='red',linewidth=2.0,linestyle='-')
    ln2, = plt.plot(time_step, listY,color='blue',linewidth=2.0,linestyle='-')
    ln3, = plt.plot(time_step, listZ,color='yellow',linewidth=2.0,linestyle='-')
    plt.title("sensor data change")  # 设置标题及字体
    plt.legend(handles=[ln1,ln2,ln3],labels=['acc_X','acc_Y', 'acc_Z'])
    ax = plt.gca()
    ax.spines['right'].set_color('none')  # right边框属性设置为none 不显示
    ax.spines['top'].set_color('none')    # top边框属性设置为none 不显示
    plt.xlabel("timeStep/ms")
    plt.ylabel("m/s²")
    plt.show()


# 数据过滤前后对比
def comparison(b_listX, b_listY, b_listZ, a_listX, a_listY, a_listZ, time_step):
    ln1, = plt.plot(time_step, b_listX, color='limegreen', linewidth=2.0, linestyle=':')
    ln2, = plt.plot(time_step, b_listY, color='burlywood', linewidth=2.0, linestyle=':')
    ln3, = plt.plot(time_step, b_listZ, color='cornflowerblue', linewidth=2.0, linestyle=':')
    ln4, = plt.plot(time_step, a_listX, color='limegreen', linewidth=2.0, linestyle='-')
    ln5, = plt.plot(time_step, a_listY, color='burlywood', linewidth=2.0, linestyle='-')
    ln6, = plt.plot(time_step, a_listZ, color='cornflowerblue', linewidth=2.0, linestyle='-')
    plt.title("sensor data change ")  # 设置标题及字体
    plt.legend(handles=[ln1, ln2, ln3, ln4, ln5, ln6], labels=['Raw_acc_X', 'Raw_acc_Y', 'Raw_acc_Z', 'Clean_acc_X', 'Clean_acc_Y', 'Clean_acc_Z'])
    ax = plt.gca()
    plt.grid(ls='-', color='whitesmoke', linewidth=1.0)
    ax.spines['right'].set_color('none')  # right边框属性设置为none 不显示
    ax.spines['top'].set_color('none')    # top边框属性设置为none 不显示
    plt.xlabel("timeStep/ms")
    plt.ylabel("Triaxial component of acceleration(m/s²)")
    plt.show()
    plt.close()


# 角度绘图
def comparison_angle(b_listX, a_listX, time_step):
    ln1, = plt.plot(time_step, b_listX, color='limegreen', linewidth=2.0, linestyle=':')
    ln4, = plt.plot(time_step, a_listX, color='limegreen', linewidth=2.0, linestyle='-')
    plt.title("sensor data change ")  # 设置标题及字体
    plt.legend(handles=[ln1, ln4], labels=['Raw_X',  'New_X'])
    ax = plt.gca()
    plt.grid(ls='-', color='whitesmoke', linewidth=1.0)
    ax.spines['right'].set_color('none')  # right边框属性设置为none 不显示
    ax.spines['top'].set_color('none')    # top边框属性设置为none 不显示
    plt.xlabel("timeStep/ms")
    plt.ylabel("(/。)")
    plt.show()
    plt.close()


# 轨迹仿真绘图
def Trajectory_simulation(Tra_X, Tra_Y, Tra_Z, Color):
    # 3维空间可视化数据
    ax1 = plt.axes(projection='3d')
    # ax1.grid(False)
    ax1.scatter3D(Tra_X, Tra_Y, Tra_Z, c=Tra_X, cmap='winter')  # 绘制散点图
    ax1.set_zlim(-0.5, 0.5)
    ax1.set_ylim(-0.5, 0.5)
    ax1.set_xlim(-0.5, 0.5)
    # ax1.scatter3D(integral3_XaccMat, integral3_YaccMat, integral3_ZaccMat, edgecolors='black')  # 绘制散点图
    # ax1.plot3D(integral3_XaccMat, integral3_YaccMat, integral3_ZaccMat)    # 绘制空间曲线
    plt.xlabel("X (m)")
    plt.ylabel("Y (m)")
    plt.show()


# 统计数值绘图
def draw_satic(listacc_X, satic, timestep):
    ln1, = plt.plot(timestep[0:len(satic)], satic, color='blue',linewidth=2.0,linestyle='-')
    ln2, = plt.plot(timestep[0:len(listacc_X)], listacc_X, color='black',linewidth=2.0,linestyle='-')
    plt.title("Zero Velocity Updata",fontsize=18)  # 设置标题及字体
    plt.legend(handles=[ln1, ln2],labels=['Velocity after ZUPT', 'Raw velocity'],fontsize=16)
    ax = plt.gca()
    ax.spines['right'].set_color('none')  # right边框属性设置为none 不显示
    ax.spines['top'].set_color('none')    # top边框属性设置为none 不显示
    
    plt.xlabel("time steps /ms",fontsize=16)
    plt.ylabel("m/s",fontsize=16)
    plt.ylim(-1.5,1.5)
    # 设置坐标标签字体大小
    plt.show()


# 速度绘图
def draw_Volocity(satic, timestep):
    ln1, = plt.plot(timestep[0:len(satic)], satic, color='cornflowerblue',linewidth=2.0,linestyle='-')
    
    plt.title("Results of Zero-Velocity detection")  # 设置标题及字体
    plt.legend(handles=[ln1],labels=['Velocity'])
    ax = plt.gca()
    ax.spines['right'].set_color('none')  # right边框属性设置为none 不显示
    ax.spines['top'].set_color('none')    # top边框属性设置为none 不显示
    plt.grid(ls='-', color='whitesmoke', linewidth=1.0)
    plt.ylabel("velocity(m/s)")
    plt.xlabel("timeStep/ms")
    plt.show()


# 速度修正前后对比绘图
def comparison_Velocity(b_listX, a_listX, time_step):
    ln1, = plt.plot(time_step, b_listX, color='limegreen', linewidth=2.0, linestyle=':')
    ln4, = plt.plot(time_step, a_listX, color='limegreen', linewidth=2.0, linestyle='-')
    plt.title("Zero Velocity Updata ")  # 设置标题及字体
    plt.legend(handles=[ln1, ln4], labels=['Raw_X',  'New_X'])
    ax = plt.gca()
    plt.grid(ls='-', color='whitesmoke', linewidth=1.0)
    ax.spines['right'].set_color('none')  # right边框属性设置为none 不显示
    ax.spines['top'].set_color('none')    # top边框属性设置为none 不显示
    plt.xlabel("timeStep/ms")
    plt.ylabel("(/。)")
    plt.show()
    plt.close()