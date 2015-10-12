#coding=utf-8
from django.db import models
from django.utils.safestring import mark_safe
from django import forms
# Create your models here.

   
class Mssqllist(models.Model):
    ipaddress=models.GenericIPAddressField()
    instance=models.CharField(max_length=50,default='')
    hostname=models.CharField(max_length=100,default='')
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    port=models.CharField(max_length=50)
    dbname=models.CharField(max_length=50)
    content=models.CharField(max_length=100)
    monitor_type=models.IntegerField(default=1)
    def __unicode__(self):
        return self.dbname
    class Meta:
        app_label='oracle'

class linuxlist(models.Model):
    ipaddress=models.GenericIPAddressField(primary_key=True)
    hostname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    os=models.CharField(max_length=50)
    monitor_type=models.IntegerField(default=1)
    performance_type=models.IntegerField(default=0)
    def __unicode__(self):
        return self.ipaddress
    class Meta:
        app_label='oracle'


class Blog(models.Model):
    Name=models.CharField(max_length=100,blank=True)
    Content=models.TextField()
    def __unicode__(self):
        return self.Name
    class Meta:
        app_label='oracle'
    def display_content(self): 
        return mark_safe(self.Content)

class alertevent(models.Model):
    oracle_name=models.CharField(max_length=50,blank=True)
    problem=models.CharField(max_length=1000,blank=True)
    issuedate=models.CharField(max_length=100,blank=True)
    createdate=models.DateField(auto_now_add=True,blank=True)
    content=models.TextField()
    solution=models.CharField(max_length=1000,blank=True)
    control=models.CharField(max_length=10,blank=True)

class oraclelist(models.Model):
    ipaddress=models.GenericIPAddressField(primary_key=True)
    #ipaddress=models.GenericIPAddressField()
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    port=models.CharField(max_length=50)
    tnsname=models.CharField(max_length=100)
    version=models.CharField(max_length=100)
    charset=models.CharField(max_length=100)
    ncharset=models.CharField(max_length=100)
    hostname=models.CharField(max_length=100)
    alertpath=models.CharField(max_length=300)
    content=models.CharField(max_length=300)
    monitor_type=models.IntegerField(default=1)
    performance_type=models.IntegerField(default=0)
    hit_type=models.IntegerField(default=1)
    def __unicode__(self):
        return self.tnsname
    class Meta:
        app_label='oracle'

class oracledglist(models.Model):
    ipaddress=models.GenericIPAddressField()
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    port=models.CharField(max_length=50)
    tnsname=models.CharField(max_length=100)
    hostname=models.CharField(max_length=100)
    monitor_type=models.IntegerField(default=1)
    def __unicode__(self):
        return self.tnsname
    class Meta:
        app_label='oracle'

class oraclestatus(models.Model):
    tnsname=models.CharField(max_length=100)
    ipaddress=models.GenericIPAddressField()
    jobstatus=models.CharField(max_length=20)
    alertstatus=models.CharField(max_length=20)
    dbsize=models.CharField(max_length=50)
    tbstatus=models.CharField(max_length=200)
    invalid_object=models.IntegerField(default=0)
    mv_compile_state=models.IntegerField(default=0)
    host_name=models.CharField(max_length=50,default='host')
    version=models.CharField(max_length=50,default='10')
    startup_time=models.CharField(max_length=50,default='2015')
    status=models.CharField(max_length=20,default='opened')
    archiver=models.CharField(max_length=20,default='opened')
    sga_size=models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.tnsname
    class Meta:
        app_label='oracle'


