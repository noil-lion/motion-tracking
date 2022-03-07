import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation




def trajectory_simulation(Tra_X, Tra_Y, Tra_Z):
    fig = plt.figure(1)
    ax = fig.add_subplot(1, 1, 1, projection='3d')  # 指定三维空间做图

    t = np.linspace(0, 4, 200)  # 在0到4之间，均匀产生200点的数组
    theta = t * 2 * np.pi  # 角度

    # 生成曲线数组
    z = np.array(Tra_Z)
    x = np.array(Tra_X)
    y = np.array(Tra_Y)
    # 运动的点
    point, = ax.plot([x[0]], [y[0]], [z[0]], 'ro', label='p')

    # 曲线
    line, = ax.plot([x[0]], [y[0]], [z[0]], label='line')

    # 设置显示的范围和描述
    x_min = 0
    y_min = 0
    z_min = 0
    x_max = 1
    y_max = 1
    z_max = 1
    margin = 1
    ax.set_xlim(x_min - margin, x_max + margin)
    ax.set_ylim(y_min - margin, y_max + margin)
    ax.set_zlim(z_min - margin, z_max + margin)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    # 标题
    ax.set_title('3D animate')
    ax.view_init(30, 35)
    # 设置标签在右下角
    ax.legend(loc='lower right')
    def animate(i):
        line.set_xdata(x[:i + 1])
        line.set_ydata(y[:i + 1])
        line.set_3d_properties(z[:i + 1])
        point.set_xdata(x[i])
        point.set_ydata(y[i])
        point.set_3d_properties(z[i])

    ani = animation.FuncAnimation(fig=fig,
                                func=animate,
                                frames=len(x),
                                interval=1,
                                repeat=True,
                                )

    plt.show()