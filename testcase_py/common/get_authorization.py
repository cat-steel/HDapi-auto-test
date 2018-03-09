def get_Authorization():
	fp = open('D:\person\learn\py\HDapi\config\Authorization.txt')
	info = fp.read()
	fp.close()
	return info
