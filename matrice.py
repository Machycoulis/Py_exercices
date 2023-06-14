import numpy as np

# FONCTION MATRICE
print("FONCTION MATRICE")

m = int(input("Nombre de lignes: "))
n = int(input("Nombre de colonnes: "))

mat = (np.zeros((m, n)))

def matrice():
    print(mat)
    return matrice
matrice()

#FONCTION MATRICE CHANGE

print("Coordonnées de la valeur à changer:")
x = int(input("Ligne :"))
y = int(input("Colonne :"))
val_chg = int(input("Valeur à donner: "))
def change_valeur():
    mat[y, x] = val_chg
    return matrice()

change_valeur()

#MATRICE IDENTITE

def matrice_id():
    return(np.identity(int(input("Taille de la matrice identité: "))))

def print_matrice():
    print(matrice_id())

print_matrice()
