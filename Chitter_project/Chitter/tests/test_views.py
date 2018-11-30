from django.test import TestCase

class AboutPageTest(TestCase):

    def test_home_url_returns_status_code(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        
    def test_about_url_returns_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
