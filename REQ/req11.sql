\echo (REQ:11) Get les mails des gens qui ont une addresse de livraison differente de leur adresse
select * from client natural join panier where addresse != adresse_livraison;
