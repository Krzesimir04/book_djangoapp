from django.test import TestCase,Client
from django.urls import reverse
from book_app.models import *

class TestView(TestCase):
    def setUp(self):
        self.client=Client()
        self.list_url=reverse('index')
        self.detail_url=reverse('reservation_2',args=['2020-20-02'])
      
    def test_project_list_GET(self):
        response=self.client.post(self.list_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'index.html')
    
    
    def test_register(self):
        response=self.client.post('/register',{'email':'mama@wp.pl','password1':'zaq1@WSX','password2':'zaq1@WSX','username':'mama'})
        self.assertEqual(response.status_code, 302)
        response=self.client.get('/register')
        self.assertEqual(response.status_code,200)