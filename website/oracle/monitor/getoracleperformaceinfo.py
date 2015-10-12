import re
import os
import subprocess
import cx_Oracle
from sendmail import *

def getbuffergets_9i(cursor):
    fp=open('/ezio/website/oracle/monitor/oracle_performance/getbuffergets_9i.sql','r') 
    fp1=fp.read()
    s=cursor.execute(fp1)
    fp.close()
    row=s.fetchall()
    return row
def getdiskreads_9i(cursor):
    fp=open('/ezio/website/oracle/monitor/oracle_performance/getdiskreads_9i.sql','r') 
    fp1=fp.read()
    s=cursor.execute(fp1)
    fp.close()
    row=s.fetchall()
    return row

def getelapsedtime_9i(cursor):
    fp=open('/ezio/website/oracle/monitor/oracle_performance/getelapsedtime_9i.sql','r') 
    fp1=fp.read()
    s=cursor.execute(fp1)
    fp.close()
    row=s.fetchall()
    return row

def gettemputilization(cursor):
    fp=open('/ezio/website/oracle/monitor/oracle_performance/gettempusage.sql','r') 
    fp1=fp.read()
    s=cursor.execute(fp1)
    fp.close()
    row=s.fetchone()
    return row[0]

def gettempusagetext(cursor):
    fp=open('/ezio/website/oracle/monitor/oracle_performance/gettempusagetext.sql','r') 
    fp1=fp.read()
    s=cursor.execute(fp1)
    fp.close()
    row=s.fetchall()
    if row is not None:
        return row
    else:
	return False

def getundousage(cursor):
    fp=open('/ezio/website/oracle/monitor/oracle_performance/getundousage.sql','r') 
    fp1=fp.read()
    s=cursor.execute(fp1)
    fp.close()
    row=s.fetchone()
    return row[0]

def getlibhit(cursor):
    fp=open('/ezio/website/oracle/monitor/oracle_performance/getlibhit.sql','r') 
    fp1=fp.read()
    s=cursor.execute(fp1)
    fp.close()
    row=s.fetchone()
    return row

def getdichit(cursor):
    fp=open('/ezio/website/oracle/monitor/oracle_performance/getdichit.sql','r') 
    fp1=fp.read()
    s=cursor.execute(fp1)
    fp.close()
    row=s.fetchone()
    return row

def getcachehit(cursor):
    fp=open('/ezio/website/oracle/monitor/oracle_performance/getcachehit.sql','r') 
    fp1=fp.read()
    s=cursor.execute(fp1)
    fp.close()
    row=s.fetchone()
    return row

def getsqlplan(cursor):
    fp=open('/ezio/website/oracle/monitor/oracle_performance/sql_plan_9i.sql','r') 
    fp1=fp.read()
    s=cursor.execute(fp1)
    fp.close()
    row=s.fetchall()
    return row

def getbuffergets(cursor):
    s=cursor.execute('select hash_value, abs(buffer_gets),abs(executions) ,abs(cpu_time),abs(elapsed_time),module,substr(sql_text,0,40) from v$sqlarea where abs(buffer_gets)>10000')
    row=s.fetchall()
    return row

def getdiskreads(cursor):
    s=cursor.execute('select hash_value, abs(disk_reads),abs(executions) ,abs(cpu_time),abs(elapsed_time),module,substr(sql_text,0,40) from v$sqlarea where abs(disk_reads)>10000')
    row=s.fetchall()
    return row

def getelapsedtime(cursor):
    s=cursor.execute('select hash_value, abs(elapsed_time),abs(executions) ,abs(cpu_time),module,substr(sql_text,0,40) from v$sqlarea where abs(elapsed_time)>1000000000')
    row=s.fetchall()
    return row

def getcputime(cursor):
    s=cursor.execute('select hash_value, abs(cpu_time),abs(executions) ,abs(elapsed_time),module,substr(sql_text,0,40) from v$sqlarea where abs(cpu_time)>1000000000')
    row=s.fetchall()
    return row

def gettopevent(cursor):
    s=cursor.execute('select event,abs(time_waited) from v$system_event')
    row=s.fetchall()
    return row

def getsessionwait(cursor):
    s=cursor.execute('select substr(a.sql_text,0,50),a.HASH_VALUE,c.event,c.p1,c.P1RAW,c.p1text,c.p2,c.p2raw,c.p2text,c.p3,c.p3raw,c.p3text from v$sqlarea a, v$session b, v$session_wait c where a.hash_value = b.SQL_HASH_VALUE and b.sid = c.sid and c.event in (\'db file scattered read\',\'db file sequential read\',\'SQL*Net message from dblink\',\'sbtwrite2\',\'SQL*Net more data from dblink\',\'log file sync\')')
    row=s.fetchall()
    return row
if __name__ == '__main__':
    ipaddress='10.65.1.110'
    username='sys'
    password='ase_sys_1'
    port='1523'
    tnsname='mesft'
    try:
        db = cx_Oracle.connect(username+'/'+password+'@'+ipaddress+':'+port+'/'+tnsname ,mode=cx_Oracle.SYSDBA)
    except Exception , e:
        content= (tnsname+' is Unreachable,The reason is '+ str(e)).strip()
	print content
        #mailcontent.append(content)
    else:
        cursor = db.cursor()
        #j=check_mv_compile_states(cursor)
	row=getsessionwait(cursor)
        cursor.close()
        db.close()
	print row














