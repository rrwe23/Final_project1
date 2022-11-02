
from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill




class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    thumbnail = ProcessedImageField(upload_to="images/", blank=True,
                                    processors=[ResizeToFill(300,200)],
                                    format ='JPEG',
                                    options = {'quality':80})
    image = ProcessedImageField(upload_to='images/', blank=True,
                                    processors=[ResizeToFill(1200,960)],
                                    format='JPEG',
                                    options={'quality':80})
    content = models.TextField()
    cart = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'cart_product')
    review = models.ManyToManyField('products.Review', related_name = 'review_product')
    qna = models.ManyToManyField('products.Question', related_name = 'qna_product')


                    









