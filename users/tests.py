from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class TestPage(TestCase):
    def test_home_page_works(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/home-page.html')
        self.assertContains(response, 'HIS BLOG')

    def test_about_us_page_works(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'blog/new_about.html')