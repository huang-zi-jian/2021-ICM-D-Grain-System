'''
author: feifei
date: 2021-2-6
file info: 最小二乘法法拟合
'''

from scipy.optimize import leastsq
import numpy

class estimateLeastSquare():
    ###需要拟合的函数func及误差error###

    # k,b表示为线性拟合
    def _func(self, p, x):
        k,b=p
        return k*x+b

    def _error(self, p, x, y, s):
        #看打印多少条s,就是leastsq调用了多少次error函数
        print(s)
        # x、y都是列表，故返回值也是个列表
        return self._func(p, x) - y

    def function(self, **kwargs):
        '''

        :param kwargs:
             p0: 输入的初始系数值
             Xi: 待拟合的x数据
             Yi: 待拟合的y数据
        :return: 返回拟合后的系数
        '''
        p0 = kwargs.get('p0')
        Xi = kwargs.get('Xi')
        Yi = kwargs.get('Yi')
        s = "Test the number of iteration"
        Para = leastsq(self._error, p0, args=(Xi, Yi, s))

        return Para


if __name__ == '__main__':
    estimateLeastObj = estimateLeastSquare()
    p0 = [1,2]
    Xi = numpy.array([2003, 2004, 2008, 2010, 2014])
    Yi = numpy.array([33.5, 33.1, 35.4, 34.7, 35.8])
    para = estimateLeastObj.function(p0=p0, Xi=Xi, Yi=Yi)
    print(para)
