
import sqlite3
from pharmacie_package import client
from pharmacie_package import produit

conn=sqlite3.connect("pharmaciebd.db") #connexion a la base des donnees
curseur=conn.cursor()
#creation de la classe achat
class Achat:
    #initialialisation de la classe
    def __init__(self):
        self.dateachat = dateachat
        self.prodach = prodach
        self.montant_achat = montant_achat
        self.montfact = montfact
        self.nombrexemplaire = nombrexemplaire
        self.prixtotpro = prixtotpro
        self.id_client = id_client
        self.id_produit = id_produit
        type_client = type_client
        
    #Methode pour l enregistrement de l achat
    def EnregistrementAchat():
        #importation du module datetime pour l utilisation de la date
        from datetime import date
        #importation du module time pour l utilisation de l heure
        import time
        montant_achat = 0
        print("Type de Client:\n 1-client non assure\n 2-client employe assure\n 3-client employe non assure\n")
        type_Client = int(input("Veillez entrer le type de client: "))
        if type_Client in range(1,4):
            if type_Client == 1:           
                type_client = "client non assure"
                nbr_produit = int(input("Veiller entrer  le nombre de produit a achete: "))
                i = 1
                while i <= nbr_produit:     #condition si l utilisateur veux entrer plusieurs produits           
                    dateachat = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                    print("Produit",i)
                    AfficheTableProduit()
                    prodach = input("Veillez entrer le nom produit: ")
                    prix_produit = float(input("Veillez entrer le prix  du produit:  "))
                    nombrexemplaire = int(input("Veillez entrer le nombre d exemplaire du produit:  "))
                    prixtotpro = prix_produit*nombrexemplaire            
                    montant_achat += prixtotpro
                    idclient = int(input("Veillez entrer l identifianr du client qui achete:  "))
                    idproduit = int(input("Veillez entrer l identifiant du produit a achete:  "))
                    if montant_achat >= 50000:     #condition pour le calcule de la remise
                        montant_achat = montant_achat-(montant_achat*0.1)   #calcule de la remise de 10%                    
                        data=[(dateachat,heure_achat,produit_achat,montant_achat,prix_total_pro,nbr_exemplaire,id_client,id_produit,typeclient)]
                    else:
                        data=[(dateachat,prodach,montant_achat,prixtotpro,nombrexemplaire,idclient,idproduit,typeclient)]
                    for x in data:
                        curseur.execute("insert into achat(dateachat,prodach,montant_achat,prixtotpro,nombrexemplaire,idclient,idproduit,typeclient)values(?,?,?,?,?,?,?,?,?)",enreg)
                        conn.commit()
                        print("Achat Ajouter avec succes")
                    i +=1
                
            elif type_Client == 2:
                type_client = "client employe assure"
                type_produit = input("Entrer le type de produit 'parapharma': ")
                if type_produit == "parapharma":
                    nbr_produit = int(input("Veiller entrer  le nombre de produit a achete: "))
                i = 1
                while i <= nombreproduit:               
                    dateachat = datetime.datetime.today()
                    heure_achat = datetime.datetime.today()
                    print("Produit",i)
                    produit_achat = input("Veillez entrer le nom produit: ")
                    prix_produit = float(input("Veillez entrer le prix  du produit:  "))
                    nbr_exemplaire = int(input("Veillez entrer le nombre d exemplaire du produit:  "))
                    prix_total_pro = prix_produit*nbr_exemplaire            
                    montant_achat += prix_total_pro
                    montant_achat = montant_achat-(montant_achat*0.05)    #calcule de la remise de 5%
                    id_client = int(input("Veillez entrer l identifianr du client qui achete:  "))
                    id_prduit = int(input("Veillez entrer l identifiant du produit a achete:  "))
                    print("===Type de client===")
                    print("client non assure / client employe assure / client employe non assure / client assure")
                    type_client = input("Veillez Confirmer le type de client ")
                      
                    data=[(date_achat,heure_achat,produit_achat,montant_achat,prix_total_pro,nbr_exemplaire,id_client,id_prduit,type_client)]
                    for enreg in data:
                        curseur.execute("insert into achat(date_achat,heure_achat,produit_achat,montant_achat,prix_total_pro,nbr_exemplaire,id_client,id_prduit,type_client)values(?,?,?,?,?,?,?,?,?)",enreg)
                        conn.commit()
                        print("Achat Ajouter avec succes")
                    i +=1
            
            elif type_Client == 3:
                type_client = "client employe non assure"
                nbr_produit = int(input("Veiller entrer  le nombre de produit a achete: "))
                i = 1
                while i <= nbr_produit:               
                    dateachat = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                    print("Produit",i)
                    AfficheTableProduit()
                    prodachat = input("Veillez entrer le nom du produit: ")
                    prix_produit = float(input("Veillez entrer le prix  du produit:  "))
                    nombrexemplaire = int(input("Veillez entrer le nombre d exemplaire du produit:  "))
                    prixtotpro = prix_produit*nombrexemplaire            
                    montant_achat += prixtotpro
                    montant_achat = montant_achat-(montant_achat*0.05)
                    idclient = int(input("Veillez entrer l identifianr du client qui achete:  "))
                    idproduit = int(input("Veillez entrer l identifiant du produit a achete:  "))
                          
                    data=[(dateachat,prodach,montant_achat,prixtotpro,nombrexemplaire,idclient,idproduit,typeclient)]
                    for enreg in data:
                        curseur.execute("insert into achat(dateachat,prodach,montant_achat,prixtotpro,nombrexemplaire,idclient,idproduit,typeclient)values(?,?,?,?,?,?,?,?,?)",enreg)
                        conn.commit()
                        print("Achat Ajouter avec succes")
                    i +=1

            else:
                type_client = "client assure"
                nbr_produit = int(input("Veiller entrer  le nombre de produit a achete: "))
                i = 1
                while i <= nbr_produit:               
                    dateachat = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    print("Produit",i)
                    prodach = input("Veillez entrer le nom produit: ")
                    prix_produit = float(input("Veillez entrer le prix  du produit:  "))
                    nombrexemplaire = int(input("Veillez entrer le nombre d exemplaire du produit:  "))
                    prixtotpro = prix_produit*nbr_exemplaire            
                    montant_achat += prix_total_pro
                    idclient = int(input("Veillez entrer l identifianr du client qui achete:  "))
                    idproduit = int(input("Veillez entrer l identifiant du produit a achete:  "))
                      
                    data=[(date_achat,heure_achat,produit_achat,montant_achat,prix_total_pro,nbr_exemplaire,id_client,id_prduit,type_client)]
                    for enreg in data:
                        curseur.execute("insert into achat(date_achat,heure_achat,produit_achat,montant_achat,prix_total_pro,nbr_exemplaire,id_client,id_prduit,type_client)values(?,?,?,?,?,?,?,?,?)",enreg)
                        conn.commit()
                        print("Achat Ajouter avec succes")
                    i +=1
            
    def AfficheAchat(): 
        curseur.execute(" select * from achat where idclient")
        conn.commit()
        for i in curseur:
            print(i)
            print("")

    def AfficheClientAchat():
        curseur.execute(" select prenom, nom from client INNER JOIN achat ON achat.idclient = client.idclient")
        conn.commit()
        for i in curseur:
            print(i)

    def Visualisation():
        curseur.execute(" select prenom, nom from client INNER JOIN achat ON achat.typeclient LIKE  client.type")
        conn.commit()
        for i in curseur:
            print(i)
        
            curseur.close()    #fermeture du curseur
            conn.close()       #fermeture de la connexion

                

    



        
    
        


