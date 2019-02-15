# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 14:00:35 2019

@author: miaom
"""

"""
__name__ :
    a built-in variable that is set when the program starts.

If the program is running as a script, 
__name__ has the value '__main__'
Otherwise :
if the module is being imported, 
the test code is skipped.
"""

def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count

if __name__ == '__main__':
    print(linecount('module_t.py'))
