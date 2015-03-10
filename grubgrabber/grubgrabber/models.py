from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    about = models.CharField(max_length=500)

    def __unicode__(self):
        return self.user.user_id

class Favourites(models.Model):
    user = models.ForeignKey(User)
    place_id = modeles.CharField(max_legnth = 100)
	
    def __unicode__(self):
        return self.Favourites.Place_ID

class Likes(models.Model):
    user = models.ForeignKey(User)
    place_id = modeles.CharField(max_legnth = 100)
	
    def __unicode__(self):
        return self.Likes.Place_ID

class Dislikes(models.Model):
    user = models.ForeignKey(User)
    place_id = modeles.CharField(max_legnth = 100)
	
    def __unicode__(self):
        return self.Dislikes.Place_ID

class Blacklist(models.Model):
    user = models.ForeignKey(User)
    place_id = modeles.CharField(max_legnth = 100)
    
    def __unicode__(self):
        return self.Blacklist.Place_ID
