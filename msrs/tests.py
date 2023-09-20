from django.test import TestCase, Client
from django.urls import reverse


class MsrTest(TestCase):
    def test_should_respond_only_for_example_a(self):
        client = Client(HTTP_HOST="www.example-a.dev")
        view = reverse("index")
        response = client.get(view)
        self.assertEqual(response.status_code, 200)
