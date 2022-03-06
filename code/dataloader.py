
from ctypes import sizeof
from tkinter.messagebox import NO
import loadData as LD
from sklearn import preprocessing
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA # 导入Kmeans 与PCA模块
import vision 

# 构建时序信号的特征向量样本矩阵。
class dataLoader(object):
    def __init__(self, path):
        self.path = path
        self.loader = LD.loadData(self.path)
        
        
        self.listacc_X, self.listacc_Y, self.listacc_Z, self.listgyo_X, self.listgyo_Y, self.listgyo_Z, self.listagl_X, self.listagl_Y, self.listagl_Z= self.loader.get_AGA()
        """a_listacc_X, a_listacc_Y, a_listacc_Z = filters.LowPass(
            listacc_X, listacc_Y, listacc_Z)
        self.listacc_X, self.listacc_Y, self.listacc_Z, self.listgyo_X, self.listgyo_Y, self.listgyo_Z, self.listagl_X, self.listagl_Y, self.listagl_Z = a_listacc_X, a_listacc_Y, a_listacc_Z, listgyo_X, listgyo_Y, listgyo_Z, listagl_X, listagl_Y, listagl_Z
        """
        self.timesteps= self.loader.get_timestep(len(self.listacc_X))

    def sample_generator(self, stride, size, mode):
        self.samples= []
        if self.path == None:
            return -1
        elif mode == 'slide':
            for i in range(0, len(self.timesteps)-size-1):
                for k in range(i, i+size):
                    sample = preprocessing.StandardScaler().fit(np.array([self.listacc_X[k], self.listacc_Y[k], self.listacc_Z[k], self.listgyo_X[k], self.listgyo_Y[k], self.listgyo_Z[k], self.listagl_X[k], self.listagl_Y[k], self.listagl_Z[k]]).reshape(1, -1))
                    self.samples.append(sample)
            i = i+stride
        elif mode == 'full':
            for k in range(0, len(self.timesteps)-size-1):
                sample = [self.listacc_X[k], self.listacc_Y[k], self.listacc_Z[k], self.listgyo_X[k], self.listgyo_Y[k], self.listgyo_Z[k], self.listagl_X[k], self.listagl_Y[k], self.listagl_Z[k]]
                self.samples.append(sample)
        return self.samples
    def detect(self, n_clusters=2, n_components=3):
        samples = self.sample_generator(stride=50, size=300, mode='full')
        ss = preprocessing.StandardScaler(copy=True, with_mean=True, with_std=True)
        Data = []
        for i in range(0,len(samples)):
            list = ss.fit_transform(np.array(samples[i]).reshape(-1, 1))
            meta = []
            for k in range(0, len(list)):
                meta.append(list[k][0])
            Data.append(meta)
        kmeans = KMeans(n_clusters) # 设定初始质心数
        pca = PCA(n_components) # 设定降维数
        pca.fit(Data) # 训练数据
        data1_pca = pca.transform(Data) # 进行PCA降维
        data1_pca # 查看降维后数据
        kmeans.fit(data1_pca) # 将降维后的数据进行聚类训练
        y = kmeans.predict(data1_pca) # 预测聚类结果
        vision.draw_satic(self.listacc_Y, y,self.timesteps)
        return y

"""def vision():
    # Set up a logs directory, so Tensorboard knows where to look for files 
    log_dir='logs/test/'
    feature_vectors =np.loadtxt('features.txt')
    weights=tf. Variable(feature_vectors)
    # Create a checkpoint from embedding, the filename and key are
    # name of the tensor.
    checkpoint=tf. train. Checkpoint(embedding=weights)
    checkpoint.save(os.path. join(log_dir,"embedding.ckpt"))
    # Set up config 
    config=projector.ProjectorConfig()
    embedding=config.embeddings.add()
    # The name of the tensor will be suffixed by/. ATTRIBUTES/VARIABLE VALUE'
    embedding.tensor_name="embedding/.ATTRIBUTES/VARIABLE_VALUE"
    embedding.metadata_path='metadata.tsv'
    projector.visualize_embeddings(log_dir, config)"""


"""
if __name__=='__main__':
    PATH = '211111140301.txt'
    DL = dataLoader(PATH)
    samples = DL.sample_generator(stride=50, size=300, mode='full')
    ss = preprocessing.StandardScaler(copy=True, with_mean=True, with_std=True)
    list = ss.fit_transform(np.array(samples).reshape(-1, 1))#数据标准化
    import codecs
    f = codecs.open("features.txt",'w','utf-8')
    #f.write(str(list))
    for i in range(3000,5500):
        list = ss.fit_transform(np.array(samples[i]).reshape(-1, 1))
        for k in range(0, len(list)):
            f.write(str(list[k][0])+'\t')
        f.write('\n')  #\r\n为换行符
    f.close()
    Data = []
    for i in range(0,len(samples)):
        list = ss.fit_transform(np.array(samples[i]).reshape(-1, 1))
        meta = []
        for k in range(0, len(list)):
            meta.append(list[k][0])
        Data.append(meta)
    print(np.array(Data).shape)
    print(len(Data), len(Data[0]))
    kmeans = KMeans(n_clusters=2) # 设定初始质心数
    pca = PCA(n_components=3) # 设定降维数
    pca.fit(Data) # 训练数据
    data1_pca = pca.transform(Data) # 进行PCA降维
    data1_pca # 查看降维后数据
    kmeans.fit(data1_pca) # 将降维后的数据进行聚类训练
    y = kmeans.predict(data1_pca) # 预测聚类结果
    vision.draw_satic(DL.listacc_Y, y,DL.timesteps)
    plt.scatter(data1_pca[:,0],data1_pca[:,1],c = y) # 将聚类结果可视化
    plt.show()
    # vision()"""


