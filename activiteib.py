import unittest

def F(nombre_pairs):
    list_pair = []
    for i in nombre_pairs:
        if i % 2 == 0:
            list_pair.append(i)
    return list_pair
# mylist = [1,2,3,5,6,7,8,9,10]
# nombre_pair = F(mylist)
# print("ma liste:", mylist)
# print("les nombres pars", nombre_pair)


class TestFonction(unittest.TestCase):

    def test_fonction(self):
        # Définir les entrées et les sorties attendues
        input_data = [1, 2, 3, 5, 6, 7, 8, 9, 10]
        expected_output = [2, 6, 8, 10]

        # Appeler la fonction que vous testez
        output = F(input_data)

        # Vérifier si la sortie correspond à ce qui est attendu
        self.assertEqual(output, expected_output)

    def test_liste_pairs(self): # definition d'une methode te test qui verifie les nombres pairs
        mylist = [1, 2, 3, 5, 6, 7, 8, 9, 10] # creation d'une liste avec des nombres pairs et impairs 
        nombre_pair = F(mylist) # appel de la fonction F avec la liste
        self.assertEqual(nombre_pair, [2, 6, 8, 10]) # verifie si la liste retournee contient les nombres pairs attendues

    def test_liste_vide(self):
        mylist = []
        nombre_pair = F(mylist)
        self.assertEqual(nombre_pair, [])

    def test_liste_sans_pairs(self):
        mylist = [1, 3, 5, 7, 9]
        nombre_pair = F(mylist)
        self.assertEqual(nombre_pair, [])

    def test_even_numbers(self): 
        input_list = [1, 2, 3, 5, 6, 7, 8, 9, 10]
        expected_output = [2, 6, 8, 10]
        self.assertEqual(F(input_list), expected_output)

    def test_empty_list(self):
        input_list = []
        expected_output = []
        self.assertEqual(F(input_list), expected_output)

    def test_no_even_numbers(self):# Cette méthode teste le comportement de la fonction F lorsque la liste d'entrée ne contient aucun nombre pair.
        input_list = [1, 3, 5, 7, 9]
        expected_output = []
        self.assertEqual(F(input_list), expected_output)

if __name__ == '__main__':
    unittest.main()
