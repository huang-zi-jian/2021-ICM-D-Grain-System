'''
author: feifei
date: 2021-2-5
file info: 网络抓取EPS农业数据包
'''


import requests
import json
import pandas
import numpy


# 处理YNames中的分隔符
def split(listData):
    normkey = []
    country = []
    for stringData in listData:
        temp = stringData.split(sep='-', maxsplit=1)
        normkey.append(temp[0])
        country.append(temp[1])

    return normkey, country


# 爬取ajax请求的数据并将提取出来的数据存入Excel文件中
def spiderAjax(url, data):
    url = url
    s = requests.session()
    data = data
    headers = {
        'Host': 'olap.epsnet.com.cn',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'http://olap.epsnet.com.cn',
        'Referer': 'http://olap.epsnet.com.cn/auth/platform.html?sid=9ABDB25601EC9674BB5E0F4572FF04AB_ipv499219786&cubeId=1190',

        'Cookie': 'UM_distinctid=17684c448b557-0c9b09ac0fda6a-c791039-144000-17684c448b67a; JSESSIONID=AFF176D0ED237F1188C40E3F87AB5671; sid=9ABDB25601EC9674BB5E0F4572FF04AB_ipv499219786'
    }
    reponse = requests.post(url=url, data=json.dumps(data), headers=headers)

    # print(reponse.text)
    # 将字符串数据加载为json数据
    result = json.loads(reponse.text)
    # print(result)
    # 返回数据和x、y坐标
    datas = result['datas']
    xNames = result['xNames']
    yNames = result['yNames']

    # 对请求到的数据进行处理并存入Excel文件
    normkey, country = split(listData=yNames)
    agricultureData = pandas.DataFrame(data=datas, columns=xNames, index=normkey)

    # 逐列插入数据用insert，切记column不能用list列表
    agricultureData.insert(loc=0, column='country', value=country)
    # agricultureData['country'] = country
    agricultureData.to_csv('output.csv',encoding='gbk')

    '''
    # CSV文件导出为Excel文件
    excelWriter = pandas.ExcelWriter('output.xlsx')
    agricultureData.to_excel(excel_writer=excelWriter, sheet_name='Sheet1')
    excelWriter.save()    
    '''

    print('success!')
    # return datas, xNames, yNames



if __name__ == '__main__':

    url = 'http://olap.epsnet.com.cn/draw/charts.do?0.5239636357807531&sid=5F8AA0C0BB4EA3336998675E6595FD59_ipv429267941'
    data = {
        'sheetId': "1612710254000s3.3943426403410504",
        'indexs': '1,2,3,4,5',
        'yindexs': "2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18"
    }
    spiderAjax(url=url, data=data)