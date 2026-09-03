nom = input("Taper votre  nom : ")
salaire = input("Taper votre salaire horaire : ") 
heure = input(" Taper le nombre d'heures travaillées : ") 


if heure <= 40  : 
    Salaire_Totale = salaire * heure 
else 
    Salaire_Totale = (40 * salaire)+(heure-40)*salaire*1.5

print(f"Votre Slaire Totale est : {Salaire_Totale}")





