#coding:utf-8

def compoundInterest(amount,rate,time):
    for i in range(1,time+1):
        amount += rate * amount
        print ('year{}:{}'.format(i,amount))
compoundInterest(100,0.05,8)
