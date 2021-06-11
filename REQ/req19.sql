\echo (REQ:19) Le classement des mangas les mieux notés
select nom,avg from (select isbn,avg(note) from avis group by isbn ) as f natural join manga order by avg desc;
