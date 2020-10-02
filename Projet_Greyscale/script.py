# -*-coding:utf-8 *-*
import numpy as np
import matplotlib.pyplot as plt
import math
import random
from copy import *

def Entrainement(eta,listeMotif):
        N=len(listeMotif)
        taille=len(listeMotif[0].flatten())
        W=np.zeros((taille,taille))
        for i in range(N):
                W+=eta*np.outer(listeMotif[i].flatten(),listeMotif[i].flatten())
        W/=N
        return W
                
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
                motifBruite[x][y]=random.random()
        return motifBruite
        
def Rappel(W,dt,motif,temps):
        g = lambda r: np.tanh(r)
        time = np.arange(0,temps,dt)
        T = len(time)
        N= len(motif.flatten())
        y = np.zeros((T,N))
        y [0] = motif.flatten()
        
        for t in range(1,T):
            #print(np.dot(W, y[t-1]))
            y[t] = y[t-1]+ dt*( -y[t-1] + g(np.dot(W, y[t-1]) ) )
        return y

def Affichage(motifOriginal,matrice,W):
        plt.figure(1); plt.clf();
        plt.subplot(211)
        motifCompresseOriginal=DeBinarisation(motifOriginal)
        plt.imshow(motifCompresseOriginal)
        plt.title('Motif Original')
        plt.draw()
        NbIterations=len(matrice)/len(motifOriginal)
        for i in range(len(matrice)):
                plt.subplot(212); plt.cla()
                motifRappel=matrice[i].reshape(len(motifOriginal),len(motifOriginal))
                motifRappelCompresse=DeBinarisation(motifRappel)
                plt.imshow(motifRappelCompresse)
                plt.title('Rappel du motif')
                print("Iteration ", i)
                plt.draw()
                plt.pause(0.01)
        plt.show()
        

def LectureImage(fichier):
        matrix=plt.imread(fichier)
        matrix=np.array(matrix)
        return matrix
        
def Binarisation(matrice):
        matrice_Antoinisee=np.zeros((3*len(matrice),3*len(matrice[0])))
        for i in range(len(matrice)):
                for j in range(len(matrice)):
                        for k in range(int(matrice[i][j]*9)):
                                #print(k)
                                ligne=int(k/3)
                                col=k%3
                                matrice_Antoinisee[i*3+ligne][j*3+col]=1
        return matrice_Antoinisee

def DeBinarisation(matrice):
        matriceCompresse=np.zeros((int(len(matrice)/3),int(len(matrice[0])/3)))
        for i in range(len(matriceCompresse)):
                for j in range(len(matriceCompresse[0])):

                        matriceCompresse[i][j]=np.mean(matrice[i*3:i*3+3,j*3:j*3+3])
        return matriceCompresse
