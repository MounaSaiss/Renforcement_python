notes = {"Python": 15, "SQL": 13, "JavaScript": 17, "Git": 14, "Linux": 12} 
#Affiche keys
keys = notes.keys()
print(keys)

#Affiche value 
values = notes.values()
print(values)
#items 
items = notes.items()
print(items)

# moyenne
Total_note = sum(values)
Moyenne_note=Total_note/len(values)
# print(Moyenne_note)
print(len(values))
# print(Total_note)

max_note=max(values)
# print(max_note)

min_note=min(values)
# print(min_note)
