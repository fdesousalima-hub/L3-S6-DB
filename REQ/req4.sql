\echo (REQ:4) Get les client qui ont le meme nom et prenom
SELECT c1 FROM client c1 INNER JOIN client c2 ON c1.nom = c2.nom AND c1.prenom = c2.prenom and c1.mail !=c2.mail;
