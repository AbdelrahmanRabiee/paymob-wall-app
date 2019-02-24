from rest_framework.test import APITestCase
from rest_framework import status

from model_mommy import mommy

from fb_wall.users.models import User
# Create your tests here.


class BlogTestAPI(APITestCase):
    def setUp(self):
        self.user = mommy.make(User)
        self.post_url = "/api/posts/"

    def tearDown(self):
        self.user.delete()

    def test_user_can_add_post(self):
        self.client.force_login(self.user)
        data = {
                    "content": "Hello paymob"
                }

        resp = self.client.post(self.post_url, data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(resp.data['content'], 'Hello paymob')
