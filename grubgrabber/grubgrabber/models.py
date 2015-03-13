from django.db import models
from django.contrib.auth.models import User

class Favourite(models.Model):
    user = models.ForeignKey(User)
    place_id = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.Favourites.Place_ID

class Like(models.Model):
    user = models.ForeignKey(User)
    place_id = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.Likes.Place_ID

class Dislike(models.Model):
    user = models.ForeignKey(User)
    place_id = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.Dislikes.Place_ID

class Blacklist(models.Model):
    user = models.ForeignKey(User)
    place_id = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.Blacklist.Place_ID

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    about = models.URLField(max_length = 2000)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username
