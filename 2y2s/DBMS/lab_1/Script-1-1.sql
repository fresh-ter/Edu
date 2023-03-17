--Кол-во актеров в БД
select count(*)
from (
	select distinct ci.person_id 
		from cast_info ci
		where (
			ci.role_id = 1 or ci.role_id = 2
		)
	) as ids
;
