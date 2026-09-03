notes = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]

print(notes)

Total_note = sum(notes)
print(Total_note)

Moyenne_note=Total_note/len(notes)
print(Moyenne_note)

#filltrage max au moyenne 
newlist=[]

for note in notes : 
    if note>Moyenne_note : 
        newlist.append(note)

print(newlist)

#filltrage min au moyenne
newlist_min = []
for note in notes : 
    if note < Moyenne_note : 
        newlist_min.append(note)
print(newlist_min)

#max note
max_note=max(notes)
print(max_note)

#min note
min_note=min(notes)
print(min_note)

#sup à dix 
i=0 
for note in notes : 
    if note > 10 :
        i+=1

print(i)
    
