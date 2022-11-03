
from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Review(models.Model):
    star_list = [
        ('⭐', '⭐'),
        ('⭐⭐', '⭐⭐'),
        ('⭐⭐⭐', '⭐⭐⭐'),
        ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    star = models.CharField(max_length=5, choices=star_list)
    created_at = models.DateTimeField(auto_now_add = True)
    image = ProcessedImageField(upload_to="images/", blank=True,
                                    processors=[ResizeToFill(200,100)],
                                    format ='JPEG',
                                    options = {'quality':80})
    content = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'like_reviews')
