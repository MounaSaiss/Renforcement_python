def compute_list_sum(numbers):
    somme = 0

    for nombre in numbers:
        if nombre % 2 == 0:
            somme += nombre

    return somme


print(compute_list_sum([1, 2, 3, 4, 5]))
print(compute_list_sum([2, 6, 8]))
print(compute_list_sum([1, 3, 5]))
print(compute_list_sum([10, 15, 20, 25]))