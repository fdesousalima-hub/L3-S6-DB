#!/usr/bin/env python3

import random
import datetime
import os

mailF = ["Gmail.com","free.fr","hotmail.fr","yahoo.com"]

def getNomPrenomAdress():
    n = list()
    p = list()
    a = list()
    with open("noms") as noms:
        for nom in noms.read().splitlines():
            n.append(nom)
    with open("prenoms") as prenoms:
        for prenom in prenoms.read().splitlines():
            p.append(prenom)
    with open("adresses75") as adds:
        for add in adds.read().splitlines():
            a.append(add)
    return n,p,a

def creeDate(fin=datetime.datetime.now(), debut=datetime.datetime(1900, 1, 1)):
    jourPossible = random.randrange(abs((fin - debut).days))
    date = debut + datetime.timedelta(days=jourPossible)
    return date

def datePlusJour(date,nbJour):
    d = date.split("/")
    date = datetime.datetime(int(d[0]), int(d[1]), int(d[2]))
    return (date + datetime.timedelta(days = nbJour)).strftime('%Y/%m/%d')

def creeClient(n,p,a,id,mails,addresses):
    nom = random.choice(n).lower()
    prenom = random.choice(p).lower()
    addresse = random.choice(a)
    addresses.add(addresse)
    mail = (nom+ "." + prenom).replace(" ","_") + "." + str(id) + "@" + random.choice(mailF)
    mails.add(mail)
    tel = random.choice(["06","07"]) + "".join([random.choice("0123456789") for i in range(8)])
    dateNaissance = creeDate(fin = datetime.datetime.now() - datetime.timedelta(days=365*18))   # Personne majeur
    dateInscription = creeDate(debut = datetime.datetime(2010, 1, 1)) # site cree le 1 janvier 2010
    dateNaissance = dateNaissance.strftime('%Y/%m/%d')
    dateInscription = dateInscription.strftime('%Y/%m/%d')
    return mail + "," + nom + "," + prenom + "," + addresse + "," +\
            tel + "," + dateNaissance + "," + dateInscription

def setClientCSV(nbClient,n,p,a):
    mails = set()
    addresses = set()
    with open("../CSV/clients.csv","w") as f:
        f.write("mail,nom,prenom,addresse,tel,d_naissance,d_inscription\n")
        for id in range(nbClient):
            f.write(creeClient(n,p,a,id,mails,addresses) + "\n")
    return mails,addresses

def creeISBN(isbns):
    isbn = "".join([random.choice("0123456789") for i in range(13)])
    while isbn in isbns:
        isbn = "".join([random.choice("0123456789") for i in range(13)])
    isbns.add(isbn)
    return isbn

def creeManga(manga,auteurs,editeurs,isbns,mangascsv):
    s = manga.split(";")
    if (s[2] not in auteurs):auteurs[s[2]] = len(auteurs)
    if (s[3] not in editeurs):editeurs[s[3]] = len(editeurs)
    jour,mois,annee = s[4].split("/")
    date = datetime.datetime(int(annee), int(mois), int(jour))
    for tome in range(int(s[1])):
        prix = random.random() * 100 # prix aleatoire entre 0 et 100
        isbn = creeISBN(isbns)
        statut = random.choice(['en stock', 'indisponible', 'sur commande'])
        quantite,delai = "",""
        if statut == "en stock": quantite = random.randint(0,100000)
        if statut == "sur commande":
            delai = creeDate(debut = datetime.datetime.now(),fin = datetime.datetime(2100, 1, 1))
            delai = delai.strftime('%Y/%m/%d')
        mangascsv.write(isbn + "," + s[0] + " - VOL "+ str(tome) + "," + str(tome) +
            "," + str(prix) + "," + date.strftime('%Y/%m/%d') + "," + str(editeurs[s[3]]) +
            "," + str(auteurs[s[2]]) + "," + statut + "," + str(quantite) + "," + delai + "\n")
        date = date + datetime.timedelta(days=60) # On dit qu'un nouveau tome est publié tout les 60 jours

def setMangaAuteurEditeurPrixCSV():
    mangascsv = open("../CSV/mangas.csv","w")
    editeurs = dict()
    auteurs = dict()
    isbns = set()
    with open("mangas") as mangas:
        mangascsv.write("isbn,nom,tome,prix,parutionid_editeur,id_auteur,statut,quantite,delai\n")
        for manga in mangas.read().splitlines():
            creeManga(manga,auteurs,editeurs,isbns,mangascsv)
    mangascsv.close()
    with open("../CSV/auteurs.csv","w") as fileAuteurs:
        fileAuteurs.write("id,nom,prenom\n")
        for auteur,id in auteurs.items():
            nom , prenom = auteur.split("_")
            fileAuteurs.write(str(id) + "," + nom + "," + prenom + "\n")
    with open("../CSV/editeurs.csv","w") as fileEditeur:
        fileEditeur.write("id,nom\n")
        for nom,id in editeurs.items():
            fileEditeur.write(str(id) + "," + nom + "\n")
    setPrixCSV(isbns)
    return isbns

