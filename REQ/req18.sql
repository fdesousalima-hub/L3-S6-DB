\echo (REQ:18) Le nombre de produit en stock
select sum(quantite) from manga where statut = 'en stock';
