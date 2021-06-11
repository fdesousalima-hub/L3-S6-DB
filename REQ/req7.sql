\echo (REQ:7) Get le nombre de produit commande pour chaques client
select mail,sum(quantite) from panier natural join prodPanier group by mail;
