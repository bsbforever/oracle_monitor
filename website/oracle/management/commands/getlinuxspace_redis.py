#coding=utf-8
#coding=gbk
from django.core.management.base import BaseCommand
from oracle.models import linuxlist
import os
import redis
import time
from oracle.monitor.getlinuxinfo import *
from oracle.monitor.sendmail import *
class Command(BaseCommand):
    def handle(self, *args, **options):
	mailcontent=[]
	r=redis.StrictRedis()
	nowtime=str(time.time()).split('.')[0]
	ip=linuxlist.objects.all().order_by('ipaddress')
	for i in ip:
	    if i.monitor_type==1:
		    ipaddress=i.ipaddress
		    username=i.username
		    password=i.password
		    hostname1=i.hostname
		    try:
			if i.os=='linux':
			    ssh = paramiko.SSHClient()
			    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			    ssh.connect(hostname=ipaddress,port=22,username=username,password=password)
			    linuxspace=getlinuxspace(ssh)
			    ssh.close()
			    if linuxspace:
				for i in linuxspace:
				    dskey='Diskspace='+ipaddress+'='+hostname1+'='+i.split()[5]
				    value=nowtime+':'+ str(int(i.split()[4][0:-1]))
				    r.lpush(dskey,value)
			    else:
				result1='The command executed error on '+ i.ipaddress
				mailcontent.append(result1)
			else:
			    ssh = paramiko.SSHClient()
			    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			    ssh.connect(hostname=ipaddress,port=22,username=username,password=password)
			    unixspace=getunixspace(ssh)
			    ssh.close()
			    if unixspace:
				for i in unixspace:
				    dskey='Diskspace='+ipaddress+'='+hostname1+'='+i.split()[5]
				    value=nowtime+':'+ str(int(i.split()[4][0:-1]))
				    r.lpush(dskey,value)
			    else:
				result1='The command executed error on '+ i.ipaddress
				mailcontent.append(result1)
		    except Exception, e:
			result1=str(e)+ipaddress
			mailcontent.append(result1)
			print mailcontent
