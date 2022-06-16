import unittest
import avaliaçãodef as a

class Tests(unittest.TestCase):
    def test_maior(self):
        self.assertEqual(a.maior([8, 6, 2, 8, 8, 2, 9, -200]), 9)
        self.assertEqual(a.maior([500, 100, 900, 200, 150, 85]), 900)
        self.assertEqual(a.maior([-20, -96, -5, -96, -8]), -5)

    def test_ordena(self):
        self.assertEqual(a.ordena(2, 9, 6), [2, 6, 9])
        self.assertEqual(a.ordena(2, 6, 9), [2, 6, 9])
        self.assertEqual(a.ordena(9, 6, 2), [2, 6, 9])
        self.assertEqual(a.ordena(9, 2, 6), [2, 6, 9])
        self.assertEqual(a.ordena(6, 2, 9), [2, 6, 9])
        self.assertEqual(a.ordena(6, 9, 2), [2, 6, 9])

    def test_ocorrencia(self):
        self.assertEqual(a.ocorrencia(
            [2, 2, 2, 2, 2, 5, 9, 8, 5, 6, 8, 15, 6, 6], 2), 5)
        self.assertEqual(a.ocorrencia(
            [2, 2, 2, 2, 2, 5, 9, 8, 5, 6, 8, 15, 6, 6], 9), 1)
        self.assertEqual(a.ocorrencia(
            [2, 2, 2, 2, 2, 5, 9, 8, 5, 6, 8, 15, 6, 6], 8), 2)
        self.assertEqual(a.ocorrencia(
            [2, 2, 2, 2, 2, 5, 9, 8, 5, 6, 8, 15, 6, 6], 5), 2)
        self.assertEqual(a.ocorrencia(
            [2, 2, 2, 2, 2, 5, 9, 8, 5, 6, 8, 15, 6, 6], 6), 3)
        self.assertEqual(a.ocorrencia(
            [2, 2, 2, 2, 2, 5, 9, 8, 5, 6, 8, 15, 6, 6], 15), 1)
        self.assertEqual(a.ocorrencia(
            [2, 2, 2, 2, 2, 5, 9, 8, 5, 6, 8, 15, 6, 6], 26), 0)

    def test_limite(self):
        self.assertTrue(a.limite(2, 1, 5))
        self.assertTrue(a.limite(45, 45, 100))
        self.assertTrue(a.limite(100, 1, 100))
        self.assertFalse(a.limite(6, 1, 5))
        self.assertFalse(a.limite(10, 100, 200))

    def test_categoria(self):
        self.assertEqual(a.categoria(7), "Infantil A")
        self.assertEqual(a.categoria(10), "Infantil B")
        self.assertEqual(a.categoria(11), "Juvenil A")
        self.assertEqual(a.categoria(17), "Juvenil B")
        self.assertEqual(a.categoria(18), "Adulto")

    def test_mais_velho(self):
        matrix = [["João", 27],["Maria", 24],["Salomé", 40],["José", 72],["Bianca", 7]]
        self.assertEqual(a.mais_velho(matrix), "José")
        matrix = [["João", 27],["Maria", 80],["Salomé", 40],["José", 72],["Bianca", 7]]
        self.assertEqual(a.mais_velho(matrix), "Maria")

if __name__ == '__main__':
    unittest.main()