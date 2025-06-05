from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    publish_date = models.DateField(auto_now_add=False)
    tags = models.ManyToManyField(Tag, blank=True)
    
    def __str__(self):
        return self.title
    
    def get_data(self):
        return {
            'title': self.title, 
            'publish_date': self.publish_date, 
            'tags': [tag.name for tag in self.tags.all()]
        }
    