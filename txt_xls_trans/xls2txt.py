#!/usr/bin/env python
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import xlrd

def xls2txt(xls_file, txt_file):
    fname = xls_file    #命令行参数 ,取第一个参数

    # print  fname
    bk = xlrd.open_workbook(fname)
    #工作簿中所有sheet的名称
    #print bk.sheet_names()
    #shxrange = range(bk.nsheets) 
        
    fo = open(txt_file, 'wb')

    #循环获取每个sheet中的数据
    sheetnames = bk.sheet_names()
    for m in sheetnames:
        sh = bk.sheet_by_name(m)
        #获取行数
        nrows = sh.nrows
        #获取列数
        ncols = sh.ncols     #此行可注释掉
        #print "nrows %d, ncols %d" % (nrows,ncols)
        row_list = []
        #获取各行数据
        for i in range(nrows):
            row_data = sh.row_values(i)
            line = ""
            for j in range(len(row_data)):
                if j == 0:
                    line = str(row_data[j])
                else:
                    line = line + "\t" + str(row_data[j])
            fo.write(line + "\n")  #输出每行后换行
        fo.close()
	
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Usage: xls2txt xls_file output_txt_file"
        exit(1)
    xls_file = sys.argv[1]
    txt_file = sys.argv[2]
    xls2txt(xls_file, txt_file)
