#coding:utf-8

class select(object):
    CN_mobile = [134, 135, 136, 137, 138, 139, 150, 151, 152, 157, 158, 159, 182, 183, 184, 187, 188, 147, 178, 1705]
    CN_union = [130, 131, 132, 155, 156, 185, 186, 145, 176, 1709]
    CN_telecom = [133, 153, 180, 181, 189, 177, 1700]
    def __init__(self):
        pass
    def adjust(self):
        self.phone = input('tell me your phone,please:')
        self.isEleven()
        return self.isComm()

    def isEleven(self):
        if len(self.phone) == 11:
            self.phone = int(self.phone)
        else:
            print('len is wrong!')
            self.adjust()
            pass

    def isComm(self):
        if int(self.phone//10**8) == 170:
            if int(self.phone//10**8%10)==5:
                pass
            elif int(self.phone//10**8%10)==9:
                pass
            elif int(self.phone//10**8%10)==0:
                pass
            else:
                print('Congratulation!you has successd give me a kid!')
        elif int(self.phone//10**8) in self.CN_mobile:
            return 'China_Mobile',self.phone
        elif int(self.phone//10**8) in self.CN_union:
            return 'China_Union',self.phone
        elif int(self.phone//10**8) in self.CN_telecom:
            return 'China_Telecom',self.phone
        else:
            print('Are you kiding me?')
            self.adjust()
            pass


if __name__ == '__main__':
    run_pro = select()
    comm,run = run_pro.adjust()
    print('Operator:{}'.format(comm))
    print('We are testing for you phone{}.'.format(run))
