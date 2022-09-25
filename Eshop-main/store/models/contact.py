from django.db import models

class Contacts(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField (max_length=50)
    # subject = models.CharField(max_length=10)
    msg= models.CharField(max_length=100)
    # sub=models.CharField(max_length=100)
    # pic=models.ImageField(upload_to="uploads/products")

    def __str__(self):
        return self.name
