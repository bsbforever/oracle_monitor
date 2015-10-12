#coding=utf-8
#coding=gbk
from django.core.management.base import BaseCommand
from oracle.models import oraclelist
from oracle.models import *
import os
import types
from oracle.monitor.getoracleperformaceinfo import *
from oracle.monitor.sendmail import *
class Command(BaseCommand):
    def handle(self, *args, **options):
        ip=oraclelist.objects.all().order_by('tnsname')
	sql_time=str(time.time()).split('.')[0]
        for i in ip:
	    if i.monitor_type==1 and i.performance_type==1:
		    ipaddress1=i.ipaddress
		    username=i.username
		    password=i.password
		    port=i.port
		    tnsname1=i.tnsname
		    try:
			db = cx_Oracle.connect(username+'/'+password+'@'+ipaddress1+':'+port+'/'+tnsname1 ,mode=cx_Oracle.SYSDBA)
		    except Exception , e:
			content= (i.ipaddress+' is Unreachable,The reason is '+str(e)).strip()
			send_mail(to_list,'Oracle Performance Monitor Exception Occured',content)
			print content
		#	break
		    else:
			if i.version=='9i' or i.version=='10g':
				cursor = db.cursor()
				buffergets_9i=getbuffergets_9i(cursor)
				diskreads_9i=getdiskreads_9i(cursor)
				elapsedtime_9i=getelapsedtime_9i(cursor)
				cursor.close()
				db.close()
				for j in buffergets_9i:
				    sql_id=j[0]
				    executions=j[1]
				    buffer_gets=j[2]
				    module=j[3]
				    sql_text=j[4]
				    insert=topsql_buffergets(ipaddress=ipaddress1,tnsname=tnsname1,sql_time=sql_time,sql_id=sql_id,executions=executions,buffer_gets=buffer_gets,module=module,sql_text=sql_text)
				    insert.save()

				for j in diskreads_9i:
				    sql_id=j[0]
				    executions=j[1]
				    disk_reads=j[2]
				    module=j[3]
				    sql_text=j[4]
				    insert=topsql_diskreads(ipaddress=ipaddress1,tnsname=tnsname1,sql_time=sql_time,sql_id=sql_id,executions=executions,disk_reads=disk_reads,module=module,sql_text=sql_text)
				    insert.save()
				for j in elapsedtime_9i:
				    sql_id=j[0]
				    executions=j[1]
				    elapsed_time=j[2]
				    module=j[3]
				    sql_text=j[4]
				    insert=topsql_elapsedtime(ipaddress=ipaddress1,tnsname=tnsname1,sql_time=sql_time,sql_id=sql_id,executions=executions,elapsed_time=elapsed_time,module=module,sql_text=sql_text)
				    insert.save()
