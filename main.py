"""
@version:
@author: DQ
@time: 2021-10-21
@file: main.py
@function: 
@modify: 
"""

from packages import *


class Main():
    def __init__(self):
        ga = calclass.GA()
        print(ga)

        # 最多迭代100次
        for i in range(100):
            # ga.one_turn(0.5, 0.01)
            if ga.if_finished():
                break
            else:
                ga.one_turn(0.6, 0.01)

        print(f'迭代了{i+1}次')
        print(ga)


if __name__ == '__main__':
    Main()