def setPrixCSV(isbns):
    with open("../CSV/prix.csv","w") as prix:
        prix.write("isbn,dh,cout\n")
        for isbn in isbns:
            s = set()
            for elt in range(random.randint(0,5)):
                date = creeDate()
                if date not in s:
                    cout = random.random() * 100 # prix aleatoire entre 0 et 100
                    date = date.strftime('%Y/%m/%d')
                    prix.write(isbn + "," + date + "," + str(cout) + "\n")

def setPanierCSV(mails,addresses,nbPanier):
    commandes = set()
    with open("../CSV/paniers.csv","w") as panier:
        panier.write("id,mail,paye,date_commande,adresse_livraison\n")
        for id in range(nbPanier):
            paye = random.choice([True,False])
            date,addresse = "",""
            mail = random.sample(mails,1)[0]
            if paye:
                date = creeDate (debut=datetime.datetime(2010, 1, 1))
                date = date.strftime('%Y/%m/%d')
                addresse = random.choice(["",random.sample(addresses,1)[0]])
                commandes.add((id,date,mail))
            panier.write(str(id) + "," + mail + "," + str(paye) +
                "," + date + "," + addresse + "\n")
    return commandes

def panierPaye(panier,id):
    for p in panier:
        if p[0] == id:
            return p[1]
    return None

def setProdPanierCSV(nbPanier,commandes,isbns):
    remboursement = set()
    livre = set()
    with open("../CSV/prodPanier.csv","w") as prod:
        prod.write("id_panier,isbn,quantite,satut,date_restock,date_expedition,date_livraison,date_retour\n")
        for idPanier in range(nbPanier):
            iss = set()
            for i in range(random.choice(range(3))):
                isbn = random.sample(isbns,1)[0]
                while isbn in iss:isbn = random.sample(isbns,1)[0]
                iss.add(isbn)
                quantite = str(random.choice(range(1,3)))
                date = panierPaye(commandes,idPanier)
                if (date == None): statut = "panier"
                else : statut = random.choice(["en attente","en preparation","expedie","livre","retourne","annule"])
                date_restock = ""
                date_expedition = ""
                date_livraison = ""
                date_retour = ""
                if statut == "en attente": date_restock = datePlusJour(date,random.choice(range(30)))
                elif statut == "expedie" : date_expedition = datePlusJour(date,random.choice(range(10)))
                elif statut == "livre" :
                    livre.add((idPanier,isbn))
                    date_expedition = datePlusJour(date,random.choice(range(10)))
                    date_livraison = datePlusJour(date_expedition,random.choice(range(30)))
                elif statut == "retourne" :
                    date_expedition = datePlusJour(date,random.choice(range(10)))
                    date_livraison = datePlusJour(date_expedition,random.choice(range(30)))
                    date_retour = datePlusJour(date_livraison,random.choice(range(90)))
                    remboursement.add((idPanier,isbn,date_retour))
                elif statut == "annule":
                    remboursement.add((idPanier,isbn,date))
                prod.write(str(idPanier) + "," + isbn + "," + quantite + "," +
                    statut + "," + date_restock + "," + date_expedition + "," +
                    date_livraison + "," + date_retour + "\n")
    return remboursement,livre

def setDemandeRemboursement(remboursement):
    raisons = ["defectueux","j'en veux plus","c'est nul","etc","...",""]
    with open("../CSV/demandeRemboursement.csv","w") as demande:
        demande.write("id_panier,isbn,date_demande,raison\n")
        for remb in remboursement:
            id = str(remb[0])
            isbn = remb[1]
            date = datePlusJour(remb[2],random.choice(range(5)))
            raison = random.choice(raisons)
            demande.write(id + "," + isbn + "," + date + "," + raison + "\n")

def getClientLivre(livre,commandes):
    ret = set()
    for l in livre:
        for c in commandes:
            if l[0] == c[0]:
                ret.add((c[2],l[1]))
    return ret

def setAvis(livre,commandes):
    livre = getClientLivre(livre,commandes)
    with open("../CSV/avis.csv","w") as avis:
        avis.write("mail,isbn,note,avis\n")
        for l in livre:
            mail = l[0]
            isbn = l[1]
            note = str(random.randint(0,20))
            av = random.choice(["Null","Bien","Incroyable","Parfait","..."])
            avis.write(mail + "," + isbn + "," + note + "," + av + "\n")

def creeCSV(nbClient,nbPanier):
    if not os.path.isdir("../CSV"): os.mkdir("../CSV")
    n,p,a = getNomPrenomAdress()
    mails,addresses = setClientCSV(nbClient,n,p,a)
    isbns = setMangaAuteurEditeurPrixCSV()
    commandes = setPanierCSV(mails,addresses,nbPanier)
    remboursement,livre = setProdPanierCSV(nbPanier,commandes,isbns)
    setDemandeRemboursement(remboursement)
    setAvis(livre,commandes)


if "__main__":
    os.chdir(os.path.dirname(__file__))
    creeCSV(nbClient=10000,nbPanier=2000)
