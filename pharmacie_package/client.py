import sqlite3
class Client:
    def __init__(self):
        """initialiseur de la classe client"""
        self.nom = ""
        self.prenom = ""
        self.genre = ""
        self.adresse = ""
        self.tel = 0
        self.mail = ""

    def saisie_cli(self, data=[]):
        """Fonction de saisie et de recuperation des données du clients"""
        self.nom = input("Nom: ")
        self.prenom = input("Prenom: ")
        self.genre = input("Genre: ")
        self.adresse = input("Adresse: ")
        self.tel = int(input("Telephone: "))
        self.mail = input("E-mail: ")

        data = [(self.nom, self.prenom, self.genre, self.adresse, self.tel, self.mail)]
        return data

class ClientAssure(Client):
    def __init__(self):
        """initialiseur de la classe clientassure"""
        self.numpolice=""
        self.nomassureur=""
        self.datedebut=""
        self.datefin=""
        
    def saisie_clia(self,datac=[]):
        """Fonction de saisie et de recuperation des données du clients"""

        self.numpolice=input("Numero police assurance: ")
        self.nomassureur=input("Nom assurance: ")
        self.datedebut=input("Date debut assurance: ")
        self.datefin=input("Date fin assurance: ")
        datac=[(self.numpolice, self.nomassureur, self.datedebut, self.datefin)]
        return datac
    
