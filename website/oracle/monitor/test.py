import redis
r=redis.StrictRedis()
sort_name= 'date'
sort_start= 0
sort_num= -1
sort_by= 'TSSIZE:MESASSY:10.65.1.113:ODM:*'
sort_get= sort_by
#r.sort(sort_name,start=sort_start,num=sort_num,by=sort_by,get=['#',sort_get])
def getinfo():
    x_categories=r.lrange('date',0,-1)
    series_key='MESASSY'
    series_value=r.sort(sort_name,start=sort_start,num=sort_num,by=sort_by,get=sort_get)
    allinfo={'x_categories':x_categories,'series_key':series_key,'series_value':series_value}
    return allinfo

print getinfo()
