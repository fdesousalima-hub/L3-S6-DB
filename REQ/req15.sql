\echo (REQ:15) Les clients né pendant la deuxieme guerre mondial
select mail from client where d_naissance > '1939-9-1' and d_naissance < '1945-9-2' ;
