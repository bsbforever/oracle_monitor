#coding=utf-8
#coding=gbk
import time
from django.core.management.base import BaseCommand
from oracle.models import Mssqllist
import os
from oracle.monitor.getmssqlinfo import *
from oracle.monitor.sendmail_139 import *
class Command(BaseCommand):
    def handle(self, *args, **options):
        mailcontent=[]
	nowtime=time.time()
        ip=Mssqllist.objects.all().order_by('dbname')
        for i in ip:
	    if i.monitor_type==1:
		    ipaddress=i.ipaddress
		    instance=i.instance
		    username=i.username
		    password=i.password
		    port=i.port
		    dbname=i.dbname
		    if instance!='MSSQLSERVER':
		        ipaddress=ipaddress+'\\'+instance
		    try:
			conn = pymssql.connect(server=ipaddress,port=port,user=username,password=password,database=dbname,charset="UTF-8")
		    except Exception , e:
			content= (i.ipaddress+' is Unreachable,The reason is '+str(e)).strip()
			mailcontent.append(content)
			print mailcontent
		    else:
			cursor = conn.cursor()
			result=getfreesize(cursor)
			backup=checkbackup(cursor)
			cursor.close()
			conn.close()
			if result!='normal':
			    content='Be carefull, The '+i.dbname+' On '+ i.ipaddress+' Is '+result
			    mailcontent.append(content)
			for j in backup:
			    backuptime=str(time.mktime(j[0].timetuple())).split('.')[0]
			    timedelta=int(nowtime)-int(backuptime)
			    if timedelta>93600 and ipaddress not in ['10.65.202.103','10.65.1.210']:
				content='Be carefull, The backup of '+dbname+' On '+ ipaddress+' is failed '+str(timedelta)+' Seconds'
				mailcontent.append(content)
	if len(mailcontent) != 0:
	    mailcontent='\n'.join(mailcontent)
            send_mail(to_list,'MSSQL Database Monitor Status',mailcontent)
