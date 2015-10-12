#coding=utf-8
#coding=gbk
from django.core.management.base import BaseCommand
from oracle.models import linuxlist
import time
import paramiko
from oracle.monitor.getlinuxinfo import *
from oracle.monitor.sendmail import *
class Command(BaseCommand):
    def handle(self, *args, **options):
        mailcontent=[]
        ip=linuxlist.objects.all().order_by('ipaddress')
        for i in ip:
            ipaddress=i.ipaddress
            username=i.username
            password=i.password
	    #print ipaddress
	    try:
		if i.os=='linux':
		    ssh = paramiko.SSHClient()
        	    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        	    ssh.connect(hostname=ipaddress,port=22,username=username,password=password)
        	    result=getlinuxspace(ssh)
                    ssh.close()
		    if result:
		        for j in result:
            	            split_value=j.split()
            		    if int(split_value[4][0:-1])>90:
			        result1='Be Careful,The Usage Of '+split_value[0]+' 0n '+i.hostname+' is '+split_value[4]+' Used'
                	        mailcontent.append(result1)
		    else:
			result1='The command executed error on '+ i.ipaddress
			mailcontent.append(result1)
		else:
		    ssh = paramiko.SSHClient()
        	    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        	    ssh.connect(hostname=ipaddress,port=22,username=username,password=password)
                    result=getunixspace(ssh)
                    ssh.close()
		    if result:
		        for j in result:
            		    split_value=j.split()
            		    if int(split_value[4][0:-1])>90:
                	        result1='Be Careful,The Usage Of '+split_value[0]+' on '+i.hostname+' is '+split_value[4]+' Used'
                	        mailcontent.append(result1)
		    else:
			result1='The command executed error on '+ i.ipaddress
                        mailcontent.append(result1)
	    except Exception, e:
        	result1=str(e)+i.ipaddress
        	mailcontent.append(result1)
        if len(mailcontent) != 0:
            mailcontent='\n'.join(mailcontent)
            send_mail(to_list,' Linux & Unix Space Monitor',mailcontent)                                                                               
