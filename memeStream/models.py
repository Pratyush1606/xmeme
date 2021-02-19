from django.db import models

# Create your models here.
class Meme(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    caption = models.TextField()

    
    def __str__(self):
        return self.name+"\n"+self.caption+"\n"+self.url
