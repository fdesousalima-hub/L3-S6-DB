\echo 1 Get manga en stock avec un prix inferieur a 10
SELECT * FROM manga WHERE statut = 'en stock' AND prix <= 10.0;
