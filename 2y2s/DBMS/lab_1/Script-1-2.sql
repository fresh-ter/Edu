--select t.production_year, count(t.id) from title t where t.kind_id = 1 group by t.production_year ;

--Вывод кол-ва фильмов за каждый год в ХХ веке
--select t.production_year, count(t.id)
--	from title t
--	where 
--		t.kind_id = 1 and (t.production_year between 1900 and 1999)
--	group by t.production_year;

--Вывод среднего кол-ва фильмов в год за ХХ век
--select AVG(s.count)
--	from (
--		select t.production_year, count(t.id)
--			from title t
--			where 
--				t.kind_id = 1 and (t.production_year between 1900 and 1999)
--			group by t.production_year
--	) as s
--;

--Вывод округленного среднего кол-ва фильмов в год за ХХ и за XXI века
select
(
	select round(AVG(s.count))
		from (
			select t.production_year, count(t.id)
				from title t
				where 
					t.kind_id = 1 and (t.production_year between 1900 and 1999)
				group by t.production_year
		) as s
) as "AVG XX",
(
	select round(AVG(s.count))
		from (
			select t.production_year, count(t.id)
				from title t
				where 
					t.kind_id = 1 and (t.production_year between 2000 and 2999)
				group by t.production_year
		) as s
)  as "AVG XXI"
;
