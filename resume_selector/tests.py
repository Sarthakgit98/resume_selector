from django.test import TestCase
from django.test import Client

class ResumeSelectorTest(TestCase):

    def test_get(self):
        c = Client()
        response = c.get('/resume_selector/resume')
        print(response.content)
    
    def test_post(self):
        c = Client()
        response = c.post('/resume_selector/resume')
        print(response.content)
