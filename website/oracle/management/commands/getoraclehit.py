#coding=utf-8
#coding=gbk
from django.core.management.base import BaseCommand
from oracle.models import oraclelist
from oracle.models import *
import os
import redis
from oracle.monitor.getoracleperformaceinfo import *
from oracle.monitor.sendmail import *
class Command(BaseCommand):
    def handle(self, *args, **options):
	r=redis.StrictRedis()
        nowtime=str(time.time()).split('.')[0]
        ip=oraclelist.objects.all().order_by('tnsname')
        for i in ip:
	    if i.hit_type==1:
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
			cursor = db.cursor()
			getlibhit1=getlibhit(cursor)
			getdichit1=getdichit(cursor)
			getcachehit1=getcachehit(cursor)
			#undousage=getundousage(cursor)
			tempusage=gettemputilization(cursor)
			if float(tempusage)>1:
			    tempusagetext=gettempusagetext(cursor)
			    if tempusagetext:
				    for i in tempusagetext:
					sql_time=i[0]
					logon=i[1]
					osuser=i[2]
					tablespace=i[3]
					sql_text=i[4]
					insert=sortusagetext(ipaddress=ipaddress1,tnsname=tnsname1,sql_time=sql_time,logon=logon,osuser=osuser,tablespace=tablespace,sql_text=sql_text)
					insert.save()
			cursor.close()
			db.close()
			pinhit=getlibhit1[2]
			reloadhit=getlibhit1[4]
			dichit=getdichit1[2]
			cachehit=getcachehit1[0]
			reloadhitkey='ReloadHit='+ipaddress1+'='+tnsname1
                        reloadvalue=nowtime+':'+str(reloadhit)
                        r.lpush(reloadhitkey,reloadvalue)
			pinhitkey='PinHit='+ipaddress1+'='+tnsname1
                        pinvalue=nowtime+':'+str(pinhit)
                        r.lpush(pinhitkey,pinvalue)
			dichitkey='DicHit='+ipaddress1+'='+tnsname1
                        dicvalue=nowtime+':'+str(dichit)
                        r.lpush(dichitkey,dicvalue)
			cachehitkey='CacheHit='+ipaddress1+'='+tnsname1
                        cachevalue=nowtime+':'+str(cachehit)
                        r.lpush(cachehitkey,cachevalue)
			tempusagekey='TempUsage='+ipaddress1+'='+tnsname1
                        tempusagevalue=nowtime+':'+str(tempusage)
                        r.lpush(tempusagekey,tempusagevalue)
			#undousagekey='UndoUsage='+ipaddress1+'='+tnsname1
                        #undousagevalue=nowtime+':'+str(undousage)
                        #r.lpush(undousagekey,undousagevalue)
