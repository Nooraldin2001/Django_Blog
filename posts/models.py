from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone
import readtime
# Create your models here.
'''
    - title
    - author
    - content
    - img
    - publish_date
    - tags
'''

'''
    - fields it choose the best field to use 
    - html widget
    - valdations
'''

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=50000)
    publish_date = models.DateTimeField(default=timezone.now())
    tags = TaggableManager()
    img = models.ImageField(upload_to='posts')

    def __str__(self):
        return self.title
    
    def get_readtime(self):
      result = readtime.of_text(self.content)
      return result.text 


    
