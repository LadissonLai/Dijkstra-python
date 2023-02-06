# 迪杰斯特拉算法python自己手写实现

# 算法步骤
# 1、建立存储连通图的邻接矩阵
# 2、创建三个列表分别存储：点A到达任一顶点的代价；点A到达任一点代价最小的上一步顶点索引；该点是否被访问；

import numpy as np
import math

INF = math.inf


# 测试连通图的邻接矩阵
#  A   B   C   D   E   F   G
# [0   2   inf inf 3   inf inf
#  2   0   2   inf inf inf inf
#  inf 2   0   3   4   3   inf
#  inf inf 3   0   inf inf 4
#  3   inf 4   inf 0   3   inf
#  inf inf 3   inf 3   0   3
#  inf inf inf 4   inf 3   0
# ]

class MGraph(object):
    def __init__(self, mx_array=None):
        if mx_array == None:
            self._matrix = np.array([[0, 2, INF, INF, 3, INF, INF],
                                     [2, 0, 2, INF, INF, INF, INF],
                                     [INF, 2, 0, 3, 4, 3, INF],
                                     [INF, INF, 3, 0, INF, INF, 4],
                                     [3, INF, 4, INF, 0, 3, INF],
                                     [INF, INF, 3, INF, 3, 0, 3],
                                     [INF, INF, INF, 4, INF, 3, 0]])
        else:
            self._matrix = mx_array

    def get_shape(self):
        return self._matrix.shape

    def get_cost(self, row, col):
        return self._matrix[row][col]

    def get_vertex_count(self):
        return self.get_shape()[0]


def Dijstra_Algorithm(mgraph, start):
    cost_acc_list = []
    path_list = []
    visit_list = []
    # 获取初始点start到其余所有点的cost列表
    vertex_count = mgraph.get_vertex_count()
    for i in range(vertex_count):
        cost_acc_list.append(mgraph.get_cost(i, start))
        path_list.append(start)
        if i == start:
            visit_list.append(True)
        else:
            visit_list.append(False)

    while not visit_all(visit_list):
        min_cost = math.inf
        min_cost_index = -1
        # 获取一步的最短路径
        for i in range(vertex_count):
            if not visit_list[i]:
                if cost_acc_list[i] < min_cost:
                    min_cost = cost_acc_list[i]
                    min_cost_index = i
        # 站在最短路径更新下一步最短路径
        visit_list[min_cost_index] = True
        for i in range(vertex_count):
            if not visit_list[i]:
                new_cost = min_cost + mgraph.get_cost(i, min_cost_index)
                if new_cost < cost_acc_list[i]:
                    cost_acc_list[i] = new_cost
                    path_list[i] = min_cost_index
    return cost_acc_list, path_list


def visit_all(visit_list):
    if False in visit_list:
        return False
    else:
        return True


def print_path(mgraph, path_list, start, end):
    # 建立索引和顶点字母的对应关系
    vertex_dict = dict()
    vertex_count = mgraph.get_vertex_count()
    a = ord('A')
    for i in range(vertex_count):
        vertex_dict[i] = chr(a + i)

    # 打印路径信息
    path_ret = list()
    path_ret.insert(0, vertex_dict[end])
    pre_index = path_list[end]
    ver_char = vertex_dict[pre_index]
    while pre_index != start:
        path_ret.insert(0, ver_char)
        pre_index = path_list[pre_index]
        ver_char = vertex_dict[pre_index]
    path_ret.insert(0, ver_char)

    for i in path_ret:
        print(i + " ", end='')


if __name__ == '__main__':
    mgraph = MGraph()
    start = 0
    end = 6
    cost_list, path_list = Dijstra_Algorithm(mgraph, start)
    print(cost_list)
    print(path_list)
    print_path(mgraph, path_list, start, end)
