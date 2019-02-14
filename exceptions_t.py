# -*- coding: utf-8 -*-

def print_content_byline(read_filename):
    try:
        fin = open(read_filename)
        for line in fin:
            print(line.strip())
        print("\nRead %s files done."%read_filename)
    except:
        print("Function print_content_byline, error happened.\n")
        
print_content_byline("Notexist.file")
print_content_byline('read.txt')