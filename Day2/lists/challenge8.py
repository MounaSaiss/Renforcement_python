L = [7, 23, 5, 23, 7, 19, 23, 12, 29, 7, 5]

frequences = {}

for el in L:
    if el in frequences:
        frequences[el] += 1
    else:
        frequences[el] = 1

for el,frequence in frequences.items():
    print(f"{el},{frequence}")
    

