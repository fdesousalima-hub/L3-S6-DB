\echo (REQ:20) Le nombre de remboursement par clients
select mail,count(*) from panier natural join prodpanier natural join demanderemboursement group by mail;
