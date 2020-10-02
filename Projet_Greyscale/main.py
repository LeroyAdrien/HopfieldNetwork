# -*-coding:utf-8 *-*
from script import *
import numpy as np
import matplotlib.pyplot as plt
import sys
np.set_printoptions(threshold=sys.maxsize)

if __name__=="__main__":
        
        matCat=LectureImage('./cat.png')
        matDog=LectureImage('./dog.png')
        
                                              #Binarisation des images 
        matCatTest=Binarisation(matCat)
        matDogTest=Binarisation(matDog)
        
                                              #Bruitage de l'image'
        matCatTestBruite=Bruitage(matCatTest,int(0.25*(len(matCatTest)*len(matCatTest[0]))))
        
        listeMotif=[matCatTest,matDogTest]
        
        
        W=Entrainement(1,listeMotif)
        y=Rappel(W,0.1,matCatTestBruite,10)
        
                                              #Affichage des images d'origine et bruitées'
        plt.figure(figsize=(5,9))
        
        plt.subplot(311)
        plt.imshow(matCat)
        plt.title("Matrice d'origine")

        plt.subplot(312)
        plt.imshow(matCatTest)
        plt.title("Matrice Binarisée")

        plt.subplot(313)
        plt.imshow(matCatTestBruite)
        plt.title("Matrice binarisée bruitée")
        plt.show()
        
                                              #Animation du rappel
        Affichage(matCatTest,y,W)

