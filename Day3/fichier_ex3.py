def calculer_carre(nombre):
    if type(nombre) != int and type(nombre) != float:
        raise TypeError("Le paramètre doit être un nombre")
    if nombre < 0:
        raise ValueError("nombre est négatif")

    return nombre ** 2


#nombre positif
try:
    print(calculer_carre(4))
except (TypeError, ValueError) as erreur:
    print("Erreur :", erreur)

# pas un nombre
try:
    print(calculer_carre("quatre"))
except (TypeError, ValueError) as erreur:
    print("Erreur :", erreur)

#nombre négatif
try:
    print(calculer_carre(-2))
except (TypeError, ValueError) as erreur:
    print("Erreur :", erreur)

print("Le programme Done")