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




    def __str__(self):
        return self.title

class Preview(models.Model):
    image = models.ImageField(upload_to='cinema')
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='images')

class Video(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='videos')
    video = models.FileField(upload_to='video/')



class Like(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes', verbose_name='Владелей лайка')
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='likes', verbose_name='фильм')
    like = models.BooleanField('лайк', default=False)

    def __str__(self):
        return f'{self.cinema}{self.like}'


class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings', verbose_name='Владелец рейтинга')
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='ratings', verbose_name='фильм')
    rating = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'{self.cinema}{self.rating}'

class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='Владелец коммента')
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='comments', verbose_name='фильм')
    comment = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class Favorite(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorits', verbose_name='Владелец избранного')
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='favorits', verbose_name='фильм')
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.cinema} {self.favorite}'












