import datetime
from django.urls import reverse
from django.test import TestCase
from .forms import CollaborationForm
from .models import About, CollaborationRequest


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

    def test_successful_collaboration_request(self):
        """Test for posting a collaboration request"""
        post_data = {
            'name': 'John Smith',
            'email': 'john@smith.com',
            'message': 'gizza job!',
        }
        response = self.client.post(reverse(
            'about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Your collaboration message has been received and will be seen',
            response.content
        )
        # Check the request was created in the database
        self.assertEqual(CollaborationRequest.objects.all().count(), 1)
        request = CollaborationRequest.objects.first()
        self.assertEqual(post_data['name'], request.name)
        self.assertEqual(post_data['email'], request.email)
        self.assertEqual(post_data['message'], request.message)
        self.assertEqual(request.read, False)
