SELECT * FROM (SELECT substr(sql_text,1,40) sql, 
disk_reads, executions, disk_reads/executions "Reads/Exec", 
hash_value,address 
FROM V$SQLAREA 
WHERE disk_reads > 1000 ORDER BY disk_reads DESC) 
where  rownum <= 10 
