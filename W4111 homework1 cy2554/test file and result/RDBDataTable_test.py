from src.RDBDataTable import RDBDataTable
import logging
import os
import json
import pymysql
import src.SQLHelper as SQLHelper


def init_data_table_test(table_name=None, connect_info=None, key_columns='nameLast'):
    """
    :param table_name:
    :param connect_info:
    :param key_columns:
    :return:
    """

    # test case
    table_name = "people"
    connect_info = {"host": 'localhost',
                    "user": 'dbuser',
                    "password": 'dbuserdbuser',
                    "db": 'lahman2019raw',
                    "charset": 'utf8mb4',
                    "cursorclass": pymysql.cursors.DictCursor}
    key_columns = ["nameLast"]

    csv_data_table = RDBDataTable(table_name=table_name, connect_info=connect_info, key_columns=key_columns)
    return csv_data_table
def find_by_template_test(data_table):
    tmp1={'birthYear': '1980','weight':'180'}
    result1=data_table.find_by_template(tmp1)
    tmp2={'nameLast': 'chenxu', 'weight': '10000000'}
    result2 = data_table.find_by_template(tmp2)
    tmp3 = {'nameLast': 'yangcx', 'weight': '1999900'}
    result3 = data_table.find_by_template(tmp3)
    print(result1)
    print(result2)
    print(result3)

def delete_by_template(data_table):
    tmp = {'nameLast': 'chenxu'}
    result = data_table.delete_by_template(tmp)
    print(result)
def delete_by_key(data_table):
    key_fields=['chenxu']
    result=data_table.delete_by_key(key_fields)
def insert(data_table):
    tmp1 = {'playerID':'cy2554','nameLast': 'chenxu', 'weight': '10000000'}
    tmp2 = {'playerID': 'dlzxycx', 'nameLast': 'yang', 'weight': '100000'}
    data_table.insert(tmp1)
    data_table.insert(tmp2)
def updata(data_table):
    tmp1={'playerID': 'dlzxycx', 'nameLast': 'yang', 'weight': '100000'}
    new_value={'playerID': 'dlzxycx', 'nameLast': 'yangcx', 'weight': '1999900'}
    data_table.update_by_template(tmp1,new_value)
if __name__ == '__main__':
    data_table_t = init_data_table_test()
    print("insert 2 raws:chenxu,yang\n")
    insert(data_table_t)
    print('find chenxu,1980')
    find_by_template_test(data_table_t)
    print('update yang into yangcx\n')
    updata(data_table_t)
    print('delete chenxu\n')
    delete_by_template(data_table_t)
    print('\n')
    print('find chenxu, yangcx,1980')
    find_by_template_test(data_table_t)



