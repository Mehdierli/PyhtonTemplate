# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 11:23:37 2019

@author: miaom
"""
#
# read file 
#
fin = open('read.txt')
line = fin.readline()
print(line) #line end with \n
word = line.strip()
print(word)

files_readed = []
fin = open('read.txt')
for line in fin:
    words = line.strip()
    print(words)
    files_readed.append(words)
    
    
#
# write file
#

fout = open('write.txt', 'w')
line1 = "secret of flame soul and young fate."
fout.write(line1+'\n')
fout.close()

def write_file(file_name, write_data_list):
    fout = open(file_name, 'w')
    for line in write_data_list:
        fout.write(line.strip()+'\n')
    fout.close()
write_file('write.txt', files_readed)


#
# file, directory path
#
import os
cwd = os.getcwd()
def print_filename_under(dirname):
    for sub_name in os.listdir(dirname):
        sub_path = os.path.join(dirname, sub_name)
        if os.path.isfile(sub_path):
            print(sub_path)
        else:
            print_filename_under(sub_path)

def print_dirname_under(dirname):
    for sub_dir in os.listdir(dirname):
        sub_path = os.path.join(dirname,sub_dir)
        if os.path.isdir(sub_path):
            print(sub_path)
            print_dirname_under(sub_path)

print_filename_under('E:\\PythonProject')    
print_dirname_under('E:\\PythonProject')       
            
            
            
            
            