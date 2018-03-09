# utf-8
from common import public
import test_inserthouse,test_updatehouse
import time
from pychartdir import *

worksheet,workbook = public.write_report()

xu,yu = test_inserthouse.test_inserthouses(worksheet,workbook)
x,y = test_updatehouse.test_updatehouses(worksheet,workbook)
xr = x+xu
yr = y+yu
worksheet.write(2,12,xr)
worksheet.write(2,13,yr)
now = time.strftime('%Y-%m-%d %H_%M_%S')
report_dir = 'D:\\person\\learn\\py\\HDapi\\report\\'
filename =report_dir + now + 'apiresult.xlsx'
workbook.save(filename)

data = [yr, xr]
labels = ["faild", "pass"]
c = PieChart(280, 240)
c.setPieSize(140, 130, 80)
c.addTitle("api_result")
#c.set3D()
c.setData(data, labels)
c.setExplode(0)
c.makeChart(report_dir+now+"apiresult.png")