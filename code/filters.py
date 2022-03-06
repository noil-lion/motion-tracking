from scipy import signal
import numpy as np

class filters(object):

    # 滑动平均滤波 利用一维卷积实现，a是待处理数组，n为平均队列长度
    def np_move_avg(self,a,n,mode="same"):
        return(np.convolve(a, np.ones((n,))/n, mode=mode))


    def highpass(self,list):
        # 高通滤波
        fs = 100 # 采样率 (赫兹)
        fc = 10 # 截止频率 （赫兹）
        b, a = signal.butter(2, 2.0*fc/fs, 'highpass')
        data = signal.filtfilt(b, a, list)
        return data


    def lowpass(self,list):
        # 低通滤波
        fs = 100 # 采样率 (赫兹)
        fc = 3 # 截止频率 （赫兹）
        b, a = signal.butter(4, 2.0*fc/fs, 'lowpass')
        data = signal.filtfilt(b, a, list)
        return data


    # 卡尔曼滤波
    def kalmanFitler(self,data,R):
        '''

        '''
        data = np.array(data)
        n_iter = len(data)
        sz = (n_iter,)
        z = np.array(data[0:n_iter])

        Q = 1e-5
        xhat = np.zeros(sz)
        P = np.zeros(sz)
        xhatminus = np.zeros(sz)
        Pminus = np.zeros(sz)
        K = np.zeros(sz)
        R = R

        xhat[0] = 0.0
        P[0] = 1.0

        for k in range(1, n_iter):
            xhatminus[k] = xhat[k - 1]
            Pminus[k] = P[k - 1] + Q

            K[k] = Pminus[k] / (Pminus[k] + R)
            xhat[k] = xhatminus[k] + K[k] * (z[k] - xhatminus[k])
            P[k] = (1 - K[k]) * Pminus[k]
        return list(xhat)


    def LowPass(self,listacc_X, listacc_Y, listacc_Z):
        a_listacc_X = self.lowpass(listacc_X)
        a_listacc_Y = self.lowpass(listacc_Y)
        a_listacc_Z = self.lowpass(listacc_Z)
        return a_listacc_X, a_listacc_Y ,a_listacc_Z


    def HighPass(self,listacc_X, listacc_Y, listacc_Z):
        a_listacc_X = self.highpass(listacc_X)
        a_listacc_Y = self.highpass(listacc_Y)
        a_listacc_Z = self.highpass(listacc_Z)
        return a_listacc_X, a_listacc_Y ,a_listacc_Z


    def Kal(self,listacc_X, listacc_Y, listacc_Z, R):
        a_listacc_X = self.kalmanFitler(listacc_X, R)
        a_listacc_Y = self.kalmanFitler(listacc_Y, R)
        a_listacc_Z = self.kalmanFitler(listacc_Z, R)
        return a_listacc_X, a_listacc_Y , a_listacc_Z


    def Move_avg(self,listacc_X, listacc_Y, listacc_Z, n):
        a_listacc_X = self.np_move_avg(listacc_X,n)
        a_listacc_Y = self.np_move_avg(listacc_Y,n)
        a_listacc_Z = self.np_move_avg(listacc_Z,n)
        return a_listacc_X, a_listacc_Y ,a_listacc_Z

