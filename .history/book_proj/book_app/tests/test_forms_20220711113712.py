from django.test import TestCase
from book_app.forms import *

class TestFormLogin(TestCase):
    def setUp(self):
        self.email='mamaa@wp.pl'
        self.password='zaq1@WSX'
    def testformTest(self):
        form=Login_form(data={'email':self.email,'password':self.password})

        self.assertTrue(form.is_valid())
        
    def testformLoginNoData(self):
        form=Login_form(data={})

        self.assertFalse(form.is_valid())
        print(form.errors)
        self.assertEqual(len(form.errors),2)