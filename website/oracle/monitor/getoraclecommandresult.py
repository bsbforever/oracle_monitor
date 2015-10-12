import re
import os
import subprocess
import cx_Oracle
from sendmail import *

def getdatafilecreationtime(cursor):
    fp=open('/ezio/website/oracle/monitor/oracle_command/getdatafilecreationtime.sql','r') 
    fp1=fp.read()
    s=cursor.execute(fp1)
    fp.close()
    row=s.fetchall()
    return row
def gettempusage(cursor):
    fp=open('/ezio/website/oracle/monitor/oracle_command/gettempusage.sql','r') 
    fp1=fp.read()
    s=cursor.execute(fp1)
    fp.close()
    row=s.fetchall()
    return row
def getexecutions(cursor):
    fp=open('/ezio/website/oracle/monitor/oracle_command/getexecutions.sql','r') 
    fp1=fp.read()
    s=cursor.execute(fp1)
    fp.close()
    row=s.fetchall()
    return row

def getunboundsql(cursor,unboundsql):
    fp=open('/ezio/website/oracle/monitor/oracle_command/getunboundsql.sql','r') 
    fp1=fp.read().strip()+unboundsql+'%\' order by last_load_time desc'
    s=cursor.execute(fp1)
    fp.close()
    row=s.fetchall()
    return row
if __name__ == '__main__':
    ipaddress='10.60.14.70'
    username='sys'
    password='ase_sys_1'
    port='1527'
    tnsname='NP1'
    try:
        db = cx_Oracle.connect(username+'/'+password+'@'+ipaddress+':'+port+'/'+tnsname ,mode=cx_Oracle.SYSDBA)
    except Exception , e:
        content= (tnsname+' is Unreachable,The reason is '+ str(e)).strip()
	print content
        #mailcontent.append(content)
    else:
        cursor = db.cursor()
        #j=check_mv_compile_states(cursor)
	row=getunboundsql(cursor)
        cursor.close()
        db.close()
	print row















