from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    body = models.TextField()

    hashtag_field = models.CharField(max_length = 200, blank = True)
    hashtags = models.ManyToManyField('Hashtag', blank = True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    def __str__(self):
        return self.text
    
    post_id = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments')
    text = models.CharField(max_length = 50)

class Hashtag(models.Model):
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length = 50)