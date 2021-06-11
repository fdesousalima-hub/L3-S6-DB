\echo (REQ:1) Get manga en stock avec un prix inferieur a 10
SELECT * FROM manga WHERE statut = 'en stock' AND prix <= 10.0;

\echo (REQ:2) Get prix moyen des manga depuis leur existence
select nom,avg(cout) from (prix natural join manga) group by nom,isbn;

\echo (REQ:3) Get pour chaque avis les notes, avis, nom du manga et nom du client concerné
SELECT note, avis, manga.nom, client.nom FROM avis JOIN manga on manga.isbn = avis.isbn JOIN client ON client.mail = avis.mail;

\echo (REQ:4) Get les client qui ont le meme nom et prenom
SELECT c1 FROM client c1 INNER JOIN client c2 ON c1.nom = c2.nom AND c1.prenom = c2.prenom and c1.mail !=c2.mail;

\echo (REQ:5) Get note moyenne pour chaque client qui ont noté
select mail,avg(note) from (select * from avis natural join client) as m group by mail

\echo (REQ:6) Get les mangas qui ont été acheté plus de 5 fois
select isbn,nom from manga where isbn in (select isbn from prodPanier where statut != 'panier' group by isbn having sum(quantite) > 5);

\echo (REQ:7) Get le nombre de produit commande pour chaques client
select mail,sum(quantite) from panier natural join prodPanier group by mail;

\echo (REQ:8) Get le nombre moyens de produit par commande
select avg(sum) from (select sum(quantite) from panier natural join prodPanier group by id_panier) as foo;

\echo (REQ:9) Get les noms des mangas qui sont disponible et qui ont recu une note superieur a 15
select nom from avis left join manga on manga.isbn = avis.isbn where note >= 15 and statut = 'en stock';

\echo (REQ:10) Get les nom des mangas dont la moyenne des note est superieur a 15
select nom from avis natural join manga group by nom having avg(note) > 15;

\echo (REQ:11) Get les mails des gens qui ont une addresse de livraison differente de leur adresse
select * from client natural join panier where addresse != adresse_livraison;

\echo (REQ:12) Get les panier dont tout les produits sont disponible
select distinct id_panier from panier natural join prodpanier where not exists ( select * from manga where manga.isbn = prodpanier.isbn and (statut = 'indisponible' or statut = 'sur commande'));

\echo (REQ:13) Le mangas disponible edité par Glenat
select manga.nom from manga join editeur on editeur.nom = 'Glenat' and statut = 'en stock' and manga.id_editeur = editeur.id_editeur ;

\echo (REQ:14) Le nom et le prix du manga le moins cher
select nom,prix from manga where prix = (select max(prix) from manga);

\echo (REQ:15) Les clients né pendant la deuxieme guerre mondial
select mail from client where d_naissance > '1939-9-1' and d_naissance < '1945-9-2' ;

\echo (REQ:16) les clients qui ont achete un manga qui commence par Naruto
select distinct mail from panier natural join prodpanier join manga on paye='true' and manga.isbn = prodpanier.isbn and manga.nom like 'Naruto%';

\echo (REQ:17) Le nombre de produit commandé depuis la creation du site
select sum(quantite) from prodpanier where statut != 'panier';

\echo (REQ:18) Le nombre de produit en stock
select sum(quantite) from manga where statut = 'en stock';

\echo (REQ:19) Le classement des mangas les mieux notés
select nom,avg from (select isbn,avg(note) from avis group by isbn ) as f natural join manga order by avg desc;

\echo (REQ:20) Le nombre de remboursement par clients
select mail,count(*) from panier natural join prodpanier natural join demanderemboursement group by mail;

