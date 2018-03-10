import os,xlrd,xlwt,time

#通过配置文件里的接口名称来获取接口url的函数
def get_url(api_name):
	fp = open('D:\person\learn\py\HDapi\config\API_url.txt')
#按行读取接口url配置文件
	api_infos = fp.readlines()
	fp.close()
#通过for循环来遍历配置文件里的每一个url，并且返回传入的接口名称相应的url
	for api in api_infos:
#去除因为读取产生的换行空格等
		api_f = api.strip(' \r\n\t')
		api_c = api_f.split('=')
		if api_name == api_c[0]:
			return api_c[1]

#通过传入用例名称的文件和excel页面来读取测试用例
def get_case(filename,sheetnum):
	case_dir='D:\\person\\learn\\py\\HDapi\\testcase_excel' + '\\' + filename + '.xlsx'

	datas = xlrd.open_workbook(case_dir)
	table = datas.sheets()[sheetnum]
	nor = table.nrows
	nol = table.ncols
	return nor,table

#通过xlwt库来设计测试报告并写入excel里面
def write_report():
	workbook = xlwt.Workbook(encoding='utf-8')
#在excel测试报告表格中创建名叫housemanage的页面
	worksheet = workbook.add_sheet('housemanage')
#设置字体格式为居中对齐
	alignment = xlwt.Alignment()
	alignment.horz = alignment.HORZ_CENTER
	alignment.vert = alignment.VERT_CENTER
	style = xlwt.XFStyle()
	style.alignment = alignment
	
#具体的合并哪些单元格并且写入相应的信息
	worksheet.write_merge(0,0,0,7,'测试报告(housemanage)',style)
	worksheet.write_merge(1,10,0,0,'house_manage',style)
	worksheet.write_merge(1,2,1,1,'insethouse',style)
	worksheet.write_merge(3,4,1,1,'updatehouse',style)
	worksheet.write_merge(5,6,1,1,'deletehouse',style)
	worksheet.write_merge(7,8,1,1,'gethouse',style)
	worksheet.write_merge(9,10,1,1,'updatehouse',style)
	worksheet.write_merge(1,2,11,11,'total_result',style)
	worksheet.write(1,2,'notes')
	worksheet.write(2,2,'detail')
	worksheet.write(3,2,'notes')
	worksheet.write(4,2,'detail')
	worksheet.write(5,2,'notes')
	worksheet.write(6,2,'detail')
	worksheet.write(7,2,'notes')
	worksheet.write(8,2,'detail')
	worksheet.write(9,2,'notes')
	worksheet.write(10,2,'detail')
	worksheet.write(1,12,'pass')
	worksheet.write(1,13,'faild')
#最后返回worksheet,workbook两个参数，因为在测试测试用例和运行文件中需要用到的两个参数
	return worksheet,workbook

