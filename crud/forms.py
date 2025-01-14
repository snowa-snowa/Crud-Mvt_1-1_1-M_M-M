from django import forms
from .models import Product, Book, Course, Student, Participant, Event


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['product', 'author', 'isbn']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['description', 'name']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'courses']


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email']


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['title', 'date', 'participants']