class topsql(models.Model):
    ipaddress=models.GenericIPAddressField()
    tnsname=models.CharField(max_length=50)
    sql_time=models.CharField(max_length=100)
    sql_id=models.CharField(max_length=50)
    executions=models.BigIntegerField(blank=True)
    sharable_mem=models.BigIntegerField(blank=True)
    sorts=models.BigIntegerField(blank=True) 
    version_count=models.BigIntegerField(blank=True) 
    disk_read=models.BigIntegerField(blank=True) 
    buffer_gets_count=models.BigIntegerField(blank=True) 
    cpu_time=models.BigIntegerField(blank=True) 
    elapsed_time=models.BigIntegerField(blank=True) 
    module=models.CharField(max_length=65)
    sql_text=models.CharField(max_length=1000)
    def __unicode__(self):
        return self.ipaddress
    class Meta:
        app_label='oracle'

class oracle_buffergets(models.Model):
    ipaddress=models.GenericIPAddressField()
    tnsname=models.CharField(max_length=50)
    sql_time=models.BigIntegerField(blank=True)
    sql_id=models.CharField(max_length=50)
    buffer_gets=models.BigIntegerField(blank=True) 
    executions=models.BigIntegerField(blank=True)
    cpu_time=models.BigIntegerField(blank=True,null=True) 
    elapsed_time=models.BigIntegerField(blank=True,null=True) 
    module=models.CharField(max_length=65,null=True)
    sql_text=models.CharField(max_length=1000)
    def __unicode__(self):
        return self.ipaddress
    class Meta:
        app_label='oracle'

class oracle_diskreads(models.Model):
    ipaddress=models.GenericIPAddressField()
    tnsname=models.CharField(max_length=50)
    sql_time=models.BigIntegerField(blank=True)
    sql_id=models.CharField(max_length=50)
    disk_reads=models.BigIntegerField(blank=True) 
    executions=models.BigIntegerField(blank=True)
    cpu_time=models.BigIntegerField(blank=True,null=True) 
    elapsed_time=models.BigIntegerField(blank=True,null=True) 
    module=models.CharField(max_length=65,null=True)
    sql_text=models.CharField(max_length=1000)
    def __unicode__(self):
        return self.ipaddress
    class Meta:
        app_label='oracle'

class oracle_elapsedtime(models.Model):
    ipaddress=models.GenericIPAddressField()
    tnsname=models.CharField(max_length=50)
    sql_time=models.BigIntegerField(blank=True)
    sql_id=models.CharField(max_length=50)
    executions=models.BigIntegerField(blank=True)
    cpu_time=models.BigIntegerField(blank=True,null=True) 
    elapsed_time=models.BigIntegerField(blank=True,null=True) 
    module=models.CharField(max_length=65,null=True)
    sql_text=models.CharField(max_length=1000)
    def __unicode__(self):
        return self.ipaddress
    class Meta:
        app_label='oracle'

class oracle_cputime(models.Model):
    ipaddress=models.GenericIPAddressField()
    tnsname=models.CharField(max_length=50)
    sql_time=models.BigIntegerField(blank=True)
    sql_id=models.CharField(max_length=50)
    executions=models.BigIntegerField(blank=True)
    elapsed_time=models.BigIntegerField(blank=True,null=True) 
    cpu_time=models.BigIntegerField(blank=True,null=True) 
    module=models.CharField(max_length=65,null=True)
    sql_text=models.CharField(max_length=1000)
    def __unicode__(self):
        return self.ipaddress
    class Meta:
        app_label='oracle'

class oracle_topevent(models.Model):
    ipaddress=models.GenericIPAddressField()
    tnsname=models.CharField(max_length=50)
    sql_time=models.CharField(max_length=100)
    event_name=models.CharField(max_length=100)
    wait_time=models.BigIntegerField(blank=True)
    def __unicode__(self):
        return self.ipaddress
    class Meta:
        app_label='oracle'
class topsql_sharablemem(models.Model):
    ipaddress=models.GenericIPAddressField()
    tnsname=models.CharField(max_length=50)
    sql_time=models.CharField(max_length=100)
    sql_id=models.CharField(max_length=50)
    executions=models.BigIntegerField(blank=True)
    sharable_mem=models.BigIntegerField(blank=True)
    module=models.CharField(max_length=65,null=True)
    sql_text=models.CharField(max_length=1000)
    def __unicode__(self):
        return self.ipaddress
    class Meta:
        app_label='oracle'

