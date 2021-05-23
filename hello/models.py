from django.db import models


class Image(models.Model):
    caption = models.CharField(max_length=50)
    img = models.ImageField(upload_to="img/%y")

    def __str__(self):
        return self.caption


class BdayComment(models.Model):
    username = models.CharField(max_length=100)
    usercomment = models.CharField(max_length=1000)

    def __str__(self):
        return self.usercomment


class UserComments(models.Model):
    img_url = models.CharField(max_length=200)
    username = models.CharField(max_length=50)
    comment = models.CharField(max_length=1000)
