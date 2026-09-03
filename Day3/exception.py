def diviser(a, b):
    try:
        resultat = a / b
        return resultat

    except ZeroDivisionError:
        print("division par zéro impossible")
        return 0

    except TypeError:
        print("les valeurs doivent être des nombres")
        return 0

    finally:
        print("Opération Done")


print(diviser(10, 2))
print(diviser(10, 0))
print(diviser(10, "2"))