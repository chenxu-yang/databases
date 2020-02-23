import src.data_service.data_table_adaptor as dta
import json
def t1():
    t=dta.get_rdb_table('people','lahman2019')
    print(t)
def t2():
    d=dta.get_databases()
    print('t2 result =',json.dumps(d,indent=2))
def t3(dbname):
    d=dta.get_tables('lahman2019clean')
    print('t2 result =', json.dumps(d, indent=2))
#t2()
#t3('lahman2019clean')
