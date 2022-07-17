
from email.policy import default
from tkinter import CASCADE
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class artist(models.Model):
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics',default='default.jpg')
    Phone = models.CharField(max_length=100)
    Desc = models.TextField()

    def __str__(self):
        return self.Name

class painting(models.Model):
    Artist = models.ForeignKey(artist,on_delete=models.CASCADE)
    Title = models.CharField(max_length=100)
    price = models.IntegerField()
    artist_name= models.CharField(max_length=200)
    # Genre = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics',default='default.jpg')
    # Desc = models.TextField()
    def __str__(self):
        return self.Title


# class art_gallery(models.Model):
#     ArtS = models.ForeignKey(Arts,on_delete=models.CASCADE)
#     Photos = models.ForeignKey(Photography,on_delete=models.CASCADE)
#     Gallery_name = models.CharField(max_length=100)
#     name = models.CharField(max_length=100)
#     Location = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='pics',default='default.jpg')


class Art(models.Model):
    # name = models.CharField(max_length=100)
    # Location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics',default='default.jpg')


class Photography(models.Model):
    # name = models.CharField(max_length=100)
    # Location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics',default='default.jpg')



# class exhibition(models.Model):
#     Gallery_ID = models.ForeignKey(art_gallery,on_delete=models.CASCADE)
#     E_name = models.CharField(max_length=100)
#     E_type = models.CharField(max_length=100)
#     E_Location = models.CharField(max_length=100)
#     Start_date = models.DateField()
#     End_date = models.DateField()

class customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    # C_name = models.CharField(max_length=100)
    Customer_address = models.TextField()
    Customer_phone = models.CharField(max_length=100)

# class order(models.Model):
#     Customer = models.ForeignKey(customer,on_delete=models.CASCADE)
#     Paintings = models.ForeignKey(painting,on_delete=models.CASCADE)
#     Order_type = models.CharField(max_length=100)
#     Order_no = models.IntegerField()
#     Order_desc = models.TextField()

# class payment(models.Model):
#     Customer = models.ForeignKey(customer,on_delete=models.CASCADE)
#     Paintings = models.ForeignKey(painting,on_delete=models.CASCADE)
#     Payment_date = models.DateField()
#     Payment_bill = models.IntegerField()
#     Payment_type = models.CharField(max_length=100)
#     Payment_desc = models.TextField()


class Person(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)

    def _str_(self):
        return self.name


