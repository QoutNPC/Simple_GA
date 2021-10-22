"""
@version:
@author: DQ
@time: 2021-10-21
@file: __init__.py
@function: 
@modify: 
"""

import os

res = os.listdir('./packages')
newres = []
for i in res:
    if i[0:2] != '__':
        s = i[0:-3]
        newres.append(s)

__all__ = newres
