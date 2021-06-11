\echo (REQ:13) Le mangas disponible edité par Glenat 
select manga.nom from manga join editeur on editeur.nom = 'Glenat' and statut = 'en stock' and manga.id_editeur = editeur.id_editeur ;
