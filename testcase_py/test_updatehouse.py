import requests,unittest,os,time,json
from common import public,get_authorization


def test_updatehouses(worksheet,workbook):
	nor,table = public.get_case('house',4)
	Authorization = get_authorization.get_Authorization()
	url = public.get_url('updatehouse')
	a = 2
	x = 0
	y = 0
	for i in range(1,nor):
		houseNum = table.cell_value(i,0)
		orgUuid = table.cell_value(i,1)
		uuid = table.cell_value(i,2)
		houseUseFor = table.cell_value(i,3)
		residentNum = table.cell_value(i,4)
		emergencyPhone = table.cell_value(i,5)
		expect_code = table.cell_value(i,6)
		expect_message = table.cell_value(i,7)
		notes = table.cell_value(i,8)
		floor = table.cell_value(i,9)
		payment = table.cell_value(i,11)
		data = {
		'houseNum':houseNum,
		'houseUseFor':houseUseFor,
		'orgUuid':orgUuid,
		'floor':floor,
		'residentNum':residentNum,
		'uuid':uuid,
		'emergencyPhone':emergencyPhone,
		'payment':payment
		}

		headers={
		'Accept':'application/json',
		'Content-Type':'application/json',
		'Authorization':Authorization
		}

		a+=1
		worksheet.write(3,a,notes)

		data = json.dumps(data)

		r = requests.post(url,data=data,headers=headers)
		b = eval(r.text)
		m = b.get('code')
		n = b.get('message')
		k = b.get('data')
		if m==expect_code and n==expect_message:
			worksheet.write(4,a,'pass')
			x += 1
		else:
			worksheet.write(4,a,'faild:%s'%k)
			y += 1
	return x,y

