

import CSVCatalog

import time
import json

def t1():
    c_cat=CSVCatalog.CSVCatalog()
    print("catlog=",c_cat)

def t2():
    c_cat=CSVCatalog.CSVCatalog()
    result=c_cat.create_table('people','/Users/mac/Desktop/database/Bonus_Outline/people.csv')
    print("result=",result)

def t3():
    c_cat = CSVCatalog.CSVCatalog()
    result = c_cat.get_table('people')
    print("result=", result)

def t4():
    c_cat = CSVCatalog.CSVCatalog()
    result=c_cat.create_table('Batting','/Users/mac/Desktop/database/Bonus_Outline/Batting.csv')
    print("result=", result)
    result=c_cat.get_table('People')
    print('result=',result)

def t5():
    c_cat = CSVCatalog.CSVCatalog()
    c_def=CSVCatalog.ColumnDefinition('PlayerID','text',True)
    print("c_def", c_def)

def t6():
    c_cat = CSVCatalog.CSVCatalog()
    i_def=CSVCatalog.IndexDefinition('people','Cool','PRIMARY',['PlayerID','teamID','yearID','stint'])

    print("i_def", i_def)

def t7():
    c_cat = CSVCatalog.CSVCatalog()
    t=result=c_cat.get_table('Batting')
    x=t.define_index("Bob",['PlayerID','teamID','yearID','stint'],"PRIMARY")

#t1()
#t2()
#t3()
#t4()
#t5()
t6()
#t7()
