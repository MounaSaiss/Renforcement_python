etudiants = [
    {"nom": "Omar", "age": 22, "note": 15},
    {"nom": "Sara", "age": 21, "note": 17},
    {"nom": "Yassine", "age": 23, "note": 9},
    {"nom": "Imane", "age": 20, "note": 13},
    {"nom": "Hamza", "age": 24, "note": 7}
]

print(etudiants[1])


#Afficher les étudiants admis/échec,
admis_list=[]
echec_list=[]
for etudiant in etudiants :
    if etudiant["note"] >= 10 :
        admis_list.append(etudiant)
    # print(etudiant["note"])
    else : 
        echec_list.append(etudiant)

print(admis_list)
print(echec_list)

# la moyenne de classe
total_note=0 
for etudiant in etudiants:
    total_note+=etudiant["note"]
    moyenne_note = total_note/len(etudiants)
# print(moyenne_note)

#l'étudiant ayant la meilleure note
max = 0 
for etudiant in etudiants:
    # print(etudiant["note"])
    if etudiant["note"]>max :
        max = etudiant["note"]
print(f"la note max est : {max},for student {etudiant["nom"]}")
