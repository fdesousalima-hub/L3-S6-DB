\echo (REQ:8) Get le nombre moyens de produit par commande
select avg(sum) from (select sum(quantite) from panier natural join prodPanier group by id_panier) as foo;
