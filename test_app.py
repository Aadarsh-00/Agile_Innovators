class FlaskTest(unittest.TestCase):
    def test_hello(self):
        tester = app.test_client(self)
        response = tester.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Hello,\n\nDevOps!")

if __name__ == '__main__':
    unittest.main()
