from django.db import models
from taggit.managers import TaggableManager
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
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=50000)
    publish_date = models.DateTimeField()
    tags = TaggableManager()
    img = models.ImageField(upload_to='posts')

    def __str__(self):
        return self.title


    
