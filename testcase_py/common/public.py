import os,xlrd,xlwt,time

def get_url(api_name):
	fp = open('D:\person\learn\py\HDapi\config\API_url.txt')
	api_infos = fp.readlines()
	fp.close()
	api_urls = []
	for api in api_infos:
		api_f = api.strip(' \r\n\t')
		api_c = api_f.split('=')
		if api_name == api_c[0]:
			return api_c[1]

def get_case(filename,sheetnum):
	case_dir='D:\\person\\learn\\py\\HDapi\\testcase_excel' + '\\' + filename + '.xlsx'

	datas = xlrd.open_workbook(case_dir)
	table = datas.sheets()[sheetnum]
	nor = table.nrows
	nol = table.ncols
	return nor,table

def write_report():
	workbook = xlwt.Workbook(encoding='utf-8')
	worksheet = workbook.add_sheet('housemanage')
	alignment = xlwt.Alignment()
	alignment.horz = alignment.HORZ_CENTER
	alignment.vert = alignment.VERT_CENTER
	style = xlwt.XFStyle()
	style.alignment = alignment

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
	return worksheet,workbook

