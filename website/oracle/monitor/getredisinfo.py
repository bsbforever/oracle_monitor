import redis
import os
import re
import cx_Oracle

def getdbsize(cursor):
    cursor.execute('select trunc(sum(bytes)/1024/1024/1024) Total from dba_segments')
    row=cursor.fetchone()
    result=row[0]
    return result

def gettbsize(cursor):
    fp=open('/ezio/website/oracle/monitor/tablespacesize.sql','r')
    fp1=fp.read()
    s=cursor.execute(fp1)
    fp.close()
    row=s.fetchall()
    return row


if __name__ == '__main__':
    ipaddress='10.65.1.120'
    username='sys'
    password='ase_sys_n'
    port='1521'
    tnsname='DCTEST'
    db = cx_Oracle.connect(username+'/'+password+'@'+ipaddress+':'+port+'/'+tnsname ,mode=cx_Oracle.SYSDBA)
    cursor = db.cursor()
    s=test(cursor)
    print s
    cursor.close()
    db.close()

