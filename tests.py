import unittest
from app import app


class AppTestCase(unittest.TestCase):

    # Проверка, возвращает ли функция ответ вообще
    def test_response(self):
        with app.test_client() as client:
            response = client.post('/', data={'a': 1, 'b': 1, 'c': 1})
            self.assertEqual(response.status_code, 200)

    # Проверка решения уравнения с действительными корнями (для a=1, b=0, c=-4)
    def test_real_roots(self):
        with app.test_client() as client:
            response = client.post('/', data={'a': 1, 'b': 0, 'c': -4})
            self.assertIn(b'x1 = 2', response.data)
            self.assertIn(b'x2 = -2', response.data)

    # Проверка решения уравнения с отрицательным дискриминантом (без действительных корней)
    def test_complex_roots(self):
        with app.test_client() as client:
            response = client.post('/', data={'a': 1, 'b': 2, 'c': 2})
            self.assertIn(b'x1 = (-1+1j)', response.data)
            self.assertIn(b'x2 = (-1-1j)', response.data)


if __name__ == '__main__':
    unittest.main()
