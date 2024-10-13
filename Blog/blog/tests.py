from django.db.models import DateTimeField
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.dateparse import parse_datetime
from django.utils import timezone

from .models import Post


class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret"
        )
        cls.post = Post.objects.create(
            title="Test Title",
            author=cls.user,
            date ="2024-10-10",
            body="Test Body",
        )


    def test_post_model(self):
        self.assertEqual(self.post.title, "Test Title")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.date, "2024-10-10")
        self.assertEqual(self.post.body, "Test Body")
        self.assertEqual(str(self.post), "Test Title")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")

    def test_url_location_listView(self):
        response = self.client.get("/post/1/")
        self.assertEqual(response.status_code, 200)

    def test_url_location_detailView(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homePage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Test Body")

    def test_post_detailView(self):
        response = self.client.get(reverse("post_detail", kwargs={"pk": self.post.pk}))
        no_response = self.client.get("/post/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, "post_detail.html")
        self.assertContains(response, "Test Title")

    def test_post_createView(self):
        response = self.client.post(
            reverse("post_new"),
            {
                "title": "New title",
                "body": "New text",
                "author": self.user.id,
                "date": "2024-12-12",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "New title")
        self.assertEqual(Post.objects.last().body, "New text")
        self.assertEqual(Post.objects.last().date, timezone.make_aware(parse_datetime("2024-12-12")))


    def test_post_updateView(self):
        response = self.client.post(
            reverse("post_update", args="1"),
            {
                "title": "Updated title",
                "body": "Updated text",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "Updated title")
        self.assertEqual(Post.objects.last().body, "Updated text")

    def test_post_deleteView(self):
        response = self.client.post(reverse("post_delete", args="1"))
        self.assertEqual(response.status_code, 302)