SELECT 
  l.session_id sid, s.serial#,
  l.oracle_username,l.os_user_name,s.machine, 
  s.terminal, o.object_name, s.logon_time
FROM 
  v$locked_object l, all_objects o, v$session s
WHERE 
  l.object_id = o.object_id
AND 
  l.session_id = s.sid
ORDER BY 
  sid, s.serial#
