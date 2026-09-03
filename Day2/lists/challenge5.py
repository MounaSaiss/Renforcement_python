scores = [45, 12, 78, 34, 90, 23, 67, 56, 89, 10]
#list principale 
print(scores)

#copy 
copy_list=scores.copy()
print(copy_list)

#croissant
scores.sort()
print(scores)

#décroissante 
copy_list.sort(reverse = True)

print(copy_list)

#3max
max_scores = copy_list[0:3]
print(max_scores)