class topsql_sorts(models.Model):
    ipaddress=models.GenericIPAddressField()
    tnsname=models.CharField(max_length=50)
    sql_time=models.CharField(max_length=100)
    sql_id=models.CharField(max_length=50)
    executions=models.BigIntegerField(blank=True)
    sorts=models.BigIntegerField(blank=True) 
    module=models.CharField(max_length=65,null=True)
    sql_text=models.CharField(max_length=1000)
    def __unicode__(self):
        return self.ipaddress
    class Meta:
        app_label='oracle'

class topsql_version(models.Model):
    ipaddress=models.GenericIPAddressField()
    tnsname=models.CharField(max_length=50)
    sql_time=models.CharField(max_length=100)
    sql_id=models.CharField(max_length=50)
    executions=models.BigIntegerField(blank=True)
    version_count=models.BigIntegerField(blank=True) 
    module=models.CharField(max_length=65,null=True)
    sql_text=models.CharField(max_length=1000)
    def __unicode__(self):
        return self.ipaddress
    class Meta:
        app_label='oracle'

class topsql_diskreads(models.Model):
    ipaddress=models.GenericIPAddressField()
    tnsname=models.CharField(max_length=50)
    sql_time=models.CharField(max_length=100)
    sql_id=models.CharField(max_length=50)
    executions=models.BigIntegerField(blank=True)
    disk_reads=models.BigIntegerField(blank=True) 
    module=models.CharField(max_length=65,null=True)
    sql_text=models.CharField(max_length=1000)
    def __unicode__(self):
        return self.ipaddress
    class Meta:
        app_label='oracle'

class topsql_buffergets(models.Model):
    ipaddress=models.GenericIPAddressField()
    tnsname=models.CharField(max_length=50)
    sql_time=models.CharField(max_length=100)
    sql_id=models.CharField(max_length=50)
    executions=models.BigIntegerField(blank=True)
    buffer_gets=models.BigIntegerField(blank=True) 
    module=models.CharField(max_length=65,null=True)
    sql_text=models.CharField(max_length=1000)
    def __unicode__(self):
        return self.ipaddress
    class Meta:
        app_label='oracle'

class topsql_cputime(models.Model):
    ipaddress=models.GenericIPAddressField()
    tnsname=models.CharField(max_length=50)
    sql_time=models.CharField(max_length=100)
    sql_id=models.CharField(max_length=50)
    executions=models.BigIntegerField(blank=True)
    cpu_time=models.BigIntegerField(blank=True) 
    module=models.CharField(max_length=65,null=True)
    sql_text=models.CharField(max_length=1000)
    def __unicode__(self):
        return self.ipaddress
    class Meta:
        app_label='oracle'

class topsql_elapsedtime(models.Model):
    ipaddress=models.GenericIPAddressField()
    tnsname=models.CharField(max_length=50)
    sql_time=models.CharField(max_length=100)
    sql_id=models.CharField(max_length=50)
    executions=models.BigIntegerField(blank=True)
    elapsed_time=models.BigIntegerField(blank=True) 
    module=models.CharField(max_length=65,null=True)
    sql_text=models.CharField(max_length=1000)
    def __unicode__(self):
        return self.ipaddress
    class Meta:
        app_label='oracle'

class sortusagetext(models.Model):
    ipaddress=models.GenericIPAddressField()
    tnsname=models.CharField(max_length=50)
    sql_time=models.CharField(max_length=100)
    logon=models.CharField(max_length=100)
    osuser=models.CharField(max_length=50)
    tablespace=models.CharField(max_length=50)
    sql_text=models.CharField(max_length=1000)
    def __unicode__(self):
        return self.ipaddress
    class Meta:
        app_label='oracle'
