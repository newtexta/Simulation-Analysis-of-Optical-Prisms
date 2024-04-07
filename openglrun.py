import os
from raytrace import faceproperties
from raytrace import pointlight
import numpy as np
import ctypes
import sys


import subprocess

# # 要运行的Python文件路径和文件名
# filename = "opengl2.py"

# # 使用subprocess模块运行Python文件
# result = subprocess.run(["python", filename], capture_output=True, text=True)

# # 输出子进程的标准输出和标准错误输出
# print("标准输出：", result.stdout)
# print("标准错误输出：", result.stderr)

# # 输出子进程的返回码
# print("返回码：", result.returncode)

# os.system("python try.py")

# os.system("python run.py")
# os.system("python openglqt5.py")

# print(ctypes.windll.shell32.IsUserAnAdmin())
# if ctypes.windll.shell32.IsUserAnAdmin():
#     pass
# else:
#     ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
#     sys.exit(0)

# # 在这里执行需要管理员权限的代码
# print("程序以管理员权限成功运行！")

if __name__ == '__main__':

#     # l = np.array([2,4,6])
#     # l2 = l/2
#     # print(l2)
#     # x1y1x2y2
#     # pointlight.raytrace2D(np.array([5,3]),[-2,1],[[[1,2],[2,1]]],[[0.5,0.6]])
#     # pointlight.raytrace2D(np.array([5,3]),[-2,1],[[[1,2],[2,1]],[[1,3],[3,1]]],[[0.5,0.6]])

# # v = np.array([1,0])
# # m = np.array([0,1])
# # # n = np.cross(m,v)
# # n = v + mE:/Extensometer/OpenGL/style

# #     # line1 = [-2, 1, 3, 4]
# #     # line2 = [1, 2, 2, 1]
# # # l1 = [1,2]
# # # l2 = [2,3]
# # # l = [l1[0] + l2[0],l1[1] + l2[1]]
# # # print(l)
# # l = abs(-30)
# # print(n)

    der = [3,1,3]
    start = [1,-1,1]
    face = [[[0,0],[1,6],1.5],[[5,0],[0,6],2.0]]
    faceside={"line1":[[0,0,0],[-2,-2,0]],"line2":[[-2,-2,0],[0,-1,0]],"line3":[[0,-1,0],[2,-2,0]],"line4":[[2,-2,0],[0,0,0]]}
    faceside2={"line1":[[0,1,0],[-2,-2,0]],"line2":[[-2,-2,0],[0,-1,0]],"line3":[[0,-1,0],[2,-2,0]],"line4":[[2,-2,0],[0,1,0]]}
    face3D = [[[-2,-2,0],[4,0,0],[-2,2,0]]]
    faceside2={"line1":[[0,0,0],[-2,-2,0]],"line2":[[-2,-2,0],[2,-2,0]],"line3":[[2,-2,0],[0,0,0]]}
    n_all = [[0.5,0.6]]

    result1 = faceproperties.face3D(faceside)
    conclusion = faceproperties.face3D(faceside2)
    # print(conclusion)
    conclusion1 = [{'dot1': [[2, 0, 0], ['L2', 'L1'], True], 'dot2': [[1, 1, 1], ['L1', 'L3'], True], 'dot3': [[1, 1, -1], ['L3', 'L1'], True]}]
    der = [-1,0,0]
    start = [3,0.5,0]
    face3D = [[[2,0,0],[1,1,1],[1,1,-1]]]
    n_all = [[1.0,1.5]]
    print(len(n_all))
    # direction = pointlight.determine3D(der,start,conclusion1,face3D)
    interaction = [[1.5,0.5,0]]
    # trace = pointlight.raytrace3D(der,start,interaction,face3D,n_all)

    start = [-5.7,2.5,-2]
    der = [-7.15541753,2,-2]
    conclusion1 = [{'dot1': [[1, -1, 1], ['L3', 'L7'], True], 'dot2': [[1, 1, 1], ['L7', 'L6'], True], 'dot3': [[1, 1, -1], ['L6', 'L8'], True],'dot4':[[1,-1,-1],['L8','L3'],True]}]
    face3D = [[[1,-1,1],[1,1,1],[1,1,-1],[1,-1,-1]]]
    # direction = pointlight.determine3D(der,start,conclusion1,face3D)
    # print(direction)
    interaction = [[1,0.6,-0.1]]
    n_all = [[1.5,1.0]]
    trace = pointlight.raytrace3D(der,start,interaction,face3D,n_all)
    # print(direction)
