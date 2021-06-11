\echo (REQ:6) Get les mangas qui ont été acheté plus de 5 fois
select isbn,nom from manga where isbn in (select isbn from prodPanier where statut != 'panier' group by isbn having sum(quantite) > 5);
