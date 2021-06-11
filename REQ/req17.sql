\echo (REQ:17) Le nombre de produit commandé depuis la creation du site
select sum(quantite) from prodpanier where statut != 'panier';