class Manipulation:
    """Classe contenant les fonctions de manipulation des données du client"""
    def ajout_client(self):
        """Fonction pour ajouter un nouveau client"""
        c = Client()
        data = []
        donnees = c.saisie_cli(data)

        print("Client assuré?")
        print("1-oui    2-non")
        rep = int(input("reponse: "))
        if rep == 1:
            ca = ClientAssure()
            datac = []
            donneesca = ca.saisie_clia(datac)

            conn = sqlite3.connect("pharmaciebd.db")
            cur = conn.cursor()
            for x in donnees:
                cur.execute("""INSERT INTO client (nom,prenom,genre,adresse,tel,mail) VALUES(?,?,?,?,?,?)""", x)
            for y in donneesca:
                cur.execute("""INSERT INTO clientassure (numpolice,nomassureur,datedebut,datefin) VALUES(?,?,?,?)""",y )
            cur.execute("""SELECT idclient FROM client,clientassure WHERE idclient=idclient_fk""")
            conn.commit()
            cur.close()
            conn.close()

        elif rep == 2:
            print("Client bien enregistré")

            conn = sqlite3.connect("pharmaciebd.db")
            cur = conn.cursor()
            for x in donnees:
                cur.execute("""INSERT INTO client (nom,prenom,genre,adresse,tel,mail) VALUES(?,?,?,?,?,?)""", x)
            conn.commit()
            cur.close()
            conn.close()

    def modifier_client(self):
        """Fonction pour modifier les données d'un client"""
        idclient = input("Veuillez preciser l'identifiant du client à modifier: ")
        reps = input("Client assuré? ")
        if reps == "oui":
            print("Que voulez vous modifier?\n ", "1-Nom\n", "2-Prenom\n", "3-Genre\n", "4-Adresse\n", "5-Telephone\n",
                  "6-Mail\n", "7-Numero de police\n", "8-Nom assureur\n", "9-Date debut\n", "10-Date fin")
            modif = int(input("Tapez votre choix: "))

            if modif == 1:

                nom = input("Nom:")
                t = (nom, idclient)
                conn = sqlite3.connect("pharmaciebd.db")
                cur = conn.cursor()
                cur.execute("""UPDATE client SET nom=? WHERE idclient=?""", t)
                conn.commit()
                cur.close()
                conn.close()

            elif modif == 2:

                prenom = input("Prenom:")
                t = (prenom, idclient)
                conn = sqlite3.connect("pharmaciebd.db")
                cur = conn.cursor()
                cur.execute("""UPDATE client SET prenom=? WHERE idclient=?""", t)
                conn.commit()
                cur.close()
                conn.close()

            elif modif == 3:
                genre = input("Genre:")
                t = (genre, idclient)
                conn = sqlite3.connect("pharmaciebd.db")
                cur = conn.cursor()
                cur.execute("""UPDATE client SET genre=? WHERE idclient=?""", t)
                conn.commit()
                cur.close()
                conn.close()

            elif modif == 4:
                adresse = input("Adresse:")
                t = (adresse, idclient)
                conn = sqlite3.connect("pharmaciebd.db")
                cur = conn.cursor()
                cur.execute("""UPDATE client SET adresse=? WHERE idclient=?""", t)
                conn.commit()
                cur.close()
                conn.close()

            elif modif == 5:
                tel = input("Telephone:")
                t = (tel, idclient)
                conn = sqlite3.connect("pharmaciebd.db")
                cur = conn.cursor()
                cur.execute("""UPDATE client SET tel=? WHERE idclient=?""", t)
                conn.commit()
                cur.close()
                conn.close()

            elif modif == 6:
                mail = input("E-mail:")
                t = (mail, idclient)
                conn = sqlite3.connect("pharmaciebd.db")
                cur = conn.cursor()
                cur.execute("""UPDATE client SET mail=? WHERE idclient=?""", t)
                conn.commit()
                cur.close()
                conn.close()

            elif modif == 7:
                numpolice = input("Numero police:")
                t = (numpolice, idclient)
                conn = sqlite3.connect("pharmaciebd.db")
                cur = conn.cursor()
                cur.execute("""UPDATE clientassure SET numpolice=? WHERE idclient=?""", t)
                conn.commit()
                cur.close()
                conn.close()

            elif modif == 8:
                nomassureur = input("Nom assureur:")
                t = (nomassureur, idclient)
                conn = sqlite3.connect("pharmaciebd.db")
                cur = conn.cursor()
                cur.execute("""UPDATE clientassure SET nomassureur=? WHERE idclient=?""", t)
                conn.commit()
                cur.close()
                conn.close()

            elif modif == 9:
                datedebut = input("Date debut:")
                t = (datedebut, idclient)
                conn = sqlite3.connect("pharmaciebd.db")
                cur = conn.cursor()
                cur.execute("""UPDATE clientassure SET datedebut=? WHERE idclient=?""", t)
                conn.commit()
                cur.close()
                conn.close()

            elif modif == 10:
                datefin = input("Date fin:")
                t = (datefin, idclient)
                conn = sqlite3.connect("pharmaciebd.db")
                cur = conn.cursor()
                cur.execute("""UPDATE clientassure SET datefin=? WHERE idclient=?""", t)
                conn.commit()
                cur.close()
                conn.close()

        if reps=="non":

            print("Que voulez vous modifier?\n ", "1-Nom\n", "2-Prenom\n", "3-Genre\n", "4-Adresse\n", "5-Telephone\n","6-Mail\n")
            modif = int(input("Tapez votre choix: "))

            if modif == 1:

                nom = input("Nom:")
                t = (nom, idclient)
                conn = sqlite3.connect("pharmaciebd.db")
                cur = conn.cursor()
                cur.execute("""UPDATE client SET nom=? WHERE idclient=?""", t)
                conn.commit()
                cur.close()
                conn.close()

            elif modif == 2:

                prenom = input("Prenom:")
                t = (prenom, idclient)
                conn = sqlite3.connect("pharmaciebd.db")
                cur = conn.cursor()
                cur.execute("""UPDATE client SET prenom=? WHERE idclient=?""", t)
                conn.commit()
                cur.close()
                conn.close()

            elif modif == 3:
                genre = input("Genre:")
                t = (genre, idclient)
                conn = sqlite3.connect("pharmaciebd.db")
                cur = conn.cursor()
                cur.execute("""UPDATE client SET genre=? WHERE idclient=?""", t)
                conn.commit()
                cur.close()
                conn.close()

            elif modif == 4:
                adresse = input("Adresse:")
                t = (adresse, idclient)
                conn = sqlite3.connect("pharmaciebd.db")
                cur = conn.cursor()
                cur.execute("""UPDATE client SET adresse=? WHERE idclient=?""", t)
                conn.commit()
                cur.close()
                conn.close()

            elif modif == 5:
                tel = input("Telephone:")
                t = (tel, idclient)
                conn = sqlite3.connect("pharmaciebd.db")
                cur = conn.cursor()
                cur.execute("""UPDATE client SET tel=? WHERE idclient=?""", t)
                conn.commit()
                cur.close()
                conn.close()

            elif modif == 6:
                mail = input("E-mail:")
                t = (mail, idclient)
                conn = sqlite3.connect("pharmaciebd.db")
                cur = conn.cursor()
                cur.execute("""UPDATE client SET mail=? WHERE idclient=?""", t)
                conn.commit()
                cur.close()
                conn.close()


    def recherche_client(self):
        """Fonction pour chercher un client dans la base de données"""
        print("Veuillez preciser l'identifiant du client à rechercher: ")
        idclient = input("Identifiant: ")

        conn = sqlite3.connect("pharmaciebd.db")
        cur = conn.cursor()
        x = (idclient)
        cur.execute("""SELECT * from client WHERE idclient=?""", x)
        a = list(cur)
        conn.commit()
        cur.close()
        conn.close()
        print(a)

    def supprimer_client(self):
        """Fonction pour la suppression d'un client dans la base de données"""
        idclient = input("Veuillez preciser l'identifiant du client à supprimer: ")
        x = (idclient)
        conn = sqlite3.connect("pharmaciebd.db")
        cur = conn.cursor()
        cur.execute("""DELETE FROM client WHERE idclient=?""", x)
        conn.commit()
        cur.close()
        conn.close()


        
        
