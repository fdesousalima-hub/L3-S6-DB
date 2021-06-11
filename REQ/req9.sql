\echo (REQ:9) Get les noms des mangas qui sont disponible et qui ont recu une note superieur a 15
select nom from avis left join manga on manga.isbn = avis.isbn where note >= 15 and statut = 'en stock';
