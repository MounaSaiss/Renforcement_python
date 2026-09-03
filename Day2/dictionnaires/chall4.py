notes_etudiants = {"Omar": 15, "Sara": 8, "Yassine": 17, "Imane": 11, "Hamza": 6, "Nadia": 14}
# obj= notes_etudiants.items()
# print(obj)
sup=[]
inf=[]
for item in notes_etudiants:
    # print(notes_etudiants[item])
    if notes_etudiants[item] > 10 :
        sup.append(item)
    else :
        inf.append(item)
    
print(sup)
print(inf)

student_Admis = len(sup)
all_student = len(notes_etudiants)
avg_réussit = (student_Admis/all_student)*100

print(avg_réussit)
# print(student_Admis)
# print(all_student)


