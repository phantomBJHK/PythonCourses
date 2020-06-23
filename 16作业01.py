def testdecode(testcode):
    strout = testcode.decode('GBK')
    return strout
strtest = b'\xe5\x93\x88\xe5\x96\xbd\xef\xbc\x8c\xe5\xa4\xa7\xe5\xae\xb6\xe5\xa5\xbd'
print(testdecode(strtest))

with open('mytest16.txt', 'a') as r:
    r.write(testdecode(strtest))


