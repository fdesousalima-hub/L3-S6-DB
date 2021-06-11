\echo (REQ:5) Get note moyenne pour chaque client qui ont noté
select mail,avg(note) from (select * from avis natural join client) as m group by mail
