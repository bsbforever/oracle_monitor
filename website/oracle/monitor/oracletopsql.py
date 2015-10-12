import re
import os
import time
import datetime
import MySQLdb
def check_topsql_final(starttime,endtime,ipaddress,tnsname,topsql_type,top):
    hour=0
    result={}
    for i in range(starttime,endtime,3600):
	hour=hour+1
    topsql=[]
    top10sql=[]
    outsql=[]
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='oracle',port=3306)
    cur=conn.cursor()
    getsql_text='select * from oracle_oracle_'+topsql_type+' where sql_time <='+ str(endtime)+' and sql_time >='+str(starttime)+' and tnsname=\''+tnsname+'\' and ipaddress=\''+ipaddress+'\' order by sql_id ,sql_time'
    cur.execute(getsql_text)
    row=cur.fetchall()
    cur.close()
    conn.close()
    count=hour
    sql_id='sql_id'
    for i in row:
	if i[4]==sql_id:
	    count=count+1
	    if count==hour:
		maxtime=i
		sql_id= maxtime[4]
            	sql_text=maxtime[10]
            	topsqltype=abs(maxtime[5]-mintime[5])
            	executions=abs(maxtime[6]-mintime[6])
            	module=maxtime[9]
            	if executions==0:
                    executions='1:0'
                    per_executions=float(topsqltype/int(executions.split(':')[0]))
                    cpu_time=abs(float(((maxtime[7]-mintime[7]))/int(executions.split(':')[0]))/1000000)
                    elapsed_time=abs(float(((maxtime[8]-mintime[8]))/int(executions.split(':')[0]))/1000000)
                else:
                    per_executions=float(topsqltype/executions)
                    cpu_time=abs(float(((maxtime[7]-mintime[7])/executions))/1000000)
                    elapsed_time=abs(float(((maxtime[8]-mintime[8])/executions))/1000000)
	        topsql.append([sql_id,sql_text,topsqltype,executions,per_executions,cpu_time,elapsed_time,module])  
	else:
	    if count!=hour and sql_id !='sql_id':
		outsql1=str(mintime[4])+'-'+str(mintime[10])+'-'+str(mintime[5])+' is wrapped out '+str(hour-count)+' times'
		outsql.append(outsql1)
	    mintime=i
	    count=1
	    sql_id=i[4]
	    
    if topsql_type=='elapsedtime':
	topsql.sort(key=lambda x:x[6],reverse=True)
    else:
        topsql.sort(key=lambda x:x[2],reverse=True)
    for n in range(0,top if len(topsql)>=top else len(topsql)):
        top10sql.append(topsql[n])
    result['top10sql']=top10sql
    if len(outsql)!=0:
        result['outsql']=outsql
    else:
	result['outsql']=[]
    return result



def check_topsql_elapsedtime(starttime,endtime,ipaddress,tnsname,topsql_type,top):
    hour=0
    result={}
    for i in range(starttime,endtime,3600):
	hour=hour+1
    topsql=[]
    top10sql=[]
    outsql=[]
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='oracle',port=3306)
    cur=conn.cursor()
    getsql_text='select * from oracle_oracle_'+topsql_type+' where sql_time <='+ str(endtime)+' and sql_time >='+str(starttime)+' and tnsname=\''+tnsname+'\' and ipaddress=\''+ipaddress+'\' order by sql_id ,sql_time'
    cur.execute(getsql_text)
    row=cur.fetchall()
    cur.close()
    conn.close()
    count=hour
    sql_id='sql_id'
    for i in row:
	if i[4]==sql_id:
	    count=count+1
	    if count==hour:
		maxtime=i
		sql_id= maxtime[4]
            	sql_text=maxtime[9]
		elapsedtime=abs((maxtime[7]-mintime[7]))/1000000
            	executions=abs(maxtime[5]-mintime[5])
            	module=maxtime[8]
            	if executions==0:
                    executions='1:0'
                    per_executions=float(elapsedtime/int(executions.split(':')[0]))
                    cpu_time=abs(float(((maxtime[6]-mintime[6]))/int(executions.split(':')[0]))/1000000)
                else:
                    per_executions=float(elapsedtime/executions)
                    cpu_time=abs(float(((maxtime[6]-mintime[6]))/executions)/1000000)
	        topsql.append([sql_id,sql_text,elapsedtime,executions,per_executions,cpu_time,module])  
	else:
	    if count!=hour and sql_id !='sql_id':
		outsql1=str(mintime[4])+'-'+str(mintime[9])+'-'+str(mintime[7])+' is wrapped out '+str(hour-count)+' times'
		outsql.append(outsql1)
	    mintime=i
	    count=1
	    sql_id=i[4]
	    
    topsql.sort(key=lambda x:x[2],reverse=True)
    for n in range(0,top if len(topsql)>=top else len(topsql)):
        top10sql.append(topsql[n])
    result['top10sql']=top10sql
    if len(outsql)!=0:
        result['outsql']=outsql
    else:
	result['outsql']=[]
    return result


