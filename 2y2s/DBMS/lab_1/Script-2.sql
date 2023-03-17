--Вывод кол-ва ролей по каждому фильму
--select ci.movie_id, count(ci.id) 
--	from cast_info ci 
--	where ci.role_id in (1,2)
--	group by ci.movie_id
--	order by ci.movie_id asc
--;

select s.production_year, round(AVG(s.count))
	from (
		select ci.movie_id, count(ci.id), (select t.production_year  from title t where t.id = ci.movie_id)
			from cast_info ci 
			where ci.role_id in (1,2)
			group by ci.movie_id
			order by ci.movie_id asc
	) as s
	group by s.production_year
	order by s.production_year asc
;
