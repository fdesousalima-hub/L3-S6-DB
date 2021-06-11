\echo (REQ:12) Get les panier dont tout les produits sont disponible
select distinct id_panier from panier natural join prodpanier where not exists ( select * from manga where manga.isbn = prodpanier.isbn and (statut = 'indisponible' or statut = 'sur commande'));
