from django.test import TestCase
from .forms import CollaborationForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborationForm({
            'name': 'Fred',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_form_missing_name(self):
        """ Test for all fields"""
        form = CollaborationForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Form missing name was accepted")

    def test_form_missing_email(self):
        """ Test for all fields"""
        form = CollaborationForm({
            'name': 'Fred',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(),
                         msg="Form missing email was accepted")

    def test_form_missing_message(self):
        """ Test for all fields"""
        form = CollaborationForm({
            'name': 'Fred',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(),
                         msg="Form missing message was accepted")
