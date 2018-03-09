import requests,unittest,os,time,json
from common import public,get_authorization



def test_inserthouses(worksheet,workbook):
	url = public.get_url('inserthouse')
	nor,table = public.get_case('house',0)
	Authorization = get_authorization.get_Authorization()
	a = 2
	xu = 0
	yu = 0
	for i in range(1,nor):
		houseNum = table.cell_value(i,0)
		orgUuid = table.cell_value(i,1)
		floor = table.cell_value(i,2)
		houseUseFor = table.cell_value(i,3)
		residentNum = table.cell_value(i,4)
		emergencyPhone = table.cell_value(i,5)
		expect_code = table.cell_value(i,6)
		expect_message = table.cell_value(i,7)
		notes = table.cell_value(i,8)
		payment = table.cell_value(i,11)
		data = {
		'houseNum':houseNum,
		'houseUseFor':houseUseFor,
		'orgUuid':orgUuid,
		'residentNum':residentNum,
		'floor':floor,
		'emergencyPhone':emergencyPhone,
		'payment':payment
		}

		headers={
		'Accept':'application/json',
		'Content-Type':'application/json',
		'Authorization':Authorization
		}
		a+=1
		worksheet.write(1,a,notes)

		data = json.dumps(data)

		r = requests.post(url,data=data,headers=headers)
		b = eval(r.text)
		m = b.get('code')
		n = b.get('message')
		k = b.get('data')
		if m==expect_code and n==expect_message:
			worksheet.write(2,a,'pass')
			xu += 1
		else:
			worksheet.write(2,a,'faild')
			yu += 1
	return xu,yu
#	now = time.strftime('%Y-%m-%d %H_%M_%S')
#	report_dir = 'D:\\person\\learn\\py\\HDapi\\report\\'
#	filename =report_dir + now + 'apiresult.xlsx'
#	workbook.save(filename)
