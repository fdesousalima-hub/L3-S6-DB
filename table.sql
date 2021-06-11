drop table if exists manga cascade;
drop table if exists prix cascade;
drop table if exists auteur cascade;
drop table if exists editeur cascade;
drop table if exists client cascade;
drop table if exists panier cascade;
drop table if exists prodPanier cascade;
drop table if exists demandeRemboursement cascade;
drop table if exists avis cascade;

drop type if exists disponibilite;
drop type if exists etat_produit;
create type disponibilite as enum ('en stock', 'indisponible', 'sur commande');
create type etat_produit as enum ('panier','en attente','en preparation','expedie','livre','retourne','annule');

create table auteur (
    id_auteur serial primary key,
    nom varchar(32) not null,
    prenom varchar(32) not null
);

create table editeur (
    id_editeur serial primary key,
    nom varchar(32) not null
);

create table manga (
    isbn char(13) primary key,
    nom varchar(32) not null,
    tome int not null,
    prix float check (prix > 0),
    parution date,
    id_editeur serial references editeur(id_editeur),
    id_auteur serial references auteur(id_auteur),
    statut disponibilite not null,
    quantite int check (quantite > 0),
    delai date
);

create table prix (
    isbn char(13) references manga(isbn),
    dh date,
    cout float not null check (cout > 0),
    primary key (isbn,dh)
);

create table client (
    mail varchar primary key,
    nom varchar not null,
    prenom varchar not null,
    addresse varchar not null,
    tel char(10),
    d_naissance date not null,
    d_inscription date not null,
    constraint dni_cst check (d_naissance < d_inscription)
);

create table panier (
    id_panier serial primary key,
    mail varchar not null references client(mail),
    paye boolean not null,
    date_commande date,
    adresse_livraison varchar
);

create table prodPanier (
    id_panier serial references panier(id_panier),
    isbn char(13) references manga(isbn),
    quantite int not null check (quantite > 0),
    statut etat_produit not null,
    date_restock date,
    date_expedition date,
    date_livraison date,
    date_retour date,
    primary key(id_panier,isbn)
);

create table demandeRemboursement (
    id_panier serial references panier(id_panier),
    isbn char(13) references manga(isbn),
    date_demande date,
    raison text,
    primary key (id_panier,isbn)
);

create table avis (
    mail varchar references client(mail),
    isbn char(13) references manga(isbn),
    note int check (note >= 0 and note <= 20),
    avis text,
    primary key (mail,isbn)
);

\i setBD.sql
