produit = {
    "nom": "Ordinateur", 
    "prix": 8500,
    "stock": 12, 
    "categorie":"Informatique"
}

# Modifier le prix à 7900
produit["prix"]=7900
print(produit)
# Ajouter "marque": "Lenovo"
produit ["marque"]="Lenovo"
produit["Disponible"]=True
print(produit)
#remove
produit.pop("categorie")
del produit["stock"]
print(produit)
