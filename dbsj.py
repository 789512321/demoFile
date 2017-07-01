#!/usr/bin/python
#coding=utf-8

"""
shixin
"""

rows_user = input("rows:");
for i in range(1,rows_user*2+1):
    if i%2 == 0 :
        row_null = rows_user-i/2;
        print " " * row_null, " * " * (i/2), " " * row_null;

"""
kongxin
"""

for a in range(1,rows_user*2+1):
    if a%2 == 0:
        row2_null = rows_user-a/2;
        if a/2 > 2 :
            row3_null = a/2-2;
        else:
            row3_null = 0;
        if a != rows_user*2 and a !=2 :
            print " " * row2_null, " * ", "   " * row3_null, " * ", " " * row2_null;
        elif a == rows_user*2:
            print " " * row2_null," * " * (a/2), " " * row2_null;
        else:
            print " " * row2_null, " * "," " * row2_null;