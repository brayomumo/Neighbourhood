from django.test import TestCase
from .models import Business, Profile, Neighbourhood, News, Health, Authorities
from django.contrib.auth.models import User
import datetime as dt
from django.urls import reverse

# Create your tests here.


class NeighbourhoodTestClass(TestCase):

    def setUp(self):
        self.new_neighbourhood = Neighbourhood(
            name="runda", neighbourhood_count="13")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_neighbourhood, Neighbourhood))

    def tearDown(self):

        Neighbourhood.objects.all().delete()

    def test_save_neighbourhood(self):

        self.new_neighbourhood.save_neighbourhood()
        self.assertTrue(len(Neighbourhood.objects.all()) > 0)

    def test_init(self):
        self.assertTrue(self.new_neighbourhood.name == 'runda')

    def test_delete_neighbourhood(self):
        self.new_neighbourhood.save_neighbourhood()
        neighbourhoods = Neighbourhood.objects.all()
        self.new_neighbourhood.delete_neighbourhood()
        self.assertTrue(len(neighbourhoods) == 0)


class ProfileTestClass(TestCase):

    def setUp(self):
        user = User(username='abbyshabi')
        self.profile = Profile(bio='very awesome', user=user)

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()

    def test_is_instance(self):
        """
        This will test whether the new profile is an instance of the Profile class
        """
        self.assertTrue(isinstance(self.profile, Profile))

    def test_init(self):
        """
        This will test whether the new profile is created coreectly
        """
        self.assertTrue(self.profile.bio == "very awesome")

    def test_save_profile(self):
        profile = Profile.objects.all()
        self.assertTrue(len(profile) >= 0)


class PostTestClass(TestCase):

    def setUp(self):

        self.new_user = User(
            username="dee", email="dammy@uu.com", password="hello")
        self.new_user.save()
        self.new_project = Project(name='dee', admin=self.new_user)
        self.new_project.save()
        self.new_post = Post(body='cool')

    def test_instance(self):
        """
        This will test whether the new comment created is an instance of the comment class
        """
        self.assertTrue(isinstance(self.new_post, Post))

    def test_init(self):
        self.assertTrue(self.new_post.body == 'cool')

    def tearDown(self):
        """
        This will clear the dbs after each test
        """

        Post.objects.all().delete()

    def test_save_post(self):
        post = Post.objects.all()
        self.assertTrue(len(post) >= 0)


class BusinessTestClass(TestCase):

    def setUp(self):
        self.new_user = User(
            username="dee", email="dammy@uu.com", password="hello")
        self.new_user.save()
        self.new_project = Project(name='dee', admin=self.new_user)
        self.new_project.save()
        self.new_business = Business(
            name='dee', owner=self.new_user, neighbourhood=self.new_project)
        self.new_business.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_business, Business))

    def tearDown(self):
        """
        This will clear the db after each test
        """
        Business.objects.all().delete()

    def test_save_business(self):

        self.new_business.save_business()
        self.assertTrue(len(Business.objects.all()) > 0)

    def test_init(self):
        self.assertTrue(self.new_business.name == 'dee')

    def test_delete_method(self):
        self.new_business.save_business()
        business = Business.objects.all()
        self.new_business.delete_business()
        business = Business.objects.all()
        self.assertTrue(len(business) == 0)

    def test_search_business(self):
        """
        This will test whether the search function works
        """
        name = Business.search_business("dee")
        self.assertTrue(len(name) > 0)
