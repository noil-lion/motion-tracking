
class loadData(object):
    """数据加载"""
    def __init__(self, path):
        self.path = path

    def get_timestep(self, n):
        lists = []
        for i in range(n):
            lists.append(i)
        return lists

    def get_acc(self):
        f = open(self.path)
        line = f.readline()
        line = f.readline()
        listX = []
        listY = []
        listZ = []
        while line:
            line = f.readline()
            lines = line.split('\t')
            data = lines[2:5]
            data = list(map(float, data))
            for i in range(len(data)):
                # data[i] = int(((data[i]+250)/500)*255)
                # lists.append(data[i])
                if i == 0:
                    listX.append(data[i])
                if i == 1:
                    listY.append(data[i])
                if i == 2:
                    listZ.append(data[i])
        f.close()
        return listX, listY, listZ

    def get_gyro(self):
        f = open(self.path)
        line = f.readline()
        line = f.readline()
        listX = []
        listY = []
        listZ = []
        while line:
            line = f.readline()
            lines = line.split('\t')
            data = lines[5:8]
            data = list(map(float, data))
            for i in range(len(data)):
                # data[i] = int(((data[i]+250)/500)*255)
                # lists.append(data[i])
                if i == 0:
                    listX.append(data[i])
                if i == 1:
                    listY.append(data[i])
                if i == 2:
                    listZ.append(data[i])
        return listX, listY, listZ


    def get_angle(self):
        f = open(self.path)
        line = f.readline()
        line = f.readline()
        listX = []
        listY = []
        listZ = []
        while line:
            line = f.readline()
            lines = line.split('\t')
            data = lines[8:11]
            data = list(map(float, data))
            for i in range(len(data)):
                # data[i] = int(((data[i]+250)/500)*255)
                # lists.append(data[i])
                if i == 0:
                    listX.append(data[i])
                if i == 1:
                    listY.append(data[i])
                if i == 2:
                    listZ.append(data[i])
        return listX, listY, listZ

    def get_AGA(self):
        listacc_X = []
        listacc_Y = []
        listacc_Z = []
        listgyo_X = []
        listgyo_Y = []
        listgyo_Z = []
        listagl_X = []
        listagl_Y = []
        listagl_Z = []
        listacc_X, listacc_Y, listacc_Z = self.get_acc()
        listgyo_X, listgyo_Y, listgyo_Z = self.get_gyro()
        listagl_X, listagl_Y, listagl_Z = self.get_angle()
        return listacc_X, listacc_Y, listacc_Z, listgyo_X, listgyo_Y, listgyo_Z, listagl_X, listagl_Y, listagl_Z