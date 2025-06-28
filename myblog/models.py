from django.db import models

# Create your models here.
class BlogPosts(models.Model):
    heading = models.CharField(max_length=350)
    blog_contents = models.TextField()
    image = models.ImageField(
        default='bg2.jpg',
        upload_to='images/blog',
        height_field='image_height',
        width_field='image_width',
        blank=True,  # Allows field to be empty in forms
        null=True    # Allows database column to be NULL
    )
    image_height = models.PositiveIntegerField(null=True, blank=True)
    image_width = models.PositiveIntegerField(null=True, blank=True)

class Users(models.Model):
    Fullname = models.CharField(max_length=300)
    Email = models.EmailField(max_length=254)
    Password = models.CharField(max_length=350)
    confirm_password = models.CharField(max_length=350)

class Comment(models.Model):
    blog = models.ForeignKey(BlogPosts, on_delete=models.CASCADE)
    text = models.TextField()