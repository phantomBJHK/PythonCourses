def testdecode(testcode):
    strout = testcode.decode('utf-8')
    return strout

def testencode(teststr):
    codeout = teststr.encode('utf-8')
    return codeout

strtest = '哈喽，小伙伴们，大家好，今后我们一定要好好学习哦'

with open(r'mytest16.txt', 'wb') as r:
    a = r.write(testencode(strtest))
    print(a)

    
with open(r'mytest16.txt', 'rb') as file:
    a = testdecode(file.read())
    print(a)

