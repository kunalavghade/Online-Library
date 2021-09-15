from django.db import models

# Create your models here.
class Student(models.Model):
	date = models.DateField()
	name = models.CharField(max_length=50)
	email= models.EmailField(max_length=50)
	phone = models.IntegerField()
	address = models.CharField(max_length = 100)
	password = models.CharField(max_length = 50)


class books(models.Model):
	book_cover = models.ImageField(upload_to="images/")
	book_name = models.CharField(max_length=20)
	authour = models.CharField(max_length=10)
	Discription = models.CharField(max_length=60)
	link = models.CharField(max_length=2083)


