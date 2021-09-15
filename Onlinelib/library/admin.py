from django.contrib import admin
from library.models import Student,books
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
	list_display = ('name','email','phone')


class BookAdmin(admin.ModelAdmin):
	list_display = ('book_name','authour')


admin.site.register(Student,StudentAdmin)
admin.site.register(books,BookAdmin)
