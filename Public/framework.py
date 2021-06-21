#coding=utf-8

import requests,xlrd,xlwt,time,hashlib
from xlutils.copy import copy
from ttxn_api.Config.Api_Data import *
def apiRequests(type, url, data, head):
    """get和post请求一起处理函数"""
    if type =='get':
        res = requests.get(url,data,headers=head,timeout=10)
    else:
        res = requests.post(url,data,headers=head,timeout=10)
    return res

def readExcel(filename, sheetname, line):
    """读取excel指定行的数据"""
    book=xlrd.open_workbook(filename)
    sheet=book.sheet_by_name(sheetname)
    data=sheet.row_values(int(line))
    return data

def dateChangeDict(filename, sheetname, line):
    """将参数转化为字典"""
    data=readExcel(filename, sheetname, line)
    dict = {}
    if '=' in  data[5]:
        if '&' in data[5]:
            data_list=data[5].split('&')
            for i in data_list:
                dict[i.split('=')[0]] = i.split('=')[1]
        else:
            dict[data[5].split('=')[0]] = data[5].split('=')[1]
    else:
        pass
    data[5] = dict
    return data

def writExcel(filename, sheetname, line, row, data):
    """写入文件指定的单元格内容,不会清楚其它单元格的数据"""
    file=xlrd.open_workbook(filename,formatting_info=True)  # 打开文件
    wb=copy(file)  # 利用xlutils.copy下的copy函数复制
    ws=wb.get_sheet(sheetname)   # 指定表格的sheet页面
    ws.write(line,row,data)   # 写入数据
    wb.save(filename)  # 保存文件

def fixExcel(filename, sheetname, line, row, data_1, data_2):
    """修改文件指定的单元格内容"""
    data=readExcel(filename, sheetname, line)
    if '&' in data[5]:
        list=data[5].split('&')
    else:
        list=[data[5]]
    value=""
    for i in list:  ##循环读取列表修改其中的值
        if data_1 in i:
            list[list.index(i)]=data_2
    for j in list:  ##循环读取列表进行拼接
        value=value+j+'&'
    value=value.strip('&')
    writExcel(filename, sheetname, line, row, value) ##调用写入表格函数，不清除其它数据


if __name__ == '__main__':

    name=r'F:\automation\ttxn_api\Testdata\data.xls'
    print(dateChangeDict(name, "login", 1))







