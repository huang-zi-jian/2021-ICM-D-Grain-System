'''
author: feifei
date: 2021-2-5
file info: 脚本测试或者用于临时数据处理
'''
import numpy
import pandas
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 导入数据
data = pandas.read_csv('Data/proportionAgricultureWage.csv', encoding='gbk', index_col=0)

# 数据准备
valueData = data.loc['孟加拉国']
dataYear = list(data.iloc[1:2])
X = []
for year in dataYear:
    X.append(int(year))

# 遍历年份和对应的数值
Xi = []
Yi = []
# 将DataFrame数据进行list强制转换返回的结果是数据列属性列表
for year, value in zip(dataYear, valueData):
     # 记录数值不为0的年份数据（也就是非缺省数据）
     if value!= 0:
         Xi.append(int(year))
         Yi.append(value)

# X = data.index  # 定义数
# Y = data['沪深300'].values  # 定义数据点
# x = numpy.arange(0, len(data), 0.15)  # 定义观测点


# 进行样条差值
from scipy import interpolate

# 进行二阶样条差值
ipo1 = interpolate.splrep(numpy.array(Xi), numpy.array(Yi), k=2)  # 源数据点导入，生成参数
iy1 = interpolate.splev(numpy.array(X), ipo1)  # 根据观测点和样条参数，生成插值

# 进行三次样条拟合
ipo3 = interpolate.splrep(numpy.array(Xi), numpy.array(Yi), k=3)  # 源数据点导入，生成参数
iy3 = interpolate.splev(numpy.array(X), ipo3)  # 根据观测点和样条参数，生成插值

##作图
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))
ax1.plot(numpy.array(Xi), numpy.array(Yi), label='沪深300')
ax1.plot(numpy.array(X), iy1, 'r.', label='插值点')
ax1.set_ylim(min(Yi) - 10, max(Yi) + 10)
ax1.set_ylabel('指数')
ax1.set_title('线性插值')
ax1.legend()
ax2.plot(numpy.array(Xi), numpy.array(Yi), label='沪深300')
ax2.plot(numpy.array(X), iy3, 'b.', label='插值点')
ax2.set_ylim(min(Yi) - 10, max(Yi) + 10)
ax2.set_ylabel('指数')
ax2.set_title('三次样条插值')
ax2.legend()

plt.show()