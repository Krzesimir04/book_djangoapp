
from book_app.views import *
from django.test import SimpleTestCase
from django.urls import reverse,resolve

class TestUrls(SimpleTestCase):
    
    def test_list_url(self):
        url=reverse('index')
        self.assertEqual(resolve(url).func,index)
    def test_login_url(self):
        url=reverse('login')
        self.assertEqual(resolve(url).func,login_view)