#coding=utf-8
#coding=gbk
from django.core.management.base import BaseCommand
from oracle.models import oracledglist
import os
from oracle.monitor.getoracleinfo import *
from oracle.monitor.sendmail_139 import *
class Command(BaseCommand):
    def handle(self, *args, **options):
	mailcontent=[]
	ip=oracledglist.objects.all().order_by('tnsname')
	for i in ip:
	    if i.monitor_type==1:
	        ipaddress=i.ipaddress
	        username=i.username
	        password=i.password
	        port=i.port
	        tnsname=i.tnsname
	        try:
	            db = cx_Oracle.connect(username+'/'+password+'@'+ipaddress+':'+port+'/'+tnsname ,mode=cx_Oracle.SYSDBA)
	        except Exception , e:
                    content= (i.tnsname+' is Unreachable,The reason is '+str(e)).strip()
                    mailcontent.append(content)
		    print mailcontent
	        else:
	            cursor = db.cursor()
	            gap=checkdggap(cursor)
	            if gap =='normal':
		        pass
	            else:   
		        status=  'The DataGuard Have Errors On  '+i.tnsname+gap
		        mailcontent.append(status)
	            cursor.close()
    	            db.close()
	if len(mailcontent) != 0:
	    mailcontent='\n'.join(mailcontent)
	    send_mail(to_list,' ORACLE Database DataGuard Monitor ',mailcontent)
