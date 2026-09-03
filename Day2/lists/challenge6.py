#rechercheElement(30, L)  # Retourne: 2
#rechercheElement(100, L) # Retourne: False

L = [10, 20, 30, 40, 50]



def rechercheElement(element, liste):
    for el in liste : 
        if el == element:
            return liste.index(element)


print(rechercheElement(30, L))
print(rechercheElement(100, L))