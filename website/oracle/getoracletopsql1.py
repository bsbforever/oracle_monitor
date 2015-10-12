import re
import os
import time
import datetime
import MySQLdb
def check_topsql(starttime,endtime,ipaddress,tnsname,topsql_type):
    hour=0
    result=[]
    for i in range(starttime,endtime,3600):
	hour=hour+1
    topsql=[]
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='oracle',port=3306)
    cur=conn.cursor()
    getsql_text='select * from oracle_oracle_'+topsql_type+' where sql_time <='+ str(endtime)+' and sql_time >='+str(starttime)+' and tnsname=\''+tnsname+'\' and ipaddress=\''+ipaddress+'\' group by sql_id ,sql_time'
    cur.execute(getsql_text)
    row=cur.fetchall()
    cur.close()
    conn.close()
    count=1
    sql_id='sql_id'
    for i in row:
	if i[4]==sql_id:
	    count=count+1
	    if count==hour:
		maxtime=i
		sql_id= maxtime[4]
            	sql_text=maxtime[10]
            	topsqltype=maxtime[5]-mintime[5]
            	executions=maxtime[6]-mintime[6]
            	module=maxtime[9]
            	if executions==0:
                    executions='1:0'
                    per_executions=float(topsqltype/int(executions.split(':')[0]))
                    cpu_time=float(((maxtime[7]-mintime[7])/int(executions.split(':')[0]))/1000000)
                    elapsed_time=float(((maxtime[8]-mintime[8])/int(executions.split(':')[0]))/1000000)
                else:
                    per_executions=float(topsqltype/executions)
                    cpu_time=float(((maxtime[7]-mintime[7])/executions)/1000000)
                    elapsed_time=float(((maxtime[8]-mintime[8])/executions)/1000000)
	        topsql.append([sql_id,sql_text,topsqltype,executions,per_executions,cpu_time,elapsed_time,module])  
	else:
	    mintime=i
	    count=1
	    sql_id=i[4]
	    
    topsql.sort(key=lambda x:x[2],reverse=True)
    for n in range(0,10):
        result.append(topsql[n])
    return result










 

if __name__ == '__main__':
    endtime=1438567200+60
    starttime=1438563600
    ipaddress='10.65.1.110'
    tnsname='mesft'
    topsql_type='buffergets'
    result= check_topsql(starttime,endtime,ipaddress,tnsname,topsql_type)











