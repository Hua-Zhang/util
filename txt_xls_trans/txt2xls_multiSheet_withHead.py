#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import sys
import datetime
import time
import os
import xlwt #需要的模块

head_line = "time_day" + "\t" + "time_hour" + "\t" + "devId" + "\t" + "passport" + "\t" + "docid" + "\t" + "platform" + "\t" + "channel" + "\t" + "info"

def txt2xls(filename, xlsname):  #文本转换成xls函数，filename 表示一个要被转换的txt文本，xlsname 表示转换后的文件名
    print ('converting xls ... ')
    f = open(filename)   #打开txt文本进行读取
    x = 0                #在excel开始写的位置（y）
    y = 0                #在excel开始写的位置（x）
    xls=xlwt.Workbook()
    sheet = xls.add_sheet('sheet1', cell_overwrite_ok=True) #生成excel的方法，声明excel
    sheet_n = 1
    line_n = 0
    for i in head_line.split('\t'):#写入表头
        item=i.strip()
        sheet.write(x,y,item)
        y += 1 #另起一列
    x += 1 #另起一行
    y = 0  #初始成第一列
    while True:  #循环，读取文本里面的所有内容
        line = f.readline() #一行一行读取
        if not line:  #如果没有内容，则退出循环
            break
        if line_n == 50000:
            sheet_n += 1
            sheet_name = "sheet" + str(sheet_n)
            sheet = xls.add_sheet(sheet_name, cell_overwrite_ok=True)
            x = 0
            y = 0
            line_n = 0
            for i in head_line.split('\t'):#写入表头
                item=i.strip()
                sheet.write(x,y,item)
                y += 1 #另起一列
            x += 1 #另起一行
            y = 0  #初始成第一列
        line_n += 1
        for i in line.split('\t'):#读取出相应的内容写到x
            item=i.strip()
            sheet.write(x,y,item)
            y += 1 #另起一列
        x += 1 #另起一行
        y = 0  #初始成第一列
    f.close()
    xls.save(xlsname+'.xls') #保存

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print ("Usage: txt2xls text_file output_xls_file")
        exit(1)
    filename = sys.argv[1]
    xlsname  = sys.argv[2]
    txt2xls(filename,xlsname)
