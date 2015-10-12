#!/usr/bin/python
#coding=utf-8
from django import forms 
from models import Blog    
from models import alertevent
from models import oraclelist    
from models import linuxlist    
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget 

class TestUeditorModelForm(forms.ModelForm):
    class Meta:
        model=Blog
	fields=['Name','Content']

class addevent(forms.ModelForm):
    class Meta:
        model=alertevent
	fields='__all__'

class charts_parameter(forms.Form):
    ip=[]
    ip1=linuxlist.objects.all().order_by('ipaddress')
    for i in ip1:
	ip.append((i.ipaddress+':'+i.hostname,i.ipaddress+'-'+i.hostname))
    #ipaddress=forms.IPAddressField()
    ipaddress=forms.ChoiceField(choices=ip)
    granularity = forms.IntegerField(initial=1)
    class Meta:
        app_label='oracle'

class cpumem(forms.Form):
    type_choice=(
	('CPU','CPU'),
	('MEMORY','MEMORY'),
	)
    os_performance=forms.ChoiceField(choices=type_choice)
    granularity = forms.IntegerField(initial=1)
    class Meta:
        app_label='oracle'

class charts_hitratio(forms.Form):
    type_choice=(
	('PinHit','PinHit'),
	('ReloadHit','ReloadHit'),
	('DicHit','DicHit'),
	('CacheHit','CacheHit'),
	('TempUsage','TempUsage'),
	)
    #ipaddress=forms.IPAddressField()
    granularity = forms.IntegerField(initial=1)
    ratio_type=forms.ChoiceField(choices=type_choice)
    class Meta:
        app_label='oracle'

class charts_performance(forms.Form):
    type_choice=(
	('diskreads:disk_reads','DiskReads'),
	('buffergets:buffer_gets','BufferGets'),
	('elapsedtime:elapsed_time','ElapsedTime'),
	('cputime:cpu_time','CpuTime'),
	)
    performance_type=forms.ChoiceField(choices=type_choice)
    granularity = forms.IntegerField(initial=1)
    class Meta:
        app_label='oracle'

class charts_topsql(forms.Form):
    ip=[]
    ip1=oraclelist.objects.filter(performance_type=1).order_by('ipaddress')
    for i in ip1:
	ip.append((i.ipaddress+':'+i.tnsname,i.ipaddress+'-'+i.tnsname))
    ipaddress=forms.ChoiceField(choices=ip)
    type_choice=(
	('diskreads:disk_reads','DiskReads'),
	('buffergets:buffer_gets','BufferGets'),
	('elapsedtime:elapsed_time','ElapsedTime'),
	('cputime:cpu_time','CpuTime'),
	('topevent:wait_time','TopEvent'),
	)
    topsql_type=forms.ChoiceField(choices=type_choice)
    top = forms.IntegerField(initial=10)
    class Meta:
        app_label='oracle'
