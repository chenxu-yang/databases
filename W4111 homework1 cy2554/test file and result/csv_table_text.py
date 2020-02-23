# I write and test methods one at a time.
# This file contains unit tests of individual methods.

from src.CSVDataTable import CSVDataTable
import logging
import os
import json


# The logging level to use should be an environment variable, not hard coded.
logging.basicConfig(level=logging.DEBUG)

# Also, the 'name' of the logger to use should be an environment variable.
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# This should also be an environment variable.
# Also not the using '/' is OS dependent, and windows might need `\\`
data_dir = os.path.abspath("../Data/Baseball")

def t_load():

    connect_info = {
        "directory": data_dir,
        "file_name": "People.csv"
    }

    csv_tbl = CSVDataTable("people", connect_info, None)

    print("Created table = " + str(csv_tbl))

def t_save():
    connect_info = {
        "directory": data_dir,
        "file_name": "People.csv"
    }
    csv_tbl = CSVDataTable("people", connect_info, None)
    csv_tbl.save()
    print("save ok")

def t_match_template(csv,tmp):
    row={'cool':'yes','db':'no'}
    t={'cool':'yes'}
    result=CSVDataTable.matches_template(row,t)
    print("the match result is",result)

def test_match_all(csv,tmp):
    result=csv.find_by_template(tmp)
    print(json.dumps(result,indent=2))

def test_delete_by_template(csv,tmp):

    result=csv.delete_by_template(tmp)
    print("delete rows' number is",result)
def test_find_by_key():
    keyfields=['Aaron']
    connect_info = {
        "directory": data_dir,
        "file_name": "People.csv"
    }
    csv_tbl = CSVDataTable("people", connect_info, ['nameLast'])
    result=csv_tbl.find_by_primary_key(keyfields)
    print(json.dumps(result,indent=2))
def text_insert(csv,tmp):
    csv.insert(tmp)
def text_updata_by_template(csv,tmp,newvalue):
    result = csv.update_by_template(tmp,newvalue)
    print(result)
def t_match_template1(csv,tmp):
    result=csv.find_by_template(tmp)
    print("the match result is",result)



if __name__=="__main__":
    connect_info = {
            "directory": data_dir,
            "file_name": "People.csv"
        }
    tmp2={'nameLast': 'DaVanon'}
    changetmp={'nameLast': 'DaVanoncolllllll'}
    inserttmp={"playerID":"cy2554"}
    tmp3={'nameLast':'Aaron','weight':'180'}
    csv_tbl = CSVDataTable("people", connect_info, None)
    #t_match_template()


    #print('')
    #test_find_by_key()
    #print('')
    #t_save()
    #test_match_all()
    #print('')
    #test_find_by_key()
    print('insert  "playerID":"cy2554" \n')
    text_insert(csv_tbl,inserttmp)
    print('find insert tmp:"playerID":"cy2554" \n')
    t_match_template1(csv_tbl, inserttmp)
    print('delete "playerID":"cy2554"\n')
    test_delete_by_template(csv_tbl,inserttmp)
    print('find insert tmp:"playerID":"cy2554" \n')
    t_match_template1(csv_tbl, inserttmp)
    print('update "nameLast": "DaVanon" into nameLast: "DaVanoncolllllll"\n')
    text_updata_by_template(csv_tbl,tmp2,changetmp)
    print('find DaVanoncolllllll \n')
    t_match_template1(csv_tbl,changetmp)


