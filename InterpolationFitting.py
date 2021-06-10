'''
author: feifei
date: 2021-2-6
file info: 插值拟合
'''

from scipy import interpolate
import numpy


def interpolation(xi, yi, kind):
    '''
    nearest：最邻近插值法
    zero：阶梯插值
    slinear、linear：线性插值
    quadratic、cubic：2、3阶B样条曲线插值
    '''
    Xi = numpy.array(xi)
    Yi = numpy.array(yi)
    f = interpolate.interp1d(x=Xi, y=Yi, kind=kind)
    # f2 = interpolate.interp1d(x=Xi, y=Yi, kind='quadratic')
    newX = numpy.linspace(xi[0], xi[-1], xi[-1]-xi[0]+1)
    # f函数返回对应newx的所有拟合值
    intervalResult = f(newX)
    # print(newY)

    # 返回插值横坐标集合newX和坐标对应的结果集
    return intervalResult, newX



if __name__ == '__main__':
    xi = [2003, 2004, 2008, 2010, 2014]
    yi = [33.5, 33.1, 35.4, 34.7, 35.8]
    interpolation(xi=xi, yi=yi, kind='cubic')