import sqlite3
from pharmacie_package import client
from pharmacie_package import achat
from pharmacie_package import produit


print("Menu principale:")
print(" 1- Gerer client\n","2- Gerer produit\n","3- Details achats du client\n","4- Etat des ventes\n")

try:
        choix=int(input("Entrez votre choix: "))
        if choix in range(1,6):
                
            if choix==1:
                    print("1- Ajouter client\n","2- Modifier client\n","3-Rechercher client\n","4-Supprimer client")
                    gc=int(input("Entrez votre choix: "))
                        
                    if gc==1:
                        #ajouter un nouveau client

                        m=client.Manipulation()
                        m.ajout_client()

                    if gc==2:
                            #modifier client
                            m=client.Manipulation()
                            m.modifier_client()

                    if gc==3:
                            #rechercher client
                            m=client.Manipulation()
                            m.recherche_client()

                    if gc==4:
                            #supprimer client
                            m=client.Manipulation()
                            m.supprimer_client()


                                    
                     
                            
            elif choix==2:
                print("1- Ajouter produit\n","2- Modifier produit\n","3-Rechercher produit\n","4-Supprimer produit")
                gp=int(input("Entrez votre choix: "))
                if gp==1:
                    #ajout produit
                    mp=produit.Manipulationp()
                    mp.ajout_prod()

                elif gp==2:
                    #modifier produit
                    mp=produit.Manipulationp()
                    mp.modifier_prod()

                elif gp==3:
                    #rechercher produit
                    mp=produit.Manipulationp()
                    mp.recherche_prod()


                elif gp==4:
                    #supprimer produit
                    mp=produit.Manipulationp()
                    mp.supprimer_prod()


            elif choix==3:
                #enregistrer achat
                print ("")
                print("moi")
            elif choix==5:
                    print("toi")
except ValueError:
    print("La valeur saisie n'est pas bonne")
