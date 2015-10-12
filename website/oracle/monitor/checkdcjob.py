import re
import os
import subprocess
import cx_Oracle
from sendmail import *
def getdbname(cursor):
    '''db = cx_Oracle.connect(username+'/'+password+'@'+ ipaddress+':'+'/'+tnsname)
    cursor = db.cursor()'''
    cursor.execute('select name from v$database')
    row=cursor.fetchone()
    dbname=row[0]
    return dbname

def getinstancename(cursor):
    cursor.execute('select instance_name from v$instance')
    row=cursor.fetchone()
    instancename=row[0]
    return instancename

def checkinvalidobject(cursor):
    cursor.execute('SELECT count(*) FROM dba_objects  WHERE status = \'INVALID\'')
    row=cursor.fetchone()
    return row[0]

def check_mv_compile_states(cursor):
    cursor.execute('SELECT count(*) FROM DBA_MVIEWS  WHERE COMPILE_STATE <> \'VALID\'')
    row=cursor.fetchone()
    return row[0]

def checkjob(cursor):
    cursor.execute('select failures from dba_jobs')
    row1=cursor.fetchone()
    if row1 is None:
	j='nojob'
	return j
    else:
        cursor.execute('select failures from dba_jobs')
        row=cursor.fetchall()
        s='2'
	for i in row:
            if i[0]==0 or i[0] is None:
                s='normal'
            else:
                s='error'
                return s
        return s
def checkifrac(cursor):
    cursor.execute('select value from v$option where  parameter=\'Real Application Clusters\'')
    row=cursor.fetchone()
    result=row[0]
    return result

def checkram(cursor):
        cursor.execute('select status from v$rman_backup_job_details')
        row=cursor.fetchall()
        j=1
        try:
            for i in row:
                if j==30:
                    ram=i[0]
                    break
                else:
                    j=j+1
            return ram
        except:
            return 'None'            

def getdbsize(cursor):
    cursor.execute('select trunc(sum(bytes)/1024/1024/1024) Total from dba_segments')
    row=cursor.fetchone()
    result=row[0]
    return result    


def getspace(cursor):
    fp=open('/ezio/website/oracle/monitor/tablespacesize.sql','r') 
    fp1=fp.read()
    s=cursor.execute(fp1)
    fp.close()
    result=[]
    row=s.fetchall()
    for i in row:
	if i[4]>95:
	    result.append(i[0])
    result='|'.join(result)
    if len(result)==0:
        return 'normal'	
    else:
	return result

def checklock(cursor):
    fp1=open('/ezio/website/oracle/monitor/checklock.sql','r')
    fp=fp1.read()
    s=cursor.execute(fp)
    fp1.close()
    row1=s.fetchone()
    if row1 is None:
        j='normal'
        return  j
    else:
        fp2=open('/ezio/website/oracle/monitor/checklock.sql','r')
        fp=fp2.read()
        s=cursor.execute(fp)
	fp2.close()
        row=s.fetchall()
	for i in row:
	    lockdate=str(i[7])
	    get_dateinterval=cursor.execute('select floor((sysdate - to_date(\''+lockdate+'\',\'yyyy-mm-dd hh24:mi:ss\'))*24*60) from dual')
	    date_interval=get_dateinterval.fetchone()
	    if  date_interval[0]>30 :
		#print date_interval[0]
		return date_interval[0]
	    else:
		return 'normal'


def checkalert(cursor):
    try:
        cursor.execute('select * from alert_ext where log like \'%ORA-%\'')
        row1=cursor.fetchone()
        if row1 is None:
            j='normal'
            return j
        else:
            j='error'
            return j
    except Exception,e:
	return 'nolog'
if __name__ == '__main__':
    ipaddress='10.65.1.120'
    username='sys'
    password='ase_sys_n'
    port='1521'
    tnsname='DCTEST'
    db = cx_Oracle.connect(username+'/'+password+'@'+ipaddress+':'+port+'/'+tnsname ,mode=cx_Oracle.SYSDBA)
    cursor = db.cursor()
    s=checkinvalidobject(cursor)
    j=check_mv_compile_states(cursor)
    print s
    print j
    cursor.close()
    db.close()
