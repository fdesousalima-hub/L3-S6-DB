\echo (REQ:16) les clients qui ont achete un manga qui commence par Naruto
select distinct mail from panier natural join prodpanier join manga on paye='true' and manga.isbn = prodpanier.isbn and manga.nom like 'Naruto%';
