# compterOccurrences(23, L) # 3
# compterOccurrences(7, L)  # 2
# compterOccurrences(100, L)# 0


L = [7, 23, 5, 23, 7, 19, 23, 12, 29]

def compterOccurrences(element, liste):
    compteur = 0
    for el in liste:
        if el == element:
            compteur += 1
    
    return compteur

print(compterOccurrences(23, L) )
print(compterOccurrences(7, L))


