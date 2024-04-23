def greater_number(x, y, z):
    # Comparer les trois nombres pour trouver le plus grand
    greater_number = x
    if y > greater_number:
        greater_number = y
    if z > greater_number:
        greater_number = z
    return greater_number
# Demander à l'utilisateur d'entrer trois nombres
x = float(input("Entrez le premier nombre : "))
y = float(input("Entrez le deuxième nombre : "))
z = float(input("Entrez le troisième nombre : "))
# Appeler la fonction pour trouver le plus grand nombre
result = greater_number(x, y, z)
print("Le plus grand nombre est :", result)
