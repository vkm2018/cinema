from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()


class Category(models.Model):

    title = models.CharField(max_length=30)
    slug = models.SlugField(primary_key=True, max_length=30,unique=True,blank=True)

    def save(self, *args, **kwargs):
        self.slug = self.title.lower()
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Cinema(models.Model):
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cinemas')
    title = models.CharField(max_length=30)
    descriptions = models.TextField(max_length=200)
    janr = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='janrs')
    year = models.IntegerField()
    avatar = models.ImageField(upload_to='cinema', blank=True, null=True)


    def __str__(self):
        return self.title

class Image(models.Model):
    preview = models.ImageField(upload_to='cinema')
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='preview')











