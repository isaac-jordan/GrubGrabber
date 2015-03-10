from django.db import models

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
        
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username
