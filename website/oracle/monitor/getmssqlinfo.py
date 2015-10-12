import re
import os
import datetime
import pymssql
from sendmail import *
def getfreesize(cursor):
    cursor.execute('sp_spaceused')
    free_row=cursor.fetchone()
    if abs(float(free_row[2].split()[0])) <=0:
	return free_row[2]
    else:
	return 'normal'
	
def test(cursor):
    cursor.execute('sp_helpdb')
    free_row=cursor.fetchall()
    return free_row	

def checkbackup(cursor):
    cursor.execute('select max(backup_finish_date) last_backup_date,database_name from msdb.dbo.backupset where type=\'D\' and database_name not in (\'ReportServerTempDB\',\'model\',\'ReportServer\',\'master\',\'msdb\') group by database_name,type order by max(backup_finish_date) desc')
    row=cursor.fetchall()
    return row	

	
def checkbackup1(cursor):
    fp=open('/ezio/website/oracle/monitor/mssqlinfo/mssqlbackup.sql','r')
    fp1=fp.read()
    print fp1
    s=cursor.execute(fp1)
    row=s.fetchall()
    fp.close()
    return row
if __name__ == '__main__':
    ipaddress1='10.65.202.81'
    instance='MSSQLSERVER'
    ipaddress=ipaddress1+'\\'+instance
    username='sa'
    password="asen_2008"
    port='1433'
    dbname='plm'
    nowtime=datetime.datetime.now()
    conn = pymssql.connect(server=ipaddress1,port=port,user=username,password=password,database=dbname,charset="UTF-8")
    cursor = conn.cursor()
    row=checkbackup(cursor)
    for i in row:
	timestamp=str(time.mktime(i[0].timetuple())).split('.')[0]
	print timestamp
    cursor.close()
    conn.close()

