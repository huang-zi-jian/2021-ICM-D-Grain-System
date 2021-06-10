'''
author: feifei
date: 2021-2-7
file info: 对结果进行国家排序并且用数字1填充没有数据的国家信息
'''
import pandas
from 基于python的美赛数据采集.fillData import getFileNames


def deficientionData(filename):

    deficientData = pandas.read_csv('Data/dealData/' + filename, encoding='gbk', index_col=0)

    l = ['孟加拉国', '中国', '印度', '印度尼西亚', '以色列', '泰国', '英国', '德国', '法国',
         '俄罗斯', '乌克兰', '加拿大', '美国', '阿根廷', '巴西', '墨西哥', '澳大利亚', '新西兰'
         ]
    # 将CSV文件中已有的国家指标删除保留没有的
    for i in deficientData.index:
        l.remove(i)

    for index in l:
        appendData = [1 for i in range(2002, 2028)]
        deficientData.loc[index] = appendData

    # 每次循环都要重新设置临时index，否则就会出现index索引名称和column属性名相同的报错
    deficientData['country'] = deficientData.index
    deficientData['country'] = deficientData['country'].astype('category')
    country = ['孟加拉国', '中国', '印度', '印度尼西亚', '以色列', '泰国', '英国', '德国', '法国',
               '俄罗斯', '乌克兰', '加拿大', '美国', '阿根廷', '巴西', '墨西哥', '澳大利亚', '新西兰'
               ]
    deficientData['country'].cat.reorder_categories(country, inplace=True)
    deficientData.sort_values('country', inplace=True)
    deficientData.set_index(['country'], inplace=True)

    deficientData.to_csv('Data/dealData/' + filename, encoding='gbk')


if __name__ == '__main__':

    # filenames = getFileNames('D:\Python项目\python爬虫\美赛数据采集\Data\dealData')
    # for filename in filenames:
    #     deficientionData(filename)
    deficientionData('innutritionIncidence.csv')