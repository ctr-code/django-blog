import datetime
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CollaborationForm
from .models import About


class TestAboutViews(TestCase):

    def setUp(self):
        self.about = About(title="About me", image="placeholder",
                           content="Sausages",
                           updated_on=datetime.datetime.now())
        self.about.save()

    def test_render_post_detail_page_with_comment_form(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About me", response.content)
        self.assertIn(b"nobody.jpg", response.content)
        self.assertIn(b"Sausages", response.content)
        self.assertIsInstance(
            response.context['collaboration_form'], CollaborationForm)
