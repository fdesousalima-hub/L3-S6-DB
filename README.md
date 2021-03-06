Rapport Base de Données - 
--

## Indications

### Prérequis

Pour utiliser correctement notre projet il faut avoir PostgreSQL d'installé

### Séparation

Au niveau des dossiers sources, ils sont séparés en 3:
* Un dossier `REQ` qui possèdent les 20 requêtes demandées dans le sujet
* Un dossier `CSV` qui possèdent le contenu des tables sql
* Un dossier `script` qui possèdent quelque scripts pour remplir les csv
* Nous avons un fichier `REQ.sql` qui liste les requêtes dans le dossier REQ
* Nous avons un fichier `tables.sql` qui est un script sql qui crée les différentes tables
* Nous avons un fichier `setBD.sql` qui est un script sql qui remplis les tables grâce au dossier CSV

## Création & Insertion

### Création des tables
```
psql
\i tables.sql
```

### Création des CSV
```
python3 script/*.py
```

### Insertion des CSV dans les tables
```
psql
\i setDB.sql
```

### Execution de toute les requêtes
```
psql
\i Req.sql
```
## Projet

Ce projet est une base de données d'un site de vente de manga.

Pour plus de détails voir ce [schèma](./shema.pdf)

## Sources

Pour les adresses :
    https://www.data.gouv.fr/fr/datasets/base-d-adresses-nationale-ouverte-bano/#_

Pour les patronymes et les noms :
    https://www.data.gouv.fr/fr/datasets/liste-de-prenoms-et-patronymes/
