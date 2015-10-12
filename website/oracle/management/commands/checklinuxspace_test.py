#coding=utf-8
#coding=gbk
from django.core.management.base import BaseCommand
from oracle.models import linuxlist
import threading
import paramiko
from oracle.monitor.getlinuxinfo import *
from oracle.monitor.sendmail import *
class Command(BaseCommand):
    def handle(self, *args, **options):
	def ssh2(os,ipaddress,username,password):
	    try:
		mailcontent=[]
		if os=='linux':
		    ssh = paramiko.SSHClient()
        	    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        	    ssh.connect(hostname=ipaddress,port=22,username=username,password=password)
        	    result=getlinuxspace(ssh)
                    ssh.close()
		    if result:
		        for j in result:
            	            split_value=j.split()
            		    if int(split_value[4][0:-1])>90:
			        result1='Be Careful,The Usage Of '+split_value[0]+' 0n '+ipaddress+' is '+split_value[4]+' Used'
                	        mailcontent.append(result1)
				return mailcontent
		    else:
			result1='The command executed error on '+ ipaddress
			mailcontent.append(result1)
			return mailcontent
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
                	        result1='Be Careful,The Usage Of '+split_value[0]+' on '+ipaddress+' is '+split_value[4]+' Used'
                	        mailcontent.append(result1)
		    else:
			result1='The command executed error on '+ ipaddress
                        mailcontent.append(result1)
			return mailcontent
	    except Exception, e:
        	result1=str(e)+ipaddress
        	mailcontent.append(result1)
		return mailcontent
	
        mailcontent1=[]
        threads=[]
        ip=linuxlist.objects.all().order_by('ipaddress')
        for i in ip:
            ipaddress=i.ipaddress
            username=i.username
            password=i.password
	    os=i.os
	    a=threading.Thread(target=ssh2,args=(os,ipaddress,username,password))
	    result=a.start()
	    #print result
	    if result is not None:
	        mailcontent1.append(result)
	    print ipaddress
	    #print ipaddress
        if len(mailcontent1) != 0:
            mailcontent='\n'.join(mailcontent1)
            send_mail(to_list,' Linux & Unix Space Monitor',mailcontent)                                                                               
