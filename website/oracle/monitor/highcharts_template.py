#!/usr/bin/python
#coding=utf-8
import redis
import time
import MySQLdb
from django.http import HttpResponse
from django.http import HttpRequest
def space_highcharts(x_categories,starttime,endtime,count,ipaddress):
        r=redis.StrictRedis()
	final_series=[]
	for i in r.keys():
		if i.split('=')[0]=='Diskspace' and i.split('=')[1]==ipaddress:
		    all_value={}
		    series_value=[]
		    series_singal={}
		    interval_value=[]
		    final_value2=[]
		#check  one more time that belong to same time interval.
		    for k in range(0,len(r.lrange(i,start=0,end=-1))):
			value1=[]
			value=r.lindex(i,k).split(':')
			if int(endtime)+300>=int(value[0])>=int(starttime):
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
			    all_value[a]=[0]
		    #return HttpResponse(all_value.keys())
	    #calculate the avg result between one hours
		    result=sorted(all_value.items(),key=lambda all_value:all_value[0])
		    for key in result:
	#               x_categories.append(key[0])
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
		    for q in interval_value:
			x=0
			for y in q:
			    x=x+y
			final_value1=x/len(q)
			final_value2.append(final_value1)
		    series_singal['name']=i.split('=')[3]
		    series_singal['data']=final_value2
		    final_series.append(series_singal)
	return final_series

def cpumem_highcharts(x_categories,os_performance,starttime,endtime,count,ipaddress_hostname):
        r=redis.StrictRedis()
	final_series=[]
	for i in r.keys():
		monitor= i.split('=')[1]+':'+i.split('=')[2]
		if i.split('=')[0]==os_performance and monitor in ipaddress_hostname:
		    all_value={}
		    series_value=[]
		    series_singal={}
		    interval_value=[]
		    final_value2=[]
		#check  one more time that belong to same time interval.
		    for k in range(0,len(r.lrange(i,start=0,end=-1))):
			value1=[]
			value=r.lindex(i,k).split(':')
			if int(endtime)+300>=int(value[0])>=int(starttime):
			    time1=int(value[0])
			    local_time=time.localtime(time1)
			    strf_local_time=time.strftime('%m/%d %H:%M',local_time)
			    #strf_local_time=time.strftime('%m/%d',local_time)
			    if all_value.has_key(strf_local_time):
				value1.append(float(value[1]))
				all_value[strf_local_time]=value1
			    else:
				del value1[:]
				value1.append(float(value[1]))
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
			    all_value[a]=[0]
		    #return HttpResponse(all_value.keys())
	    #calculate the avg result between one hours
		    result=sorted(all_value.items(),key=lambda all_value:all_value[0])
		    for key in result:
	#               x_categories.append(key[0])
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
		    for q in interval_value:
			x=0
			for y in q:
			    x=x+y
			final_value1=x/len(q)
			final_value2.append(final_value1)
		    series_singal['name']=i.split('=')[1]+'-'+i.split('=')[2]
		    series_singal['data']=final_value2
		    final_series.append(series_singal)
	return final_series
def hitratio_highcharts(x_categories,ratio_type,starttime,endtime,count,ipaddress_tnsname):
        r=redis.StrictRedis()
	final_series=[]
	for i in r.keys():
	        monitor=i.split('=')[1]+':'+i.split('=')[2]
		if i.split('=')[0]==ratio_type and monitor  in ipaddress_tnsname:
		    all_value={}
		    series_value=[]
		    series_singal={}
		    interval_value=[]
		    final_value2=[]
		#check  one more time that belong to same time interval.
		    for k in range(0,len(r.lrange(i,start=0,end=-1))):
			value1=[]
			value=r.lindex(i,k).split(':')
			if int(endtime)+300>=int(value[0])>=int(starttime):
			    time1=int(value[0])
			    local_time=time.localtime(time1)
			    strf_local_time=time.strftime('%m/%d %H',local_time)
			    #strf_local_time=time.strftime('%m/%d',local_time)
			    if all_value.has_key(strf_local_time):
				value1.append(float(value[1]))
				all_value[strf_local_time]=value1
			    else:
				del value1[:]
				value1.append(float(value[1]))
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
			    all_value[a]=[0]
		    #return HttpResponse(all_value.keys())
	    #calculate the avg result between one hours
		    result=sorted(all_value.items(),key=lambda all_value:all_value[0])
		    for key in result:
	#               x_categories.append(key[0])
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
		    for q in interval_value:
			x=0
			for y in q:
			    x=x+y
			final_value1=x/len(q)
			final_value2.append(final_value1)
		    series_singal['name']=i.split('=')[0]+'-'+i.split('=')[1]+'-'+i.split('=')[2]
		    series_singal['data']=final_value2
		    final_series.append(series_singal)
	return final_series







def performance_highcharts(x_categories,performance_type,count,starttime,endtime,ipaddress_tnsname):
    col_name=performance_type.split(':')[1]
    table_name=performance_type.split(':')[0]
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='oracle',port=3306)
    cur=conn.cursor()
    final_series=[]
    for i in ipaddress_tnsname:
	    ipaddress=i.split(':')[0]
	    tnsname=i.split(':')[1]
	    getsql_text='select sql_time,sum('+col_name+') from oracle_oracle_'+table_name+' where sql_time>='+str(starttime)+' and sql_time<='+str(endtime+60)+' and ipaddress=\''+ipaddress+'\' and tnsname=\''+tnsname+'\' group by sql_time order by sql_time'
	    cur.execute(getsql_text)
	    row=cur.fetchall()
	    result={}
	    data=[]
	    data1=[]
	    final_data=[]
	    final_single={}
	    for l in row:
		time1=time.localtime(l[0])
		interval= strf_local_time=time.strftime('%m/%d %H',time1)
		result[interval]=l[1]
	    for j in x_categories:
		if j in result.keys():
		    pass
		else:
		    result[j]=0
	    result1=sorted(result.items(),key=lambda result:result[0])
	    for k in result1:
		data.append(int(k[1]))
	    for  x   in range(0,len(data),count):
		data1.append(data[x:x+count])
	    for  y in data1:
		h=0
	        for z in y:
		    h=h+z
		final_data.append(h/len(y))	
		
	        
	    final_single['name']=table_name+'-'+ipaddress+'-'+tnsname
	    final_single['data']=final_data
	    final_series.append(final_single)
    cur.close()
    conn.close()
    return final_series
