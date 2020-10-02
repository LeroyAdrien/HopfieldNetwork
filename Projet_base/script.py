# -*-coding:utf-8 *-*
import numpy as np
import matplotlib.pyplot as plt
import math
import random
from copy import *


                                                      #Crée les matrices utilisées lors du projet 
def Matrix_Creation():
        mat1=np.array([[-1,-1,-1,-1, 1],
                      [ 1,-1, 1, 1,-1],
                      [ 1,-1, 1, 1,-1],
                      [ 1,-1, 1, 1,-1],
                      [ 1,-1,-1,-1, 1]])
                      
        mat2=np.array([[-1,-1,-1,-1,-1],
                      [ 1, 1, 1,-1, 1],
                      [ 1, 1, 1,-1, 1],
                      [-1, 1, 1,-1, 1],
                      [-1,-1,-1, 1, 1]])
                      
        mat3=np.array([[ 1,-1,-1,-1,-1],
                      [-1, 1, 1, 1, 1],
                      [-1, 1, 1, 1, 1],
                      [-1, 1, 1, 1, 1],
                      [ 1,-1,-1,-1,-1]])
                      
        mat4=np.array([[-1, 1, 1, 1,-1],
                      [-1,-1, 1,-1,-1],
                      [-1, 1,-1, 1,-1],
                      [-1, 1, 1, 1,-1],
                      [-1, 1, 1, 1,-1]])
                      
        mat5=np.array([[ 1,-1, 1,-1, 1],
                      [-1, 1,-1, 1,-1],
                      [ 1,-1, 1,-1, 1],
                      [-1, 1,-1, 1,-1],
                      [ 1,-1, 1,-1, 1]])
                      
        mat6=np.array([[ 1,-1,-1,-1, 1],
                      [-1, 1, 1, 1, 1],
                      [ 1,-1,-1,-1, 1],
                      [ 1, 1, 1, 1,-1],
                      [ 1,-1,-1,-1, 1]])
              
        return mat1,mat2,mat3,mat4,mat5,mat6
                                                      #Effectue l'entrainenemnt hebbien des poids synaptiques du réseau'
def Entrainement(eta,listeMotif):
        N=len(listeMotif)
        taille=len(listeMotif[0].flatten())
        W=np.zeros((taille,taille))
        for i in range(N):
                W+=eta*np.outer(listeMotif[i].flatten(),listeMotif[i].flatten())
        W/=N
        return W
                
                                                      #Bruite les motifs pour le rappel'
def Bruitage(motif,m):
        motifBruite=deepcopy(motif)
        taille = len(motif)
        N=len(motif.flatten())
        listeCoordonnee=[i for i in range(N)]
        for i in range(m):
                choix=random.choice(listeCoordonnee)
                listeCoordonnee.remove(choix)
                x=int(choix/taille)
                y=choix%taille
                motifBruite[x][y]=motif[x][y] * -1
        return motifBruite
                                                      #Effectue par descente de gradient le rappel du motif appris
def Rappel(W,dt,motif,temps):
        g = lambda r: np.tanh(r)
        time = np.arange(0,temps,dt)
        T = len(time)
        N= len(motif.flatten())
        y = np.zeros((T,N))
        y [0] = motif.flatten()
        
        for t in range(1,T):
            y[t] = y[t-1]+ dt*( -y[t-1] + g(np.dot(W, y[t-1]) ) )
        return y
                                                      #Calcul l'erreur de rappel entre le pixel remémoré et le pixel d'origine'
def Erreur(motifTrouve,motifOriginal):
        somme=0
        for i in range(len(motifTrouve)):
                for j in range(len(motifTrouve[0])):
                        somme+=abs(motifTrouve[i,j]-motifOriginal[i,j])
        return somme/2

                                                      #Cree l'animation de rappel du pixel d'intérêt
def Affichage(motifOriginal,matrice,W):
        
        plt.figure(1); plt.clf();
        
        plt.subplot(311)
        plt.imshow(motifOriginal)
        plt.title('Motif Original')
        plt.draw()
        
        plt.subplot(312); plt.cla()
        plt.imshow(W)
        plt.title('Matrice de poids')
        plt.draw()
        
        input("\n Appuyer sur Entrée \n")
        
        NbIterations=len(matrice)/len(motifOriginal)
        for i in range(len(matrice)):
                plt.subplot(313); plt.cla()
                plt.imshow(matrice[i].reshape(len(motifOriginal),len(motifOriginal)))
                plt.title("Matrice Remémorée")
                #plt.title('Rappel du motif')
                print("Iteration ", i)
                plt.draw()
                plt.pause(0.001)
        plt.show()

                                                      #Calcule l'erreur moyenne pour un niveau de bruit donnée '
def ErreurMoyenne(listeMotif,N,mMax,seuilBruit):
        listeErreur=[]
        for m in range(mMax):
                ErreurBruit=0
                for i in range(100):
                        choix=np.random.choice(len(listeMotif), N, replace=False)
                        matriceEtudies=[listeMotif[x] for x in choix]
                        matriceOrigine=random.choice(matriceEtudies)
                        W=Entrainement(1,matriceEtudies)
                        mat1Bruite=Bruitage(matriceOrigine,m)
                        y=Rappel(W,0.1,mat1Bruite,10)
                        ErreurBruit+=Erreur(y[-1].reshape(len(listeMotif[0]),len(listeMotif[0])),matriceOrigine)
                listeErreur.append(ErreurBruit/100)
                if m==seuilBruit and ErreurBruit/100>=1:
                        Inf1=False
                elif m==seuilBruit and ErreurBruit/100<1:
                        Inf1=True
        return listeErreur,Inf1
                                                      #Calcule l'erreur moyenne pour plusieurs niveaux de bruit, pour plusieurs motifs mémorisés
def Question2(listeMotif,nint,nMax,seuilBruit):
	matriceErreur=[]
	listeInf1=[]
	for N in range(nint,len(listeMotif)+1):
		listeErreur,inf1=ErreurMoyenne(listeMotif,N,nMax,seuilBruit)
		matriceErreur.append(listeErreur)
		listeInf1.append(inf1)
                
	return matriceErreur,listeInf1



