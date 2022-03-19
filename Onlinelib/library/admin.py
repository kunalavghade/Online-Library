from django.contrib import admin
from . models import Student,books,ContactUs


class StudentAdmin(admin.ModelAdmin):
	list_display = ('firstName','firstName','email','phone','password')


class BookAdmin(admin.ModelAdmin):
	list_display = ('book_name','authour')

admin.site.register(Student,StudentAdmin)
admin.site.register(books,BookAdmin)