#     conclusions = [conclusion]
#     rr = pointlight.determine3D(der,start,conclusions,face3D)
#     Intersection = [rr]
#     dd = pointlight.raytrace3D(der,start,Intersection,face3D,n_all)
#     # print(result1)
#     print(rr)
#     print(dd)
#     # print(faceside2["line1"])


# def compute_perpendicular_foot(A, B, P):
#     AB = [B[0] - A[0], B[1] - A[1], B[2] - A[2]]
#     PQ = [P[0] - A[0], P[1] - A[1], P[2] - A[2]]
    
#     AB_dot_PQ = AB[0] * PQ[0] + AB[1] * PQ[1] + AB[2] * PQ[2]
#     AB_dot_AB = AB[0] * AB[0] + AB[1] * AB[1] + AB[2] * AB[2]
    
#     t = AB_dot_PQ / AB_dot_AB
    
#     Q = [A[0] + t * AB[0], A[1] + t * AB[1], A[2] + t * AB[2]]
    
#     return Q

# # 示例使用
# A = [1, 2, 3]
# B = [4, 5, 6]
# P = [7, 8, 9]

# Q = compute_perpendicular_foot(A, B, P)
# print(Q)
# def orthogonal_vector_3d(vector):
#     # 定义一个单位向量
#     u1 = vector / np.linalg.norm(vector)
    
#     # 随机选择一个与u1不平行的向量作为参考向量
#     reference_vector = np.array([1.0, 0.0, 0.0])
#     if np.dot(u1, reference_vector) == 1:
#         reference_vector = np.array([0.0, 1.0, 0.0])
    
#     # 计算与参考向量正交的向量
#     v2 = np.cross(u1, reference_vector)
#     u2 = v2 / np.linalg.norm(v2)
    
#     # 计算与u1和u2都正交的向量
#     u3 = np.cross(u1, u2)
    
#     return u2, u3

# # 测试
# vector = np.array([1.0, 2.0, 3.0])
# u2, u3 = orthogonal_vector_3d(vector)
# print("正交向量1：", u2)
# print("正交向量2：", u3)


# li = ["FALSE","NONE","TRUE"]
# print(bool("NONE" in li))
            

# lll = [["line1"]]
# ll = lll[0][0][-1]
# print(ll)

# r = result1.get("dot1")
# if r[-1]:
#     print(r[-1])
















# os.system("python opengl2.py")
# os.system("python use.py")
# os.system("python ls.py")

















# my_dict = {"a": 1, "b": 2, "c": 3}
# keys_list = list(my_dict)
# keynum = keys_list.index("b")
# print(keynum)
# import numpy as np

# my_list = [[1, 2], [3, 4], [5, 6], [7, 8]]

# # 根据索引将两个元素替换为一个元素
# index = 1  # 要替换的元素所在的索引

# # 创建新的元素，并替换原来的两个元素
# new_element = [9, 10]
# my_list[index:index + 2] = [new_element]

# print(my_list)


# def intersection_of_line_and_plane(a, b, p, d):
#     # 计算面的法向量
#     n = np.cross(a, b)
#     print(type(n))
    
#     # 判断法向量与方向向量是否垂直
#     if np.dot(n, d) == 0:
#         print("直线与平面平行或重合，无交点")
#         return None
    
