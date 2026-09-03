donnees = ["Omar", 25, "Casablanca", 15.5, True]

# affiche element and type 
for element in donnees :
    print(f"{element},{type(element)}")
    

#numbers of chaque type 
frequences={}
count=0
count_bool=0
count_numbers=0
for element in donnees :
    if type(element) == str:
        count+=1
    elif type(element)==bool:
        count_bool+=1
    else : 
        count_numbers+=1
print(f"number string is {count},number bool {count_bool},number of numbers {count_numbers}")

#nembers
numbers = []

for element in donnees:
    if type(element) == int or type(element) == float:
        numbers.append(element)

print(numbers)
