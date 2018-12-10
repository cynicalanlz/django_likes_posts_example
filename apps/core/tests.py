import json
from random import randint
import lorem
from os.path import abspath, dirname, join
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from core.views import SignUpView
from posts.views import PostsViewSet
from likes.views import LikesViewSet


class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = APIRequestFactory()
        config_path = join(dirname(abspath(__file__)), "test_config.json")
        with open(config_path, 'r') as f:
            params = json.load(f)
        self.number_of_users = int(params['number_of_users'])
        self.max_posts_per_user = int(params['max_posts_per_user'])
        self.max_likes_per_user = int(params['max_likes_per_user'])

    def test_details(self):
        user_ids = []
        for n in range(self.number_of_users):
            username = 'user' + str(n)
            email = username + "@google.com"
            request = self.factory.post(
                '/signup_json/',
                json.dumps({
                    "username": username,
                    "email": email,
                    "password": "Aiquai3h"
                }),
                content_type='application/json')
            force_authenticate(request, user=AnonymousUser())
            response = SignUpView.as_view()(request)
            user_ids.append(response.data['id'])
            self.assertEqual(response.status_code, 201)

        post_ids = []
        for user in user_ids:
            for n in range(randint(1, self.max_posts_per_user)):
                user_object = User.objects.get(id=user)
                request = self.factory.post(
                    '/posts/',
                    json.dumps({
                        "user": user,
                        "text": lorem.paragraph()
                    }),
                    content_type='application/json')
                force_authenticate(request, user=user_object)
                response = PostsViewSet.as_view({'post': 'create'})(request)
                post_ids.append(response.data['id'])
                self.assertEqual(response.status_code, 201)
        likes_ids = []
        for user in user_ids:
            available_posts = post_ids
            for n in range(randint(1, self.max_likes_per_user)):
                if len(available_posts) == 0:
                    break
                post_index = randint(0, len(available_posts) - 1)
                post_id = available_posts[post_index]
                del available_posts[post_index]
                request = self.factory.post(
                    '/likes/',
                    json.dumps({
                        "user": user,
                        "post": post_id
                    }),
                    content_type='application/json')
                force_authenticate(request, user=user_object)
                response = LikesViewSet.as_view({'post': 'create'})(request)
                likes_ids.append(response.data['id'])
                self.assertEqual(response.status_code, 201)