def check_topsql_cputime(starttime,endtime,ipaddress,tnsname,topsql_type,top):
    hour=0
    result={}
    for i in range(starttime,endtime,3600):
	hour=hour+1
    topsql=[]
    top10sql=[]
    outsql=[]
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='oracle',port=3306)
    cur=conn.cursor()
    getsql_text='select * from oracle_oracle_'+topsql_type+' where sql_time <='+ str(endtime)+' and sql_time >='+str(starttime)+' and tnsname=\''+tnsname+'\' and ipaddress=\''+ipaddress+'\' order by sql_id ,sql_time'
    cur.execute(getsql_text)
    row=cur.fetchall()
    cur.close()
    conn.close()
    count=hour
    sql_id='sql_id'
    for i in row:
	if i[4]==sql_id:
	    count=count+1
	    if count==hour:
		maxtime=i
		sql_id= maxtime[4]
            	sql_text=maxtime[9]
		cputime=abs((maxtime[6]-mintime[6]))/1000000
            	executions=abs(maxtime[5]-mintime[5])
            	module=maxtime[8]
            	if executions==0:
                    executions='1:0'
                    per_executions=float(cputime/int(executions.split(':')[0]))
                    elapsed_time=abs(float(((maxtime[7]-mintime[7]))/int(executions.split(':')[0]))/1000000)
                else:
                    per_executions=float(cputime/executions)
                    elapsed_time=abs(float(((maxtime[7]-mintime[7])/executions))/1000000)
	        topsql.append([sql_id,sql_text,cputime,executions,per_executions,elapsed_time,module])  
	else:
	    if count!=hour and sql_id !='sql_id':
		outsql1=str(mintime[4])+'-'+str(mintime[9])+'-'+str(mintime[6])+' is wrapped out '+str(hour-count)+' times'
		outsql.append(outsql1)
	    mintime=i
	    count=1
	    sql_id=i[4]
	    
    topsql.sort(key=lambda x:x[2],reverse=True)
    for n in range(0,top if len(topsql)>=top else len(topsql)):
        top10sql.append(topsql[n])
    result['top10sql']=top10sql
    if len(outsql)!=0:
        result['outsql']=outsql
    else:
	result['outsql']=[]
    return result



def check_topsql_topevent(starttime,endtime,ipaddress,tnsname,topsql_type,top):
    hour=0
    result={}
    for i in range(starttime,endtime,3600):
	hour=hour+1
    topsql=[]
    top10sql=[]
    outsql=[]
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='oracle',port=3306)
    cur=conn.cursor()
    getsql_text='select * from oracle_oracle_'+topsql_type+' where sql_time <='+ str(endtime)+' and sql_time >='+str(starttime)+' and tnsname=\''+tnsname+'\' and ipaddress=\''+ipaddress+'\' order by event_name ,sql_time'
    cur.execute(getsql_text)
    row=cur.fetchall()
    cur.close()
    conn.close()
    count=hour
    idle=['LNS ASYNC end of log','Streams AQ: waiting for time management or cleanup tasks','jobq slave wait','SQL*Net message from client','rdbms ipc message','pmon timer','Streams AQ: qmn coordinator idle wait','Streams AQ: qmn slave idle wait','smon timer','dispatcher timer','PX Idle Wait','wakeup time manager','virtual circuit status']
    event_name='event_name'
    for i in row:
	if i[4] not in idle:
	    if i[4]==event_name :
	        count=count+1
	        if count==hour:
		    maxtime=i
		    event= maxtime[4]
		    waittime=abs((maxtime[5]-mintime[5]))/100
	            topsql.append([event,waittime])  
	    else:
	        if count!=hour and event_name !='event_name':
		    outsql1=str(mintime[4])+' is wrapped out '+str(hour-count)+' times'
		    outsql.append(outsql1)
	        mintime=i
	        count=1
	        event_name=i[4]
	else:
	    pass
	    
    topsql.sort(key=lambda x:x[1],reverse=True)
    for n in range(0,top if len(topsql)>=top else len(topsql)):
        top10sql.append(topsql[n])
    result['top10sql']=top10sql
    if len(outsql)!=0:
        result['outsql']=outsql
    else:
	result['outsql']=[]
    return result


 

if __name__ == '__main__':
    endtime=1438567200+60
    starttime=1438563600
    ipaddress='10.65.1.110'
    tnsname='mesft'
    topsql_type='buffergets'
    result= check_topsql_final(starttime,endtime,ipaddress,tnsname,topsql_type)
    print result










