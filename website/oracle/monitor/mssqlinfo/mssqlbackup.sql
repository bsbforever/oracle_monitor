select max(backup_finish_date) last_backup_date,database_name from msdb.dbo.backupset where type='D' group by database_name order by max(backup_finish_date) desc
