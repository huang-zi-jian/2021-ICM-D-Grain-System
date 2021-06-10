'''
author: feifei
date: 2021-2-5
file info: 利用插值以及最小二乘的线性方程来填充以及预测数据
'''
import pandas
from 基于python的美赛数据采集.InterpolationFitting import interpolation
from 基于python的美赛数据采集.leastSquaresEstimate import estimateLeastSquare
import csv
import os


# 函数获取指定文件夹下的所有文件名，并且返回列表数据
def getFileNames(filePath):

    files = []
    for parent, dirnames, filenames in os.walk(filePath):
        # 因为os.walk是遍历一个文件夹下的所有文件，如果parent父文件等于rootdir，
        # 那么此时的filesnames文件集合就是该文件夹下的所有文件
        if parent == filePath:
            files = filenames

    return files



def fillData(filepath, startYear, endYear):
    '''

    :param filepath: 待填充数据的路径
    :param startYear: 填充数据的开始年份
    :param endYear: 填充数据的终止年份
    :return:
    '''
    NORM_data = pandas.read_csv('province/'+filepath, encoding='gbk', index_col=0)
    print(NORM_data.index)
    # 获取非缺失值的年份数据
    dataYear = list(NORM_data.iloc[1:2])

    with open('province/dealData/'+filepath, mode='w', newline='', encoding='gbk') as csvfile:
        writer = csv.writer(csvfile)
        # temp = ['country'] + list(range(2002, 2028))
        writer.writerow(['st'] + list(range(startYear, endYear+1)))
        for index in NORM_data.index:
            data = NORM_data.loc[index]
            '''
            获取指标数据，这里一个CSV文件中不能出现两个相同index的数据，
            不然这里得到的values就是DataFrame而不是Series
            '''
            values = data.array

            # 遍历年份和对应的数值
            Xi = []
            Yi = []
            # 将DataFrame数据进行list强制转换返回的结果是数据列属性列表
            for year, value in zip(dataYear, values):
                 # 记录数值不为0的年份数据（也就是非缺省数据）
                 if value!= 0:
                     Xi.append(int(year))
                     Yi.append(value)

            intervalData, X = interpolation(xi=Xi, yi=Yi, kind='quadratic')

            # 计算para拟合系数
            estimateLeastObj = estimateLeastSquare()
            p0 = [1, 2]
            para = estimateLeastObj.function(p0 = p0, Xi = X, Yi = intervalData)[0]
            # print(para[0],para[1])

            # 分别预测向2002和2027方向预测的数据，并将结果转list，这样是为了方便后续列表的相加连接
            fittingDataForward = list(para[0]*range(startYear, int(X[0])) + para[1])
            fittingDataBackward = list(para[0]*range(int(X[-1]) + 1, endYear + 1) + para[1])

            # 向前加上index国家，然后写入CSV文件
            result = [index] + fittingDataForward + list(intervalData) + fittingDataBackward
            writer.writerow(result)



if __name__ == '__main__':
    # 循环填充缺失数据，以及数据预测
    for filename in getFileNames(filePath=r'/美赛数据采集\province'):
        fillData(filename, 2002, 2027)

    # fillData('innutritionIncidence.csv', 2002, 2027)
