from django.db import models
# Create your models here.

class Student(models.Model):
	firstName = models.CharField(max_length = 50)
	lastName = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 254)
	phone = models.IntegerField()
	password = models.CharField(max_length = 50)

class ContactUs(models.Model):
	your_name = models.CharField(max_length = 50)
	email_address = models.EmailField(max_length = 254)
	Your_message = models.CharField(max_length = 1024)

class books(models.Model):
	book_cover = models.ImageField(upload_to="images/")
	book_name = models.CharField(max_length=20)
	authour = models.CharField(max_length=10)
	Discription = models.CharField(max_length=60)
	link = models.CharField(max_length=2083)


