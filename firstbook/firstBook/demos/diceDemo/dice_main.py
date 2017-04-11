#coding:utf-8
from pyclbr import Class

from dbus.service import Object

from diceDemo import compare_two
from diceDemo import random_dice


class game_begin(object):
    def __init__(self):
        self.random_ = random_dice.RandomDice()
        self.compare = compare_two.CompareTwo()

    def game_run(self,num_input):
        key = self.random_.create()
        big_lit = key > 10
        result = self.compare.compare(num_input,big_lit)
        return result


if __name__ == '__main__':
    begin = game_begin()
    while True:
        num_input = input('Enter 1 for big.Or 0 for less:')
        result = begin.game_run(num_input)
        if result == True:
            print('You won!')
        else:
            print('You loss!')

