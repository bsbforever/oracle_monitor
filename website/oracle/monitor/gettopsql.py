import re
import os
import subprocess
import cx_Oracle
import MySQLdb
from sendmail import *
def gettopread(cursor):
    fp=open('/ezio/website/oracle/monitor/gettopsql/topread.sql','r')
    fp1=fp.read()
    s=cursor.execute(fp1)
    fp.close()
    row=s.fetchall()
    return row

def getbufferget(cursor):
    fp=open('/ezio/website/oracle/monitor/gettopsql/buffer_gets.sql','r')
    fp1=fp.read()
    s=cursor.execute(fp1)
    fp.close()
    row=s.fetchall()
    return row

def getexecutions(cursor):
    fp=open('/ezio/website/oracle/monitor/gettopsql/executions.sql','r')
    fp1=fp.read()
    s=cursor.execute(fp1)
    fp.close()
    row=s.fetchall()
    return row

if __name__ == '__main__':
    ipaddress='10.65.1.118'
    username='sys'
    password='ase_sys_n'
    port='1524'
    tnsname='HDB'
    db = cx_Oracle.connect(username+'/'+password+'@'+ipaddress+':'+port+'/'+tnsname ,mode=cx_Oracle.SYSDBA)
    cursor = db.cursor()
    disk_read=gettopread(cursor)
    buffer_gets=getbufferget(cursor)
    executions=getexecutions(cursor)
    db.close()
    try:
        conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='oracle',port=3306)
        cur=conn.cursor()
    	j=1
    	for i in disk_read:
	    sql="insert into oracle_topsql(dbname,top_type,sql_text,total,executions,rate,hash_vaule,top_num,sql_time) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(sql,(tnsname,'DISK_READ',str(i[0]),int(i[1]),int(i[2]),float(i[3]),str(i[4]),int(j),str(i[5])))
	    j=j+1
	    #print value
    	j=1
    	for i in buffer_gets:
	    sql="insert into oracle_topsql(dbname,top_type,sql_text,total,executions,rate,hash_vaule,top_num,sql_time) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(sql,(tnsname,'BUFFER_GETS',str(i[0]),int(i[1]),int(i[2]),float(i[3]),str(i[4]),int(j),str(i[5])))
	    j=j+1
    	
	j=1
    	for i in executions:
	    sql="insert into oracle_topsql(dbname,top_type,sql_text,total,executions,rate,hash_vaule,top_num,sql_time) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(sql,(tnsname,'EXECUTIONS',str(i[0]),int(i[1]),int(i[2]),float(i[3]),str(i[4]),int(j),str(i[5])))
	    j=j+1
        cur.close()
        conn.commit()
        conn.close()
    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])
