langages = ["Python", "Java", "JavaScript", "C++"]

#Ajoute
langages.append("PHP")
langages.append("SQL")
langages.insert(1,"C")

#Supprime
langages.remove("Java")
langages.pop()

print(langages)
print(len(langages))