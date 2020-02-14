# Python-Study
#!/usr/bin/python
import xlrd
data=xlrd.open_workbook('read.xlsx')
st=data.sheets()[0]
rows=st.nrows

t=open("0.txt","w")
for i in range(rows):
	t.write(str(st.row_values(i))+'\n')
	
t.close()
