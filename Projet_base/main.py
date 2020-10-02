# -*-coding:utf-8 *-*
from script import *
import numpy as np
import matplotlib.pyplot as plt

                                                      #Génère la Figure 2 du rapport 
def RepresentationQ1(listeMotif):
        matrice,trash=ErreurMoyenne(listeMotif,1,int(len(listeMotif[0].flatten())/2)+1,6)
        plt.figure(figsize=(10,5))
        plt.plot(np.arange(0,13),matrice)
        plt.ylim(0,0.01)
        plt.xlabel('Bruit (nombre de pixels inversés)')
        plt.ylabel('Erreur moyenne e')
        plt.title('Erreur moyenne de rappel du réseau pour un motif mémorisé en fonction du bruit de départ ')
        plt.show()
                                                      #Génère la figure 3 du rapport 
def RepresentationQ2(listeMotif):
        matrice,listeinf1=Question2(listeMotif,2,int(len(listeMotif[0].flatten())/2),6)
        plt.figure(figsize=(10,5))
        for i in range(len(matrice)):
                plt.plot(np.arange(0,12),matrice[i],'o-',label='Motifs mémorisés: '+str(i+2))
        plt.legend()
        plt.title('Erreur moyenne de rappel du motif en fonction du nombre de motifs mémorisés et du bruit de départ')
        plt.xlabel('Bruit de départ (nombre de pixels inversés)')
        plt.ylabel('Erreur Moyenne e')
        
        plt.show()
        print("Nombre de motif maximum sauvegardé avec un bruit de 6:",np.max(np.where(np.array(listeinf1)==True))+2)
        return matrice
                                                      #Génère la figure 4 du rapport 
def RepresentationDifference6(listeMotif,listeMotifsix):
    erreurWO6=RepresentationQ2(listeMotif)[2:]
    erreurW6=RepresentationQ2(listeMotifsix)[2:-1]
    couleurs=['green','red','purple']
    plt.figure(figsize=(10,5))
    for i in range(len(erreurW6)):
        plt.plot(np.arange(0,12),erreurWO6[i],'o--',color=couleurs[i],label="Motifs (sans 6): "+str(i+4))
        plt.plot(np.arange(0,12),erreurW6[i],'o-',color=couleurs[i],label="Motifs (avec 6): "+str(i+4))
    plt.legend()
    plt.title("Variation de Rappel en fonction des motifs choisis ")
    plt.xlabel("Bruit de départ (nombre de pixels inversés)")
    plt.ylabel("Erreur Moyenne e")
    plt.show()
                                                      #Calcul de la capacité du réseau
def RepresentationQ3(listeMotif):
        trash,listeinf1=Question2(listeMotif,1,1,0)
        Nmax=(np.max(np.where(np.array(listeinf1)==True))+1)
        print("Complexité du réseaux:",Nmax/len(listeMotif[0].flatten())) 
        return Nmax/len(listeMotif[0].flatten())
        
                                                      #Moyenne du calul de la capacitédu réseau en fonction des motifs sélectionnés.
def RepresentationQ3Moyenne(listeMotif):
        complexite=[]
        for i in range(100):
                complexite.append(RepresentationQ3(listeMotif))
        complexite=np.array(complexite)
        print("Complexité Moyenne:",np.mean(complexite))
        return np.mean(complexite)
        
                

if __name__=="__main__":
                                                      #Création des structures pour le calcul
    mat1,mat2,mat3,mat4,mat5,mat6=Matrix_Creation()
    
    matriceOrigine=mat1
    listeMotif=[mat1,mat2,mat3,mat4,mat5]
    listeMotifsix=[mat1,mat2,mat3,mat4,mat5,mat6]
    
                                                      #Affichage du rappel (pour 5 motifs)
    """
    W=Entrainement(1,listeMotif)
    mat1Bruite=Bruitage(matriceOrigine,6)
    
    plt.figure()
    plt.subplot(211)
    plt.imshow(mat1)
    plt.title("Matrice d'origine")
    plt.subplot(212)
    plt.imshow(mat1Bruite)
    plt.title("Matrice bruitée")
    plt.show()
    y=Rappel(W,0.1,mat1Bruite,10)
    Affichage(matriceOrigine,y,W)
    """
                                                      #Représentation des figures du rapport et des résultats
    RepresentationQ1(listeMotif)
    RepresentationQ2(listeMotifsix)
    #RepresentationDifference6(listeMotif,listeMotifsix)
    RepresentationQ3(listeMotifsix)
    #RepresentationQ3Moyenne(listeMotifsix)

    
	
