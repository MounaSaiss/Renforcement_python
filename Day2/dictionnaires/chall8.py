ventes = [
    {"produit": "PC", "categorie": "Informatique", "prix": 8000, "quantite": 2},
    {"produit": "Souris", "categorie": "Accessoire", "prix": 150, "quantite": 10},
    {"produit": "Clavier", "categorie": "Accessoire", "prix": 300, "quantite": 5},
    {"produit": "PC", "categorie": "Informatique", "prix": 8000, "quantite": 1},
    {"produit": "Écran", "categorie": "Informatique", "prix": 2500, "quantite": 3}
]

for i in range(0,len(ventes)):
    print(ventes[i])
    
# Nombre total de ventes
total_vente=0
for vente in ventes: 
    # print(vente["quantite"])
    total_vente+=vente["quantite"]
print(f"Quantité total vendu est : {total_vente}")

# Chiffre d'affaires (CA) total
total_ca = 0 
for vente in ventes :
    total_ca+=vente["prix"]*vente["quantite"]
print(f"chiffre d'affaire totale est : {total_ca}")

# Produit le plus cher
max_price=0
for vente in ventes : 
    if max_price < vente["prix"]:
        max_price=vente["prix"]
print(f"max price is {max_price}, for {vente["produit"]} product ")

# Chiffre d'affaires par produit
for vente in ventes :
    CA=vente["prix"]*vente["quantite"]
    print(f"chiffre d'affaire de {vente["produit"]} est : {CA}")

#Nombre de produits par catégorie
