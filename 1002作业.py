while True:             #判断输入是否是数字
    num1 = input('请输入数字：')
    try:
        num1 = float(num1)
        break
    except:
        continue

while True:             #判断输入是否是正确运算符
    symbols = ['+','-','*','/']
    symbol = input('请输入运算符/(+-*/)：')
    if symbol in symbols:
        break

while True:             #判断输入是否是数字
    num2 = input('请输入数字：')
    try:
        num2 = float(num2)
        break
    except:
        continue

def calculator(num1,symbol,num2):
    if symbol == '+':
        result = num1+num2
        return result
    elif symbol == '-':
        result = num1-num2
        return result
    elif symbol == '*':
        result = num1*num2
        return result
    else:
        result = round(num1/num2,2)
        return result

print(calculator(num1,symbol,num2))
