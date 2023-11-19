from django.db import models

# Create your models here.
class Users(models.Model):

    def __str__(self):
        return self.user_name

    user_name = models.CharField(max_length=200)
    user_password = models.CharField(max_length=50)
    user_id = models.IntegerField()