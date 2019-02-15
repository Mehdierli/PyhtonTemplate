# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 13:45:02 2019

@author: miaom
"""
import os
cmd = "ls -l"
fp = os.popen(cmd)
res = fp.read()
print(res)
stat = fp.close()
print(stat)

filename = 'read.txt'
cmd = 'md5sum '+filename
fp = os.popen(cmd)
res = fp.read()
stat = fp.close()