from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_player = models.BooleanField(default=False)
    is_developer = models.BooleanField(default=False)


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)


# Create your models here.
class Category(models.Model):
    DEFAULT_PK = 1
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:game_list_by_category', args=[self.slug])




class Game(models.Model):
    category = models.ForeignKey(Category, related_name='games', on_delete=models.CASCADE)
    url = models.URLField()
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)
    price = models.PositiveIntegerField()
    image = models.ImageField()
    description = models.TextField()

    class Meta:
        ordering = ('name',)
        #index_together = (('id', 'slug'),)
        verbose_name = 'game'
        verbose_name_plural = 'games'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:game_detail', args=[self.id, self.slug])



#* Player: name, email, password, games

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    games = models.ManyToManyField(Game)

    def get_id(self):
        return self.user.id

    def username(self):
        return self.user.get_username()

    def name(self):
        return self.user.get_full_name()

#* Developer: name, email, password, games
class Developer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    games = models.ManyToManyField(Game)

    def get_id(self):
        return self.user.id

    def username(self):
        return self.user.get_username()

    def name(self):
        return self.user.get_full_name()

#* Highscore: gameName, playerName, score
