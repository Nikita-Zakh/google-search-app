import unittest
from services.google_service import get_google_results
from app import app

class TestGoogleService(unittest.TestCase):

    def test_get_google_results(self):
        results = get_google_results("Mr. Robot")
        self.assertIsInstance(results, list)
        if results:
            self.assertIn("title", results[0])
            self.assertIn("link", results[0])

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_get(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        # kontrolujeme, že záhlaví je v odpovědi
        self.assertIn("Google Search", response.data.decode("utf-8"))

    def test_home_post(self):
        response = self.app.post("/", data=dict(query="Mr. Robot"))
        self.assertEqual(response.status_code, 200)
        # kontrolujeme, že jsou výsledky
        self.assertIn("Výsledky", response.data.decode("utf-8"))

if __name__ == "__main__":
    unittest.main()