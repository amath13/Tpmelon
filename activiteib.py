

def F(nombre_pairs):
    list_pair = []
    for i in nombre_pairs:
        if i % 2 == 0:
            list_pair.append(i)
    return list_pair
mylist = [1,2,3,5,6,7,8,9,10]
nombre_pair = F(mylist)
print("ma liste:", mylist)
print("les nombres pars", nombre_pair)


import unittest

def F(nombre_pairs):
    list_pair = []
    for i in nombre_pairs:
        if i % 2 == 0:
            list_pair.append(i)
    return list_pair

class TestFonction(unittest.TestCase):

    def test_fonction(self):
        # Définir les entrées et les sorties attendues
        input_data = [1, 2, 3, 5, 6, 7, 8, 9, 10]
        expected_output = [2, 6, 8, 10]

        # Appeler la fonction que vous testez
        output = F(input_data)

        # Vérifier si la sortie correspond à ce qui est attendu
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()


