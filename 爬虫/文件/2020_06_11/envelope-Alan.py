import time
import random


class wallet:

    def __init__(self):
        self.envelope_z = {}
        self.envelopeAmount = 0
        self.envelopeNumber = 0
        self.minnum = 0.1
        self.time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # print(self.time)

    def Getparameters(self):
        self.envelopeNumber = int(input('请输入红包个数：'))
        self.envelopeAmount = float(input('请输入红包金额：'))
        while True:
            if self.envelopeAmount / self.envelopeNumber < self.minnum:
                print('每个红包的最小金额为:%.2f' % self.minnum)
                self.envelopeAmount = float(input('请重新输入红包金额：'))
            else:
                print('准备就绪【%d个红包,共%.2f元】' % (self.envelopeNumber, self.envelopeAmount))
                break

    def generate(self):
        self.envelope = {}
        self.Getparameters()
        Number = self.envelopeNumber
        minnum = self.minnum * 100
        maxmum1 = self.envelopeAmount * 100
        average = self.envelopeAmount * 100 / self.envelopeNumber
        if self.envelopeAmount / self.minnum == self.envelopeNumber:
            for i in range(self.envelopeNumber):
                Single = self.minnum
                self.envelope[str(i + 1)] = self.minnum
                # print('第%d个红包为%.2f元' % (i + 1, Single))
        else:
            for i in range(self.envelopeNumber):
                Number = Number - 1
                if Number == 0:
                    Single = maxmum1 / 100
                    self.envelope[str(i + 1)] = Single
                else:
                    maxmum2 = int(maxmum1 - Number * minnum)
                    if maxmum2 > average * 2:
                        Single = random.randint(minnum, average * 2)
                    else:
                        Single = random.randint(minnum, maxmum2)
                    maxmum1 -= Single
                    Single /= 100
                    self.envelope[str(i + 1)] = Single
                # print('第%d个红包为%.2f元' % (i + 1, Single))
        # print('已生成成功')
        # print(self.envelope)
        self.time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.envelope_z['envelopeAmount'] = self.envelopeAmount
        self.envelope_z['envelopeNumber'] = self.envelopeNumber
        self.envelope_z['time'] = self.time
        self.envelope_z['data'] = self.envelope
        return self.envelope_z


envelope_z = {}
Start = wallet()
envelope = Start.generate()
envelope_z[str(len(envelope_z) + 1)] = envelope
print(envelope_z)