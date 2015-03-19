from django.db import models
from django.contrib.auth.models import User

class Favourite(models.Model):
    user = models.ForeignKey(User)
    place_id = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.user.username + " favourited " + self.place_id

class Like(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    place_id = models.CharField(max_length = 100)
    name = models.CharField(max_length = 30)

    def __unicode__(self):
        return self.place_id

class Dislike(models.Model):
    user = models.ForeignKey(User)
    place_id = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.place_id

class Blacklist(models.Model):
    user = models.ForeignKey(User)
    place_id = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.place_id

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    about = models.CharField(max_length = 2000, blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username
