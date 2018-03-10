#从配置文件获取访问权限信息
def get_Authorization():
	fp = open('D:\person\learn\py\HDapi\config\Authorization.txt')
	info = fp.read()
	fp.close()
	return info
