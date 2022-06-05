from django.test import TestCase

# Create your tests here.
# test for model class Profile
class TestProfile(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("testuser", "secret")
        self.profile_test = Profile(picture='test.jpg',bio="this is a test bio",user=self.user)
        self.profile_test.save()

    def test_instance_true(self):
        self.profile_test.save()
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_profile(self):
        self.profile_test.save()
        pp = Profile.objects.all()
        self.assertTrue(len(pp) > 0)
