etudiant = {
    
    "nom": "Omar", 
    "age": 22,
    "formation": 
        {"nom": "Développement IA", 
        "niveau": "Avancé", 
        "duree": 12
        }
}

print(etudiant["formation"]["nom"])
niveau=etudiant["formation"]["niveau"]

etudiant["formation"]["niveau"]="Expert"

#Add new clé 
etudiant["technologies"]=["Python", "SQL", "Pandas", "MachineLearning"]

# print(etudiant)
