import random



class RandomDice(object):
    key_num = 0

    def create(self):
        self.key_num=0
        for i in range(3):
            value = random.randrange(1, 7)
            self.key_num += value
            print(str(value) + '=======' + str(self.key_num))
        return self.key_num
