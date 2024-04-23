# Créer la fonction de reverse
def reverseOrdre(list):
    inv = []
    i = len(list)-1
    while i >= 0:
        inv.append(list[i])
        i -= 1
    return inv

# définir la liste a reverser
list = [1, 2, 3, 4, 5]
list_invert = reverseOrdre(list)

# afficher la liste apré reverse
print(list_invert)