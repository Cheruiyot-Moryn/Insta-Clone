from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
#class Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='0')
    picture = CloudinaryField('image')
    bio = models.TextField()
    
    def __str__(self):
        return self.user.username

    @classmethod
    def update_profile(cls, id, user, bio, picture):
        cls.objects.filter(id=id).update(user=user, bio=bio, picture=picture)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()