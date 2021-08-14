from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.urls import reverse


# Create your models here.

class BlogPost(models.Model):

    title=models.CharField(max_length=256)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    slug=models.CharField( max_length=50)
    content=models.TextField()
    image=models.ImageField(upload_to="profile_pics",blank=True,null=True)
    datetime=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  "Blog Title :" + self.title

    def get_absolute_url(self):
        return reverse("blogs_detail", kwargs={"slug": self.slug})
        
        
         