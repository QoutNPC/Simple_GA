"""
@version:
@author: DQ
@time: 2021-10-21
@file: calclass.py
@function: 
@modify: 
"""

import random
from . import binclass


class GA():
    __obj = None  # 单态
    chromo_list = None
    __to_end = None

    def __new__(cls, *args, **kwargs):
        if not cls.__obj:
            cls.__obj = object.__new__(cls)
        return cls.__obj

    def __init__(self):
        """
        初始产生100个染色体
        """
        self.__to_end = False
        seq = random.sample(range(90001), 100)

        self.chromo_list = []
        for i in seq:
            self.chromo_list.append(binclass.BinNum(i / 10000))

        # 按照函数值从高到低排序
        self.chromo_list.sort(key=lambda binnum: binnum.f_value, reverse=True)

    def if_finished(self):
        return self.__to_end

    def __str__(self):
        res = f'函数值为：{self.chromo_list[0].f_value}，此时x为：{self.chromo_list[0].decimal_num}'
        return res

    def one_turn(self, p_crossover, p_mutation):
        """
        只从前20%中选择染色体遗传
        交叉概率，变异概率
        """
        newchromo_list = []
        for i in range(100):
            x, y = random.sample(range(20), 2)  # 20 = 100 * 20%
            diff_bits = self.chromo_list[x].compare(self.chromo_list[y])

            vbin_str = self.chromo_list[x].bin_str
            for c in diff_bits:
                if random.random() < p_crossover:
                    if vbin_str[c] == '1':
                        vs = vbin_str[0:c] + '0' + vbin_str[c + 1:]
                        if binclass.bin2dec(vs) <= 9:
                            vbin_str = vs
                    else:
                        vs = vbin_str[0:c] + '1' + vbin_str[c + 1:]
                        if binclass.bin2dec(vs) <= 9:
                            vbin_str = vs

            for m in range(17):
                if random.random() < p_mutation:
                    if vbin_str[m] == '1':
                        vs = vbin_str[0:m] + '0' + vbin_str[m + 1:]
                        if binclass.bin2dec(vs) <= 9:
                            vbin_str = vs
                    else:
                        vs = vbin_str[0:m] + '1' + vbin_str[m + 1:]
                        if binclass.bin2dec(vs) <= 9:
                            vbin_str = vs

            newchromo_list.append(binclass.BinNum(vbin_str, False))

        # 按照函数值从高到低排序
        newchromo_list.sort(key=lambda binnum: binnum.f_value, reverse=True)

        # 子代前5均值小于上一代，则停止进化
        s1 = 0
        s2 = 0
        for i in range(5):
            s1 += newchromo_list[i].f_value
            s2 += self.chromo_list[i].f_value

        if s1 <= s2:
            self.__to_end = True
        else:
            self.chromo_list = newchromo_list
