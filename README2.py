#!/usr/bin/env python3
# coding: utf-8
import xlrd

# 打开excel文件
rbook = xlrd.open_workbook('read.xlsx')
rsheet = rbook.sheets()[0]  # 取第一个工作簿
#ncols=rsheet.ncols

t= open("1.txt","w")

for row in rsheet.get_rows():
	write_value=row[2]
	result=str(write_value)
	t.write(result.replace('text:',' ').replace('empty',' ')+'\n')

t.close()
