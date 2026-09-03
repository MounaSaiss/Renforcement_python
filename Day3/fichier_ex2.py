liste1 = [1, 2, 3, 4, 5]

# Calculer le carré de chaque élément
liste2 = []

for nombre in liste1:
    liste2.append(nombre ** 2)

# Ajouter un nouvel élément
liste2.append(36)

try:
    assert len(liste1) == len(liste2)
except AssertionError:
    print("Attention les 2 listes n'ont pas la même taille")