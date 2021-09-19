from school.models import Parent
from django.test import TestCase
from rest_framework.reverse import reverse

class ParentAPITest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.list_url = reverse('parent list')
        # cls.paginated_url = reverse('presets:industry-type-option-paginated')
        cls.model = Parent
        cls.queryset = cls.model.objects.all()
        # cls.factory = preset_factory.IndustryTypeOptionFactory

    def setUp(self):
        super().setUp()
        self.parent_instance = Parent.objects.create(
          first_name="Jane", last_name="Smith", phone="+41524204242"
        )

    def test_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        expected_response = [
            {   "id" : 3,
                "first_name": "Jane",
                "last_name": "Smith",
                "phone" : "+41524204242"
            }
        ]
        self.assertEqual(response.json(), expected_response)

#    def test_paginated(self):
#         response = self.client.get(
#             self.paginated_url
#         )
#         self.assertEqual(response.status_code, 200)
#         expected_response = {
#             "count": 1,
#             "previous": None,
#             "next": None,
#             "results": [
#                 {
#                     "label": "ECOMMERCE",
#                     "value": "Ecommerce"
#                 }
#             ]
#         }
#         self.assertEqual(response.json(), expected_response)

    # def test_detail(self):
    #     response = self.client.get(
    #         f"{self.list_url}{self.default_instance.uuid}/"
    #     )
    #     self.assertEqual(response.status_code, 404)

    def test_create(self):
        expected_response = {
            "id" : 2,
            "first_name" : "Jane",
            "last_name" : "Smith",
            "phone" : "+41524204242"
        }
        response = self.client.post(
            self.list_url, data=expected_response
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), expected_response)

    # def test_update(self):
    #     # PUT
    #     data = {
    #         "label": "ECOMMERCE",
    #         "value": "Ecommerce"
    #     }
    #     response = self.client.put(
    #         f"{self.list_url}{self.default_instance.uuid}/",
    #         data=data
    #     )
    #     self.assertEqual(response.status_code, 404)

    #     # PATCH
    #     data = {
    #         "label": "ECOMMERCE",
    #         "value": "Ecommerce"
    #     }
    #     response = self.client.patch(
    #         self.client.get(f"{self.list_url}{self.default_instance.uuid}/"),
    #         data=data
    #     )
    #     self.assertEqual(response.status_code, 404)

    # def test_destroy(self):
    #     # DELETE
    #     response = self.client.delete(
    #         f"{self.list_url}{self.default_instance.uuid}/",
    #     )
    #     self.assertEqual(response.status_code, 404)

# import xlsxwriter
# import pandas as pd
# import io
# import random

# from django.contrib.auth import get_user_model
# from django.test import TestCase

# from rest_framework.test import APIClient
# from reportlab.pdfgen import canvas
# from PIL import Image

# #from ats_backend.recruiters.models import Recruiter
# #from ats_backend.users.models import MultiToken

# User = get_user_model()


# class APITest(TestCase):
#     """Base APITest class."""

#     fixtures = (
#         'templates.json', 'auth.json', 'recruiters.json', 'candidates.json',
#         'interviews.json',
#     )

#     def setUp(self):
#         """Will Setup base for tests."""
#         super().setUp()
#         self.client = APIClient()

#         # Users
#         self.admin = User.objects.get(email='admin@yopmail.com')
#         self.recruiter1 = Recruiter.objects.get(user__email='user@yopmail.com')
#         self.recruiter2 = Recruiter.objects.get(
#             user__email='user2@yopmail.com'
#         )
#         self.recruiter3 = Recruiter.objects.get(
#             user__email='user3@yopmail.com'
#         )

#     def get_auth_header(self, user):
#         """Get Auth token."""
#         token = MultiToken.objects.create(user=user)
#         return f'Token {token.key}'
