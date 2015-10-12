#coding=utf-8
#coding=gbk
from django.core.management.base import BaseCommand
from oracle.models import oraclelist
import os
from oracle.monitor.getoracleinfo import *
from oracle.monitor.sendmail import *
class Command(BaseCommand):
    def handle(self, *args, **options):
	mailcontent=[]
	ip=oraclelist.objects.all().order_by('tnsname')
	for i in ip:
	    ipaddress=i.ipaddress
	    username=i.username
	    password=i.password
	    port=i.port
	    tnsname=i.tnsname
	    db = cx_Oracle.connect(username+'/'+password+'@'+ipaddress+':'+port+'/'+tnsname ,mode=cx_Oracle.SYSDBA)
	    cursor = db.cursor()
	    lock=checklock(cursor)
	    print str(lock)+i.tnsname
	    cursor.close()
    	    db.close()
