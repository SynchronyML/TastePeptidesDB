#-*- codeing = utf-8 -*-
#@Time: 2021/10/23 10:57
#@Author : 范范
#@File : aaa.py
#@Software: PyCharm



#    http://camt.pythonanywhere.com/iUmami-SCM


import requests
import re
import csv
import xlwt
url = "http://pmlab.pythonanywhere.com/bitterbertpredict"
files = {'file': open('C:\\Users\\Alex\\Desktop\\00-分子模拟自己写的教参\\0_Tastepeptidesdb\\Umami_YYDS\\模型评价\\BERTBitter-范大哥的爬虫\\tect.csv', 'rb')}  #路径要修改
def data_submit(f):
    r = requests.post(url, files=f)
    # print(r.text)
    s = re.findall('Test is (.*?)\(',r.text)
    # print('s=',s)
    r.close()
    return s

workbook=xlwt.Workbook(encoding='utf-8')
sheet1=workbook.add_sheet('sheet1')
# f2=open('result.xlsx',mode='r')
f1=open('C:\\Users\\Alex\\Desktop\\00-分子模拟自己写的教参\\0_Tastepeptidesdb\\Umami_YYDS\\模型评价\\BERTBitter-范大哥的爬虫\\wait_r.csv','rt')    #路径要修改
list=[]
reader = csv.reader(f1)
for row in reader:
    list.append(row[0])
# print(len(list))
b=[]
for i in data_submit(files):
    b.append(i)
print(len(b))
for i in range(437):    #数据长度
    for j in range(2):
        if j%2==0:
            sheet1.write(i,j,'{}'.format(list[i]))
        else:
            sheet1.write(i, j,'{}'.format( b[i]))
workbook.save('reslut_new.xls')

f1.close()
print('over!')

