#document_1602.txt的地址，直接粘贴即可
#from kkb_tools import open_file
#书写你的代码

myfile = open(r'document_1602.txt','a')
while True:
	new_content = input('请输入内容太，Q退出：')
	if new_content == 'Q':
		break
	else:
		myfile.write(new_content)

myfile.close()

#open_file("document_1602.txt")