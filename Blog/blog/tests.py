from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
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

    def test_postDetailPage(self):
        response = self.client.get(reverse("post_detail", kwargs={"pk": self.post.pk}))
        no_response = self.client.get("/post/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, "post_detail.html")
        self.assertContains(response, "Test Title")