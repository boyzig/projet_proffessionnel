"""Module pour la gestion des produits"""
import sqlite3

class Produit():

    def __init__(self):
        """Initialiseur des variables de la classe produit"""
        self.nomprod=""
        self.prix=0.0
        self.prisencharge=""
        self.types=""

    def saisie_produit(self,datap=[]):
        """Fonction de saisie et de recuperation des valeurs des variables"""
        self.nomprod=input("Nom produit: ")
        self.prix=float(input("Prix: "))
        self.prisencharge=bool(input("Pris en charge?(vrai/faux): "))
        self.types=input("Type produit: ")
        datap=[(self.nomprod, self.prix, self.prisencharge, self.types)]
        return datap

class Manipulationp:
    """Classe contenant toutes les fonctions de manipulation des variables et des données relatifs aux produits"""

    def ajout_prod(self):
        """Cette fonction permet de gerer les ajouts de produits """

        p = Produit()
        datap = []
        donneesp = p.saisie_produit(datap)
        conn = sqlite3.connect("pharmaciebd.db")
        cur = conn.cursor()
        for x in donneesp:
            cur.execute("""INSERT INTO produit (nomprod,prix,prisencharge,types) VALUES(?,?,?,?)""", x) #insertion des données das la base
            conn.commit()
            cur.close()
            conn.close()

    def modifier_prod(self):
        """Cette fonction gère les modifications des produits dans la base de données"""
        idprod = input("Veuillez preciser l'identifiant du produit: ")
        print("Que voulez vous modifier?\n ", "1-Nom produit\n", "2-Prix produit\n", "3-Prise en charge\n", "4-Type\n")
        modifp = int(input("Tapez votre choix: "))

        if modifp == 1:
            nomprod = input("Nom produit:")
            t = (nomprod, idprod)
            conn = sqlite3.connect("pharmaciebd.db")
            cur = conn.cursor()
            cur.execute("""UPDATE produit SET nomprod=? WHERE idprod=?""", t)
            conn.commit()
            cur.close()
            conn.close()

        elif modifp == 2:
            prix = input("Prix produit:")
            t = (prix, idprod)
            conn = sqlite3.connect("pharmaciebd.db")
            cur = conn.cursor()
            cur.execute("""UPDATE produit SET prix=? WHERE idprod=?""", t)
            conn.commit()
            cur.close()
            conn.close()

        elif modifp == 3:
            prisencharge = input("Prise en charge:")
            t = (prisencharge, idprod)
            conn = sqlite3.connect("pharmaciebd.db")
            cur = conn.cursor()
            cur.execute("""UPDATE produit SET prisencharge=? WHERE idprod=?""", t)
            conn.commit()
            cur.close()
            conn.close()

        elif modifp == 4:
            types = input("Type produit:")
            t = (types, idprod)
            conn = sqlite3.connect("pharmaciebd.db")
            cur = conn.cursor()
            cur.execute("""UPDATE produit SET types=? WHERE idprod=?""", t)
            conn.commit()
            cur.close()
            conn.close()

    def recherche_prod(self):
        """Fonction pour la recherche d'un produt"""
        print("Veuillez preciser l'identifiant du produit à rechercher: ")
        idprod = input("Identifiant: ")

        conn = sqlite3.connect("pharmaciebd.db")
        cur = conn.cursor()
        x = idprod
        cur.execute("""SELECT * from produit WHERE idprod=?""", x)
        a = list(cur)
        conn.commit()
        cur.close()
        conn.close()
        print(a)

    def supprimer_prod(self):
        """Fonction pour la suppression d'un produit"""
        idprod = input("Veuillez preciser l'identifiant du produit à supprimmer: ")
        x = idprod
        conn = sqlite3.connect("pharmaciebd.db")
        cur = conn.cursor()
        cur.execute("""DELETE FROM produit WHERE idprod=?""", x)
        conn.commit()
        cur.close()
        conn.close()