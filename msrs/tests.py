from django.test import TestCase, Client, tag
from django.urls import reverse


# Remove this tag when test passes
class MsrTest(TestCase):
    @tag("skip")
    def test_should_respond_only_for_example_a(self):
        client = Client(HTTP_HOST="www.example-a.dev")
        view = reverse("index")
        response = client.get(view)
        self.assertEqual(response.status_code, 200)
