do $$
declare
	rec record;
begin
	for rec in (select tablename from pg_catalog.pg_tables where tableowner = 'pguser')
	loop
		execute format('DROP TABLE %s', rec.tablename);
	end loop;
	
end $$