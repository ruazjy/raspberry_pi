# 第一步 以像素为单位，进行带角度的坐标转换                                     像素相对坐标系
# 第二步 将坐标转化为以毫米为单位                                               毫米绝对坐标系
# 第三步 加上平移的毫米偏移量，最终毫米绝对坐标系下的坐标

import numpy as np

# a = np.arange(10)
# print(a)
# print(a.shape)

a = np.arange(100).reshape(10, 10)
print(a)
print(a.shape)

a_index = []
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        a_index.append([i,j])
print(a_index)

matrix = [[0.6,0.8],[-0.8,0.6]]
b = np.dot(a_index, matrix)
print(b)