#     # 计算参数t
#     t = -np.dot(n, p) / np.dot(n, d)
    
#     # 计算交点坐标
#     intersection = p + t * d
    
#     return intersection

# # 示例数据
# a = np.array([1, 2, 3])   # 面上的向量a
# b = np.array([4, 5, 6])   # 面上的向量b
# p = np.array([7, 8, 9])   # 直线上的一点p
# d = np.array([-5, -3, -4])  # 直线的方向向量d

# # 调用函数计算交点
# intersection = intersection_of_line_and_plane(a, b, p, d)

# if intersection is not None:
#     print("交点坐标：", intersection)
#     print(type(intersection))

# import numpy as np

# # 已知平面上两个向量a和b、平面上一点P、直线上一点Q和方向向量d
# a = np.array([1, 1, 1])  # 平面上的向量a
# b = np.array([-1, 1, -1])  # 平面上的向量b
# p = np.array([1, 2, 3])  # 平面上的点P
# q = np.array([1, 1, 1])  # 直线上的点Q
# d = np.array([1, 1, 2])  # 直线的方向向量d

# # 计算平面的法向量n
# n = list(np.cross(a, b))
# print(n)

# # 判断n·d是否为零
# if np.dot(n, d) == 0:
#     print("直线与平面平行或共面，无交点")
# else:
#     D = - (np.dot(n,p))
#     print(D)
#     t = -(np.dot(n,q) + D)/(np.dot(n,d))
#     print(t)
#     r = q + t * d
#     print(r)
#     # 计算参数t
#     t = np.dot(n, p - q) / np.dot(n, d)

#     # 计算交点R
#     r = q + t * d

#     print("交点R的坐标为：", r)





# import numpy as np

# my_list = [np.array([0, 0, 2]), np.array([0, 0, -4]), np.array([0, 0, 2]), np.array([0, 0, 8])]


# to_remove = my_list[2]  # 要删除的元素

# if np.array_equal(to_remove, my_list[2]):  # 判断要删除的元素是否与列表中的元素相等
#     removed_element = my_list.pop(2)  # 使用 pop 方法从列表中删除相等的元素


# print(my_list)  # 输出 [array([0, 0, -4]), array([0, 0, 2]), array([0, 0, 8])]



# import sqlite3

# # 创建连接对象
# conn = sqlite3.connect("mydatabase.sqlite")

# # 创建游标对象
# cursor = conn.cursor()

# # 执行SQL语句以创建表
# cursor.execute("""CREATE TABLE users
#                   (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)""")

# # 关闭连接
# conn.close()

# lst = [[3, 5, 1], [4, 3, 2], [4, 5, 8], [4, 3, 2], [3, 5, 1]]

# # 将列表转换为集合，去除重复项，再转换回列表
# unique_lst = list(set(map(tuple, lst)))

# print(unique_lst)
# import numpy as np

# 定义多个三维向量
# vectors = np.array([[1, 0, 0], [0, 1, 0], [2, 0, 0], [0, 3, 0]])

# # 初始化零向量的数量
# num_zero_vectors = 0

# # 计算叉乘结果
# cross_products = []
# for i in range(len(vectors)):
#     for j in range(i+1, len(vectors)):
#         cross_product = np.cross(vectors[i], vectors[j])
#         cross_products.append(cross_product)
#         if np.linalg.norm(cross_product) == 0:
#             num_zero_vectors += 1

# # 判断向量方向是否一致
# if num_zero_vectors < len(vectors) - 1:
#     print("部分向量的方向不一致")
# else:
#     print("所有向量的方向是一致的")

# # 输出叉乘结果
# print("各向量叉乘结果：\n", cross_products)

# vec = np.array([1,0,0])
# ve = np.array([1,0,0])
# cr = vec + ve
# if cr.all() == np.array([2,1,2]).all():
# 	print(cr == np.array([2,0,0]))

