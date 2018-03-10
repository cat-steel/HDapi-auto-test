# utf-8
from common import public
import test_inserthouse,test_updatehouse
import time
from pychartdir import *
#从公共函数调用excel的写入方法
worksheet,workbook = public.write_report()

#测试用例的执行，并且返回x:成功的数量，y：失败的数量
xu,yu = test_inserthouse.test_inserthouses(worksheet,workbook)
x,y = test_updatehouse.test_updatehouses(worksheet,workbook)
#得到成功与失败的总数量
xr = x+xu
yr = y+yu
#将成功与失败的数量写入的excel的固定表格中
worksheet.write(2,12,xr)
worksheet.write(2,13,yr)
#获取当前的时间并以制定的格式返回
now = time.strftime('%Y-%m-%d %H_%M_%S')
#测试报告输出的地址
report_dir = 'D:\\person\\learn\\py\\HDapi\\report\\'
#拼接出测试报告名
filename =report_dir + now + 'apiresult.xlsx'
workbook.save(filename)

#通过pychart库实现图形处理，生成测试报告总览图----具体的参数设计可以参考pychart库的文档
data = [yr, xr]
labels = ["faild", "pass"]
c = PieChart(280, 240)
c.setPieSize(140, 130, 80)
c.addTitle("api_result")
c.set3D()
c.setData(data, labels)
c.setExplode(0)
c.makeChart(report_dir+now+"apiresult.png")
