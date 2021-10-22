"""
@version:
@author: DQ
@time: 2021-10-21
@file: binclass.py
@function: 
@modify: 
"""

import math


def cal_func(x):
    """
    计算：f(x) = x + 10sin5x + 7cos4x
    """
    f = x + 10 * math.sin(5 * x) + 7 * math.cos(4 * x)
    return f


def dec2bin(dec):
    """
    将[0,9]范围的十进制数转为17位二进制数字符串
    """
    num = int(dec / 0.0001)
    b = bin(num)
    return f'{b[2:]:0>17}'


def bin2dec(bin_str):
    """
    将17位二进制数字符串转为[0,9]范围的十进制数
    """
    v = 0
    for i in range(17):
        if bin_str[i] == '1':
            v += 2 ** (16 - i)

    return v * 0.0001


class BinNum():
    """
    专用于本Demo中的求解。
    十进制0对应二进制的17'b0 0000 0000 0000 0000
    二进制1'b1代表十进制0.0001
    """

    bin_str = None  # 二进制表示，17位字符串
    decimal_num = None  # 十进制，数值
    f_value = None  # 函数值

    def __init__(self, dec_bin, if_dec=True):
        """
        两种初始化方式，dec or bin
        dec小数点后最多4位，取值范围为[0,9]
        bin为17位字符串
        """
        if if_dec:
            self.decimal_num = dec_bin
            self.bin_str = dec2bin(dec_bin)
        else:
            self.bin_str = dec_bin
            self.decimal_num = bin2dec(dec_bin)

        self.f_value = cal_func(self.decimal_num)

    def compare(self, binnum):
        """
        找出两个二进制数的不同项序号
        """
        res = []

        for i in range(17):
            if self.bin_str[i] != binnum.bin_str[i]:
                res.append(i)

        return res
