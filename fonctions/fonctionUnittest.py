import unittest
def carre(x):
        return x**2
class CarreTestCase(unittest.TestCase):
            test_values=((2,4),(6,36),(5,20))
            def test_carre(self):
                    for nombre, nombre2 in self.test_values:
                            self.assertEqual(nombre2,carre(nombre))
if __name__=='__main__':
        unittest.main()