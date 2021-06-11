\echo (REQ:3) Get pour chaque avis les notes, avis, nom du manga et nom du client concerné
SELECT note, avis, manga.nom, client.nom FROM avis JOIN manga on manga.isbn = avis.isbn JOIN client ON client.mail = avis.mail;
