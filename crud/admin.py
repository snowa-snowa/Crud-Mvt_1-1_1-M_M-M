from django.contrib import admin
from .models import Participant, Event, Product, Book, Course, Student

admin.site.register(Participant)
admin.site.register(Event)
admin.site.register(Product)
admin.site.register(Book)
admin.site.register(Course)
admin.site.register(Student)
