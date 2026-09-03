# 🎯 Objectif :
#  Transformer des données textuelles et les analyser.
# A partir de 2 textes, transformer chaque texte en liste de mots (
# Convertir en minuscules et éliminer les mots de 3 lettres ou moins.
# Comparer les listes et identifier les mots communs. 

texte1 = "Mouna hello girl okey "

texte2 = "Python is facile language"


# text to list 
liste1 = texte1.lower().split()
liste2 = texte2.lower().split()

print(liste1)
print(liste2)


# delete moins 3 lettres 
liste1 = [mot for mot in liste1 if len(mot) > 3]
liste2 = [mot for mot in liste2 if len(mot) > 3]

print(liste1)
print(liste2)


# mots communs
mots_communs = []
for mot in liste1 :
    if mot in liste2 :
        mots_communs.append(mot)

print( mots_communs)

