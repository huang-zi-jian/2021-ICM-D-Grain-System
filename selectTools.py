'''
author: feifei
date: 2021-2-6
file info: 数据的函数处理
'''

import pandas

# 选取DataFrame数据中指定下标index，并存放到新的文件中
def selectData(filepath, start, end, savepath):
    '''

    :param filepath: 读取文件的地址
    :param start: CSV文件读取数据的起始index
    :param end: CSV文件读取数据的终止index
    :param savepath: 提取数据的文件存储地址
    :return:
    '''
    data = pandas.read_csv(filepath,encoding='gbk',index_col=0)
    result = data.iloc[start:end,:]

    result.to_csv(savepath,encoding='gbk',index=False)
    # data = data.groupby(by=['country']).sum()
    # data.to_csv('foodAll.csv',encoding='gbk')

    print(result)


# 将统一类别下标的数据按照国家分组并对组进行加和
def dataGroupbyCountry(filepath, savepath):
    '''

    :param filepath: 读取文件的地址
    :param savepath: 提取数据的文件存储地址
    :return:
    '''
    data = pandas.read_csv(filepath,encoding='gbk',index_col=0)

    result = data.groupby(by=['country']).sum()
    result.to_csv(savepath,encoding='gbk')

    print(result)


if __name__ == '__main__':
    # selectData('output.csv', 0, 18, 'Data/urbanPopulation.csv')
    # selectData('output.csv', 18, 36, 'Data/countryArea.csv')
    selectData('output.csv', 0, 5, 'Data/Urbanization.csv')
    # selectData('output.csv', 31, 45, 'Data/agricultureProductivity.csv')
    # dataGroupbyCountry('output.csv', 'Data/foodOfAgriculture.csv')