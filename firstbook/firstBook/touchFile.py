#coding:utf-8

def mkdir(numFile):
    for i in range(numFile):
        fileOp = open('{}.txt'.format(i),'w')
        fileOp.close()
mkdir(10)
