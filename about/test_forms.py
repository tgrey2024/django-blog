from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_email_is_required(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Jon',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Email is missing")

    def test_name_is_required(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Name is missing")

    def test_message_is_required(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Mary',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg="Message is missing")
