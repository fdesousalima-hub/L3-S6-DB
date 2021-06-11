\echo (REQ:10) Get les nom des mangas dont la moyenne des note est superieur a 15
select nom from avis natural join manga group by nom having avg(note) > 15;
