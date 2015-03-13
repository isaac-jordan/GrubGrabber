from django.contrib import admin
from grubgrabber.models import Favourite, Like, Dislike, Blacklist, UserProfile

class FavouritesAdmin(admin.ModelAdmin):
    list_display = ('user', 'place_id')
    
class LikesAdmin(admin.ModelAdmin):
    list_display = ('user', 'place_id')

class DislikesAdmin(admin.ModelAdmin):
    list_display = ('user', 'place_id')
    
class BlacklistAdmin(admin.ModelAdmin):
    list_display = ('user', 'place_id')
    
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'about', 'picture')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Favourite, FavouritesAdmin)
admin.site.register(Like, LikesAdmin)
admin.site.register(Dislike, DislikesAdmin)
admin.site.register(Blacklist, BlacklistAdmin)