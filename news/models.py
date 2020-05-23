from django.db import models

# Create your models here.

class New(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField(editable=True)
    image = models.ImageField(upload_to='static/images/news/',null=True)

    def __str__(self):
        return '%s \n %s \n %s \n' % (self.title, self.body, self.image)