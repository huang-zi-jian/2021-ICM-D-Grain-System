'''
author: feifei
date: 2021-2-6
file info: DataFrame数据的除法处理
'''
import pandas


def dataFrameDivision(NumeratorPath, denominatorPath, savePath):
    Numerator_data = pandas.read_csv(NumeratorPath, encoding='gbk', index_col=0)
    denominator_data = pandas.read_csv(denominatorPath, encoding='gbk', index_col=0)

    '''
    Numerator_data['st'] = Numerator_data.index
    Numerator_data['st'] = Numerator_data['st'].astype('category')
    l = ['孟加拉国', '中国', '印度', '印度尼西亚', '以色列', '泰国', '英国', '德国', '法国',
         '俄罗斯', '乌克兰', '加拿大', '美国', '阿根廷', '巴西', '墨西哥', '澳大利亚', '新西兰'
         ]
    Numerator_data['st'].cat.reorder_categories(l, inplace=True)
    Numerator_data.sort_values('st', inplace=True)
    Numerator_data.set_index(['st'], inplace=True)

    denominator_data['st'] = denominator_data.index
    denominator_data['st'] = denominator_data['st'].astype('category')
    l = ['孟加拉国', '中国', '印度', '印度尼西亚', '以色列', '泰国', '英国', '德国', '法国',
         '俄罗斯', '乌克兰', '加拿大', '美国', '阿根廷', '巴西', '墨西哥', '澳大利亚', '新西兰'
         ]
    denominator_data['st'].cat.reorder_categories(l, inplace=True)
    denominator_data.sort_values('st', inplace=True)
    denominator_data.set_index(['st'], inplace=True)
    '''

    # 这里循环设置的是从2002-2027的循环模式
    for i in range(0,26):
        a = Numerator_data.iloc[:, i]
        b = denominator_data.iloc[:, i]
        column = a / b
        # print(column)
        Numerator_data[str(2002 + i)] = column
        # print([2,4,6,8]/[2,4,6,8])

    Numerator_data.to_csv(savePath, encoding='gbk')


if __name__ == '__main__':
    dataFrameDivision(NumeratorPath='Data/dealData/AGR.csv',
                      denominatorPath='Data/dealData/GDP.csv',
                      savePath='Data/efficiency/i.csv')