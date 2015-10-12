#coding=utf-8
#coding=gbk
from django.core.management.base import BaseCommand
from oracle.models import oraclelist
import os
import redis
import time
from oracle.monitor.getoracleinfo import *
from oracle.monitor.sendmail import *
from oracle.monitor.getredisinfo import *
class Command(BaseCommand):
    def handle(self, *args, **options):
	mailcontent=[]
	r=redis.StrictRedis()
	nowtime=time.strftime('%Y%m%d',time.localtime(time.time()))
	r.rpush('date',nowtime)
	ip=oraclelist.objects.all().order_by('tnsname')
	for i in ip:
	    ipaddress=i.ipaddress
	    username=i.username
	    password=i.password
	    port=i.port
	    tnsname=i.tnsname
	    db = cx_Oracle.connect(username+'/'+password+'@'+ipaddress+':'+port+'/'+tnsname ,mode=cx_Oracle.SYSDBA)
	    cursor = db.cursor()
	    dbsize=getdbsize(cursor)
	    tbsize=gettbsize(cursor)
	    cursor.close()
    	    db.close()
	    for i in tbsize:
		tbkey='TSSIZE:'+tnsname+':'+ipaddress+':'+i[0]+':'+nowtime
		r.set(tbkey,i[1])
	    dbkey='DBSIZE:'+tnsname+':'+ipaddress+':'+nowtime
	    r.set(dbkey,dbsize) 
