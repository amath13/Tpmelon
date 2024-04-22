#Créer la fonction de reverse
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

#afficher la liste apré reverse
print(list_invert)

#importer unitest
import unittest

# Importer la fonction à tester depuis le fichier ou le code se trouve
from Exosalim.py import reverseOrdre

# Définir les cas de test
def test_reverseOrdre(self):
        # Cas de test avec une liste non vide
        self.assertEqual(reverseOrdre([1, 2, 3]), [3, 2, 1])
        # Cas de test avec une liste vide
        self.assertEqual(reverseOrdre([]), [])
        # Cas de test avec une liste contenant un seul élément
        self.assertEqual(reverseOrdre([5]), [5])
        # Cas de test avec une liste contenant des éléments de types différents
        self.assertEqual(reverseOrdre([1, 'a', 3.5]), [3.5, 'a', 1])
        # Cas de test avec une liste contenant des éléments dupliqués
        self.assertEqual(reverseOrdre([1, 2, 2, 3]), [3, 2, 2, 1])
        # Cas de test ou une partie des elemnets de la liste sont identiques
        self.assertEqual(reverseOrdre([1, 1, a, b, 1], [1, b, a, 1, 1]))
        
# Exécuter les tests
if __name__ == '__main__':
    unittest.main()