balance=int(input("请输入卡片余额："))
if balance < 5:
    print("余额不足请及时充值，不能乘车")
elif 5 <= balance <= 15:
    print(balance)
else:
    print("余额充足，请放心乘车")
    