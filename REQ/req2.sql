\echo (REQ:2) Get prix moyen des manga depuis leur existence
select nom,avg(cout) from (prix natural join manga) group by nom,isbn;
