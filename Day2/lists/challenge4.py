temperatures = [18, 25, 31, 14, 27, 35, 22, 19, 30, 12, 28]

#temp max than 25 
temp_max=[]
for temp in temperatures : 
    if temp > 25 : 
        temp_max.append(temp)
print(temp_max)

#temp min than 25 
temp_min=[]
for temp in temperatures : 
    if temp <= 25 : 
        temp_min.append(temp)
print(temp_min)

#temp entre 20 et 30
temp_list=[]
for temp in temperatures : 
    if 20 <= temp <= 30  : 
        temp_list.append(temp)
print(temp_list)

#compteur 
i = 0 
for temp in temperatures : 
    if temp > 30 :
        i+=1
print(i)