#!/usr/bin/python
#coding=utf-8
import MySQLdb
import re
import os
import cx_Oracle
import redis
import time
import datetime
import MySQLdb
from django.views.decorators.http import require_http_methods
from oracle.monitor.getoraclecommandresult import *
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpRequest
from django import template
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger     
from django.db.models.loading import get_model
from oracle.models import *
from oracle.form import *
from oracle.monitor.test import *
from oracle.monitor.oracletopsql import *
from oracle.monitor.highcharts_template import *
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from oracle.serializers import OracleListSerializer


class OracleListViewSet(viewsets.ModelViewSet):
    """
    允许查看和编辑user 的 API endpoint
    """
    queryset = oraclelist.objects.all()
    serializer_class = OracleListSerializer


# Create your views here.

def index(request):
    result=oraclelist.objects.all().order_by('tnsname')
    dic={'result':result}
    return render_to_response('index.html',dic)

def pages(request):
    return render_to_response('pages/index.html')

def mssql(request):
    result=Mssqllist.objects.all().order_by('ipaddress')
    dic={'result':result}
    return render_to_response('mssql.html',dic)

def check_topsql1(request):
    endtime= int(str(time.time()).split('.')[0])
    starttime=endtime-24*3600
    hendtime=time.localtime(endtime)
    hendtime=time.strftime('%Y/%m/%d %H',hendtime)
    hstarttime=time.localtime(starttime)
    hstarttime=time.strftime('%Y/%m/%d %H',hstarttime)
    topsql_type='oracle_topsql_diskreads'
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='oracle',port=3306)
    cur=conn.cursor()
    sqltext='select a.tnsname,format(avg(a.disk_reads/a.executions),0),a.sql_id,left(a.sql_text,40),a.module,count(*) from '+topsql_type+' a where ipaddress=\'10.65.1.113\' and sql_time<='+str(endtime)+' and sql_time>='+str(starttime)+' group by sql_id order by count(*) desc' 
    cur.execute(sqltext)
    row=cur.fetchall()
    cur.close()
    conn.close()
    title=topsql_type+'-'+hstarttime+'-'+hendtime
    tr=['数据库名','平均值','哈希值','SQL语句','模块','次数']
    dic ={'title':title,'tr':tr,'row':row}
    return render_to_response('oracle_command_result.html',dic)

def check_topsql(request):
    if request.method == 'POST': # If the form has been submitted...
        form = charts_topsql(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
	    top = form.cleaned_data['top']
	    starttime1  = request.POST['starttime']
	    endtime1  = request.POST['endtime']
	    ipaddress = form.cleaned_data['ipaddress'].split(':')[0]
	    tnsname = form.cleaned_data['ipaddress'].split(':')[1]
	    topsql_type= form.cleaned_data['topsql_type'].split(':')[0]
	    topsql_col=form.cleaned_data['topsql_type'].split(':')[1]
	    title=tnsname+'-'+topsql_type+'-'+str(starttime1)+'-'+str(endtime1)

	    if starttime1 =='' or endtime1 =='':
		return HttpResponse('Please give the Start and End time')
	    else:	
	    	starttime=int(str(time.mktime(time.strptime(starttime1,'%Y%m%d %H'))).split('.')[0])
	    	endtime=int(str(time.mktime(time.strptime(endtime1,'%Y%m%d %H'))).split('.')[0])+60
	    if  starttime>endtime:
		return HttpResponse('The Start time must larger than the End time')
	    	#starttime=int(str(time.mktime(time.strptime(starttime1,'%Y%m%d %H:%M:%S'))))
	    	#endtime=int(str(time.mktime(time.strptime(endtime1,'%Y%m%d %H:%M:%S'))))
	    else:
		    if topsql_type=='buffergets' or topsql_type=='diskreads':
		        row=check_topsql_final(starttime,endtime,ipaddress,tnsname,topsql_type,top)
		    elif topsql_type=='elapsedtime':
		        row=check_topsql_elapsedtime(starttime,endtime,ipaddress,tnsname,topsql_type,top)
		    elif topsql_type=='cputime':
		        row=check_topsql_cputime(starttime,endtime,ipaddress,tnsname,topsql_type,top)
		    else:
			row=check_topsql_topevent(starttime,endtime,ipaddress,tnsname,topsql_type,top)
			
			
		    top10sql=row['top10sql']
		    outsql=row['outsql']
		    if topsql_type=='buffergets' or topsql_type=='diskreads':		    
    		        tr=['SQL_ID','SQL 语句',topsql_type,'次数','每次的数据块数/块','CPU时间/秒','执行时间/秒','模块']
		    elif topsql_type=='elapsedtime':
    		        tr=['SQL_ID','SQL 语句',topsql_type,'次数','每次的时间/秒','CPU时间/秒','模块']
		    elif topsql_type=='cputime':
    		        tr=['SQL_ID','SQL 语句',topsql_type,'次数','每次的时间/秒','执行时间/秒','模块']
		    else:
			tr=['事件名称','等待时间/秒']
			
    		    dic ={'title':title,'tr':tr,'top10sql':top10sql,'outsql':outsql}
    		    return render_to_response('oracle_command_result.html',dic)


		    
	else:
           return render(request, 'check_topsql.html', {'form': form})
    else:
	form = charts_topsql() # An unbound form
	d1=datetime.datetime.now() 
	etime= d1.strftime("%Y%m%d %H")
	stime=(d1-datetime.timedelta(hours=1)).strftime("%Y%m%d %H")
	dic={'form':form,'etime':etime,'stime':stime}
        return render(request, 'check_topsql.html', dic)

def check_topsql11(request):
    if request.method == 'POST': # If the form has been submitted...
        form = charts_topsql(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
	    starttime1  = request.POST['starttime']
	    endtime1  = request.POST['endtime']
	    ipaddress = form.cleaned_data['ipaddress'].split(':')[0]
	    tnsname = form.cleaned_data['ipaddress'].split(':')[1]
	    topsql_type= form.cleaned_data['topsql_type'].split(':')[0]
	    topsql_col=form.cleaned_data['topsql_type'].split(':')[1]

	    if starttime1 =='' or endtime1 =='':
		return HttpResponse('Please give the Start and End time')
	    else:	
	    	starttime=int(str(time.mktime(time.strptime(starttime1,'%Y%m%d %H'))).split('.')[0])
	    	endtime=int(str(time.mktime(time.strptime(endtime1,'%Y%m%d %H'))).split('.')[0])+130
	    if  starttime>endtime:
		return HttpResponse('The Start time must larger than the End time')
	    	#starttime=int(str(time.mktime(time.strptime(starttime1,'%Y%m%d %H:%M:%S'))))
	    	#endtime=int(str(time.mktime(time.strptime(endtime1,'%Y%m%d %H:%M:%S'))))
	    else:
		    title=topsql_type+'-'+str(starttime1)+'-'+str(endtime1)
    		    conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='oracle',port=3306)
    		    cur=conn.cursor()
    		    sqltext='select a.tnsname,round(avg(a.'+topsql_col+'/a.executions),0) topsql_avg ,a.sql_id,left(a.sql_text,40),a.module,count(*) from oracle_topsql_'+topsql_type+' a where ipaddress=\''+str(ipaddress) +'\' and tnsname=\''+tnsname+'\'  and sql_time<='+str(endtime)+' and sql_time>='+str(starttime)+' group by sql_id order by topsql_avg  desc' 
		    cur.execute(sqltext)
    		    row=cur.fetchall()
    		    cur.close()
    		    conn.close()
    		    tr=['数据库名','平均值','哈希值','SQL语句','模块','次数']
    		    dic ={'title':title,'tr':tr,'row':row}
    		    return render_to_response('oracle_command_result.html',dic)


		    
	else:
           return render(request, 'check_topsql.html', {'form': form})
    else:
	form = charts_topsql() # An unbound form
	d1=datetime.datetime.now() 
	etime= d1.strftime("%Y%m%d %H")
	stime=(d1-datetime.timedelta(hours=24)).strftime("%Y%m%d %H")
	dic={'form':form,'etime':etime,'stime':stime}
        return render(request, 'check_topsql.html', dic)

@require_http_methods(["GET", "POST"])	
def check_graphic(request):
    if request.method == 'POST': # If the form has been submitted...
        form = charts_parameter(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
	    starttime1  = request.POST['starttime']
	    endtime1  = request.POST['endtime']
	    ipaddress1 = form.cleaned_data['ipaddress']
	    count = form.cleaned_data['granularity']
	    if starttime1 =='' or endtime1 =='':
		return HttpResponse('Please give the Start and End time')
	    else:	
	    	starttime=int(str(time.mktime(time.strptime(starttime1,'%Y%m%d %H'))).split('.')[0])
	    	endtime=int(str(time.mktime(time.strptime(endtime1,'%Y%m%d %H'))).split('.')[0])
	    if  starttime>endtime:
		return HttpResponse('The Start time must larger than the End time')
	    	#starttime=int(str(time.mktime(time.strptime(starttime1,'%Y%m%d %H:%M:%S'))))
	    	#endtime=int(str(time.mktime(time.strptime(endtime1,'%Y%m%d %H:%M:%S'))))
	    else:
		    ipaddress =str(ipaddress1).split(':')[0]
		    hostname =str(ipaddress1).split(':')[1]
		    title='Linux&Unix-'+hostname+'-'+ipaddress
		    title_y='Utilization'
		    x_categories=[]
		    final_series=[]
		    for categories in range (starttime,endtime+count*3600,count*3600):
		    #for categories in range (starttime,endtime,count*3600):
			categories=time.localtime(categories)
			interval= strf_local_time=time.strftime('%m/%d %H',categories)
			x_categories.append(interval)
		    #return HttpResponse(x_categories)
		    final_series=space_highcharts(x_categories,starttime,endtime,count,ipaddress)
		    dic={'categories':x_categories,'series':final_series,'title':title,'title_y':title_y}
		    return render_to_response('highcharts.html',dic) # Redirect after POST
	else:
           return render(request, 'check_graphic.html', {'form': form})
    else:
	form = charts_parameter() # An unbound form
	d1=datetime.datetime.now() 
	etime= d1.strftime("%Y%m%d %H")
	stime=(d1-datetime.timedelta(hours=12)).strftime("%Y%m%d %H")
	dic={'form':form,'etime':etime,'stime':stime}
        return render(request, 'check_graphic.html',dic)	

def os_performance(request):
    ip=[]
    ip1=linuxlist.objects.all().order_by('ipaddress')
    for i in ip1:
        ip.append(i.ipaddress+':'+i.hostname)
    if request.method == 'POST': # If the form has been submitted...
        form = cpumem(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
	    starttime1  = request.POST['starttime']
	    endtime1  = request.POST['endtime']
	    ipaddress_hostname=[]
	    ipaddress_hostname1=request.REQUEST.getlist('performance')
	    for j in ipaddress_hostname1:
		ipaddress_hostname.append(j)
	    os_performance = form.cleaned_data['os_performance']
	    count = form.cleaned_data['granularity']
	    if starttime1 =='' or endtime1 =='':
		return HttpResponse('Please give the Start and End time')
	    else:	
	    	starttime=int(str(time.mktime(time.strptime(starttime1,'%Y%m%d %H'))).split('.')[0])
	    	endtime=int(str(time.mktime(time.strptime(endtime1,'%Y%m%d %H'))).split('.')[0])
	    if  starttime>endtime:
		return HttpResponse('The Start time must larger than the End time')
	    	#starttime=int(str(time.mktime(time.strptime(starttime1,'%Y%m%d %H:%M:%S'))))
	    	#endtime=int(str(time.mktime(time.strptime(endtime1,'%Y%m%d %H:%M:%S'))))
	    else:
		    #ipaddress =str(ipaddress1).split(':')[0]
		    #hostname =str(ipaddress1).split(':')[1]
		    title='Linux&Unix '+os_performance+' Utilization'
		    title_y='Percents'
		    x_categories=[]
		    final_series=[]
		    for categories in range (starttime,endtime+count*600,count*600):
		    #for categories in range (starttime,endtime,count*3600):
			categories=time.localtime(categories)
			interval= strf_local_time=time.strftime('%m/%d %H:%M',categories)
			x_categories.append(interval)
		    final_series=cpumem_highcharts(x_categories,os_performance,starttime,endtime,count,ipaddress_hostname)
	#	    return HttpResponse(final_series)
		    dic={'categories':x_categories,'series':final_series,'title':title,'title_y':title_y}
		    return render_to_response('highcharts.html',dic) # Redirect after POST
	else:
           return render(request, 'os_performance.html', {'form': form})
    else:
	form = cpumem() # An unbound form
        ipaddress_checked=[]
        ipaddress_check=['10.65.1.37','10.65.1.105','10.60.14.60','10.65.1.117','10.65.1.102','10.65.1.104']
        for i in ip1:
            if i.ipaddress in ipaddress_check:
                ipaddress_checked.append(i.ipaddress+':'+i.hostname)
	d1=datetime.datetime.now()
        etime= d1.strftime("%Y%m%d %H")
        stime=(d1-datetime.timedelta(hours=4)).strftime("%Y%m%d %H")
        dic={'form':form,'ip':ip,'ipaddress_checked':ipaddress_checked,'etime':etime,'stime':stime}
        return render(request, 'os_performance.html', dic)
def check_hitratio(request):
    ip=[]
    ip1=oraclelist.objects.all().order_by('ipaddress')
    for i in ip1:
        ip.append(i.ipaddress+':'+i.tnsname) 
    if request.method == 'POST': # If the form has been submitted...
        form = charts_hitratio(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
	    ipaddress_tnsname=[]
	    ipaddress1=request.REQUEST.getlist('hitratio')
	    for i in ipaddress1:
		ipaddress_tnsname.append(i)
	    starttime1  = request.POST['starttime']
	    endtime1  = request.POST['endtime']
	    count = form.cleaned_data['granularity']
	    ratio_type= form.cleaned_data['ratio_type']

	    if starttime1 =='' or endtime1 =='':
		return HttpResponse('Please give the Start and End time')
	    else:	
	    	starttime=int(str(time.mktime(time.strptime(starttime1,'%Y%m%d %H'))).split('.')[0])
	    	endtime=int(str(time.mktime(time.strptime(endtime1,'%Y%m%d %H'))).split('.')[0])
	    if  starttime>endtime:
		return HttpResponse('The Start time must larger than the End time')
	    	#starttime=int(str(time.mktime(time.strptime(starttime1,'%Y%m%d %H:%M:%S'))))
	    	#endtime=int(str(time.mktime(time.strptime(endtime1,'%Y%m%d %H:%M:%S'))))
	    else:
		    title='Oracle Hit Ratio '+'-'+ratio_type
		    title_y='Ratio Percents'
		    x_categories=[]
		    final_series=[]
		    for categories in range (starttime,endtime+count*3600,count*3600):
		    #for categories in range (starttime,endtime,count*3600):
			categories=time.localtime(categories)
			interval= strf_local_time=time.strftime('%m/%d %H',categories)
			x_categories.append(interval)
		    final_series=hitratio_highcharts(x_categories,ratio_type,starttime,endtime,count,ipaddress_tnsname)
		    dic={'categories':x_categories,'series':final_series,'title':title,'title_y':title_y}
		    return render_to_response('highcharts.html',dic) # Redirect after POST
	else:
           return render(request, 'check_graphic.html', {'form': form})
    else:
	form = charts_hitratio() # An unbound form
	ipaddress_checked=[]
    	ipaddress_check=['10.65.1.203','10.65.1.118','10.60.14.70','10.65.1.119','10.65.1.113','10.65.1.109','10.65.1.110']
    	for i in ip1:
	    if i.ipaddress in ipaddress_check:
                ipaddress_checked.append(i.ipaddress+':'+i.tnsname)
	d1=datetime.datetime.now() 
	etime= d1.strftime("%Y%m%d %H")
	stime=(d1-datetime.timedelta(hours=24)).strftime("%Y%m%d %H")
	dic={'form':form,'ip':ip,'ipaddress_checked':ipaddress_checked,'etime':etime,'stime':stime}
        return render(request, 'check_hitratio.html', dic)	

def performance(request):
    ip=[]
    ip1=oraclelist.objects.all().order_by('ipaddress')
    for i in ip1:
        ip.append(i.ipaddress+':'+i.tnsname) 
    if request.method == 'POST': # If the form has been submitted...
        form = charts_performance(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
	 #   ipaddress=[]
	    ipaddress_tnsname=request.REQUEST.getlist('performance')
	   # for i in ipaddress1:
	#	ipaddress.append(i.split(':')[0])
	    starttime1  = request.POST['starttime']
	    endtime1  = request.POST['endtime']
	    performance_type= form.cleaned_data['performance_type']
	    count = form.cleaned_data['granularity']
	    if starttime1 =='' or endtime1 =='':
		return HttpResponse('Please give the Start and End time')
	    else:	
	    	starttime=int(str(time.mktime(time.strptime(starttime1,'%Y%m%d %H'))).split('.')[0])
	    	endtime=int(str(time.mktime(time.strptime(endtime1,'%Y%m%d %H'))).split('.')[0])
	    if  starttime>endtime:
		return HttpResponse('The Start time must larger than the End time')
	    	#starttime=int(str(time.mktime(time.strptime(starttime1,'%Y%m%d %H:%M:%S'))))
	    	#endtime=int(str(time.mktime(time.strptime(endtime1,'%Y%m%d %H:%M:%S'))))
	    else:
		    title='Oracle Performance'
		    title_y=performance_type+' Blocks'
		    x_categories=[]
		    final_series=[]
		    for categories in range (starttime,endtime+count*3600,count*3600):
		    #for categories in range (starttime,endtime,count*3600):
			categories=time.localtime(categories)
			interval= strf_local_time=time.strftime('%m/%d %H',categories)
			x_categories.append(interval)
		    final_series=performance_highcharts(x_categories,performance_type,count,starttime,endtime,ipaddress_tnsname)
		    dic={'categories':x_categories,'series':final_series,'title':title,'title_y':title_y}
		    #return HttpResponse(final_series)
		    return render_to_response('highcharts.html',dic) # Redirect after POST
	else:
           return render(request, 'performance.html', {'form': form})
    else:
	form = charts_performance() # An unbound form
	ipaddress_checked=[]
    	ipaddress_check=['10.65.1.203','10.65.1.118','10.60.14.70','10.65.1.119','10.65.1.113','10.65.1.109','10.65.1.110']
    	for i in ip1:
	    if i.ipaddress in ipaddress_check:
                ipaddress_checked.append(i.ipaddress+':'+i.tnsname)
	d1=datetime.datetime.now() 
	etime= d1.strftime("%Y%m%d %H")
	stime=(d1-datetime.timedelta(hours=24)).strftime("%Y%m%d %H")
	dic={'form':form,'ip':ip,'ipaddress_checked':ipaddress_checked,'etime':etime,'stime':stime}
        return render(request, 'performance.html', dic)	

def highcharts(request):
    r=redis.StrictRedis()
    count=1
    ipaddress=['10.65.1.203','10.65.1.118','10.60.14.70','10.65.1.119','10.65.1.113','10.65.1.109','10.65.1.110']
    title='Linux&Unix服务器磁盘空间'
    title_y='使用率'
    x_categories=[]
    endtime= int(str(time.time()).split('.')[0])
    final_series=[]
    starttime=endtime-24*3600
    for categories in range (starttime+count*3600,endtime+count*3600,count*3600):
	categories=time.localtime(categories)
	interval= strf_local_time=time.strftime('%m/%d %H',categories)
	x_categories.append(interval)
    final_series=hitratio_highcharts(x_categories,starttime,endtime,count,ipaddress)
    dic={'categories':x_categories,'series':final_series,'title':title,'title_y':title_y}
    return render_to_response('highcharts.html',dic)

def highcharts1(request):
    r=redis.StrictRedis()
    count=1
    x_categories=[]
    #endtime= int(r.lindex(i,0).split(':')[0])
    endtime= int(str(time.time()).split('.')[0])
    final_series=[]
    #endtime=time.time()
    starttime=endtime-24*3600
    for categories in range (starttime+count*3600,endtime+count*3600,count*3600):
	categories=time.localtime(categories)
	interval= strf_local_time=time.strftime('%m/%d %H',categories)
	x_categories.append(interval)
    
    for i in r.keys():
        if i.split('=')[0]=='Diskspace' and i.split('=')[1]=='10.60.14.60':
	    all_value={}
	    series_value=[]
	    series_singal={}
	    interval_value=[]
	    final_value2=[]
	#check  one more time that belong to same time interval.
	    for k in range(0,len(r.lrange(i,start=0,end=-1))):
	        value1=[]
		value=r.lindex(i,k).split(':')
		if int(endtime)>=int(value[0])> int(starttime):
		    time1=int(value[0])
		    local_time=time.localtime(time1)
		    strf_local_time=time.strftime('%m/%d %H',local_time)
		    #strf_local_time=time.strftime('%m/%d',local_time)
		    if all_value.has_key(strf_local_time):
		        value1.append(int(value[1]))
		        all_value[strf_local_time]=value1
		    else:
			del value1[:]
			value1.append(int(value[1]))
                        all_value[strf_local_time]=value1
	        		
		else:
		    if int(value[0]) <starttime:
			break
		    else:
			continue
	    #return HttpResponse(all_value.items())
	    for a in x_categories:
		if a  in all_value.keys():
		    pass
		else:
		    all_value[a]=[-10]
	    #return HttpResponse(all_value.keys())
    #calculate the avg result between one hours
	    result=sorted(all_value.items(),key=lambda all_value:all_value[0])
	    for key in result:
#		x_categories.append(key[0])
		l=0
		for n in key[1]:
		    l=l+n
		final_value=l/len(key[1])
		series_value.append(final_value)
	    #return HttpResponse(len(series_value))
    #calculate the avg. result while the calculate is larger than 1 hour
	    for p in range(0,len(series_value),count):
		interval_value1=series_value[p:p+count]
		interval_value.append(interval_value1)
	    #return HttpResponse(interval_value)
#	    x=0
	    for q in interval_value:
		x=0
		for y in q:
		    x=x+y
		final_value1=x/len(q)		
		final_value2.append(final_value1)
	    series_singal['name']=i.split('=')[3]
	    series_singal['data']=final_value2
    	    final_series.append(series_singal)
	    #return HttpResponse(series_singal['data'][2])
    #final_series = sorted(final_series, key=operator.itemgetter('name'))
    #return HttpResponse(final_series)
    dic={'categories':x_categories,'series':final_series}
    return render_to_response('highcharts.html',dic)


def sop(request):
    return render_to_response('sop.html')

def diskspace(request):
    result=[]
    r=redis.StrictRedis()
    for i in r.keys():
	last_time=int(r.lindex(i,0).split(':')[0])
	local_time=time.localtime(last_time)
        last_update_time=time.strftime('%m/%d %H',local_time)
    	nowtime= int(str(time.time()).split('.')[0])
	if i.split('=')[0]=='Diskspace' and nowtime - last_time<86400 and int(r.lindex(i,0).split(':')[1])>90:
	    ipaddress=i.split('=')[1]
	    hostname=i.split('=')[2]
	    diskname=i.split('=')[3]
	    value_now=r.lindex(i,0).split(':')[1]
	    #return HttpResponse(last_update_time)
	    k=0
	    for j in range(1,73 if len(r.lrange(i,start=0,end=-1))>73  else len(r.lrange(i,start=0,end=-1))):
		value_before=r.lindex(i,j).split(':')[1]
	        if value_now!=value_before:
		    change='Changed'
	    	    disk_status={'ipaddress':ipaddress,'hostname':hostname,'diskname':diskname,'value':value_now,'if_changed':change,'last_update_time':last_update_time}
	            result.append(disk_status)
		    k=1
		    break
	    if k==0:
	        change='No changed'
	        disk_status={'ipaddress':ipaddress,'hostname':hostname,'diskname':diskname,'value':value_now,'if_changed':change,'last_update_time':last_update_time}
	        result.append(disk_status)
    if len(result)>0:
	dic={'result':result}
	return render_to_response('diskspace.html',dic)
    else:
	return  HttpResponse('There is No DiskSpace Used above 90%')
def test(request):
    db = cx_Oracle.connect('sys/ase_sys_n@10.65.1.106/MESDEV' ,mode=cx_Oracle.SYSDBA)
    cursor = db.cursor()
    cursor.execute('select instance_name from v$instance')
    row=cursor.fetchone()
    instancename=row[0]
    cursor.close()
    db.close()
    return  HttpResponse(instancename)

def oracle_status(request):
    stamp=time.time()
    nowtime=time.localtime(stamp)
    nowtime= strf_local_time=time.strftime('%Y/%m/%d %H:%M',nowtime)
    result=oraclestatus.objects.all().order_by('tnsname')
    dic ={'result':result,'nowtime':nowtime}
    return render_to_response('oracle_status.html',dic)

def oracle_status2(request):
    result=oraclestatus.objects.all().order_by('tnsname')
    dic ={'result':result}
    return render_to_response('oracle_status2.html',dic)

def blog(request):
    result=Blog.objects.all().order_by('Name')
    dic={'result':result}
    return render_to_response('blog.html',dic)

def blog_sop(request,title):
    content = Blog.objects.get(Name=title).Content
    dic={'title':title,'content':content}
    return render_to_response('sop.html',dic)


def alert_event(request):
    result=alertevent.objects.all().order_by('createdate')
    dic={'result':result}
    return render_to_response('alert_event.html',dic)

def add_event(request):
    if request.method == 'POST': # If the form has been submitted...
        form = addevent(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            return HttpResponseRedirect('/oracle/alert_event') # Redirect after POST
    else:
	form = addevent() # An unbound form
        return render(request, 'addevent.html', {'form': form,})	

def check_server(ipaddress,port):
    import socket
    s=socket.socket()
    try:
        s.connect((ipaddress,port))
        return True
    except socket.error,e:
        return False

def scanport(request):
        return render_to_response('scanport.html')

def scanresult(request):
    try:
        ipaddress  = str(request.GET['ipaddress'])
        startport  = int(request.GET['startport'])
        endport  =   int(request.GET['endport'])
        if startport<=endport:
            ports=[]
            for i in range(startport,endport+1):
                ports.append(i)
            import socket
            openedport=[]
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            for port in ports:
                check = check_server(ipaddress, port)
                if (check):
                    openedport.append(port)
                else: pass
            dic={'ipaddress':ipaddress,'openedport':openedport}
            return render_to_response('finalresult.html',dic)
        else:
            return HttpResponse('The Endport must greater than startport')
    except Exception,e:
        #return HttpResponse('Please Fill all the blanks below or enter right value')
        return HttpResponse(e)

def oracle_command(request):
    result=oraclelist.objects.all().order_by('tnsname')
    dic={'result':result}
    return render_to_response('oracle_command.html',dic)


def  commandresult(request):
    ipaddress  = str(request.GET['ipaddress']).split('-')[0]
    tnsname=str(request.GET['ipaddress']).split('-')[1]
    command_content  = str(request.GET['operate'])
    result=oraclelist.objects.all().order_by('tnsname')
    for i in result:
	if i.ipaddress==ipaddress:
	    username =i.username
	    password=i.password
	    port=i.port
	    break
    if command_content=='check_session_count':
	try:
	    db = cx_Oracle.connect(username+'/'+password+'@'+ipaddress+':'+port+'/'+tnsname ,mode=cx_Oracle.SYSDBA)    
        except Exception , e:
            content= (ipaddress+' is Unreachable,The reason is '+ str(e)).strip()
	    return HttpResponse(content)
        else:
	    return HttpResponse('ss')
    elif command_content=='check_datafile_time':
	try:
	    db = cx_Oracle.connect(username+'/'+password+'@'+ipaddress+':'+port+'/'+tnsname ,mode=cx_Oracle.SYSDBA)    
        except Exception , e:
            content= (ipaddress+' is Unreachable,The reason is '+ str(e)).strip()
	    return HttpResponse(content)
        else:
	    cursor = db.cursor()
	    row=getdatafilecreationtime(cursor)
            cursor.close()
            db.close()
	    title='数据文件创建时间-'+ipaddress+'-'+tnsname
	    tr=['数据文件名称','文件大小','表空间','自动扩展','创建时间']
    	    dic ={'title':title,'tr':tr,'row':row}
	    return render_to_response('oracle_command_result1.html',dic)
	    
    elif command_content=='check_temp_usage':
	try:
	    db = cx_Oracle.connect(username+'/'+password+'@'+ipaddress+':'+port+'/'+tnsname ,mode=cx_Oracle.SYSDBA)    
        except Exception , e:
            content= (ipaddress+' is Unreachable,The reason is '+ str(e)).strip()
	    return HttpResponse(content)
        else:
	    cursor = db.cursor()
	    row=gettempusage(cursor)
            cursor.close()
            db.close()
	    title='数据库临时文件使用率-'+ipaddress+'-'+tnsname
	    tr=['使用率']
    	    dic ={'title':title,'tr':tr,'row':row}
	    return render_to_response('oracle_command_result1.html',dic)
    
    elif command_content=='check_executions':
	try:
	    db = cx_Oracle.connect(username+'/'+password+'@'+ipaddress+':'+port+'/'+tnsname ,mode=cx_Oracle.SYSDBA)    
        except Exception , e:
            content= (ipaddress+' is Unreachable,The reason is '+ str(e)).strip()
	    return HttpResponse(content)
        else:
	    cursor = db.cursor()
	    row=getexecutions(cursor)
            cursor.close()
            db.close()
	    title='执行次数等于一语句-'+ipaddress+'-'+tnsname
	    tr=['SQL语句','次数']
    	    dic ={'title':title,'tr':tr,'row':row}
	    return render_to_response('oracle_command_result1.html',dic)
    elif command_content=='check_unboundsql':
	try:
	    db = cx_Oracle.connect(username+'/'+password+'@'+ipaddress+':'+port+'/'+tnsname ,mode=cx_Oracle.SYSDBA)    
        except Exception , e:
            content= (ipaddress+' is Unreachable,The reason is '+ str(e)).strip()
	    return HttpResponse(content)
        else:
	    unboundsql  = str(request.GET['sql'])
	    cursor = db.cursor()
	    row=getunboundsql(cursor,unboundsql)
            cursor.close()
            db.close()
	    title='未绑定变量语句-'+ipaddress+'-'+tnsname
	    tr=['SQL语句','哈希值','模块','第一次载入时间','上一次载入时间']
    	    dic ={'title':title,'tr':tr,'row':row}
	    return render_to_response('oracle_command_result1.html',dic)
