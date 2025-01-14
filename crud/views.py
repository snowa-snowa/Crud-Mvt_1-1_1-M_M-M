from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Book, Course, Student, Participant, Event
from .forms import ProductForm, BookForm, CourseForm, StudentForm, ParticipantForm, EventForm


def product_list(request):
    names = Product.objects.all()
    return render(request, 'crud/product_list.html', {'names': names})


def product_detail(request, pk):
    name = Product.objects.get(pk=pk)
    return render(request, 'crud/product_detail.html', {'name': name})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'crud/product_form.html', {'form': form})


def product_update(request, pk):
    name = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=name)
        if form.is_valid():
            form.save()
            return redirect('place_list')
    else:
        form = ProductForm(instance=name)
    return render(request, 'crud/product_form.html', {'form': form})


def product_delete(request, pk):
    name = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        name.delete()
        return redirect('product_list')
    return render(request, 'crud/product_confirm_delete.html', {'object': name})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'crud/book_list.html', {'books': books})


def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'crud/book_detail.html', {'book': book})


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'crud/book_form.html', {'form': form})


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'crud/book_form.html', {'form': form})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'crud/book_confirm_delete.html', {'object': book})


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'crud/course_list.html', {'courses': courses})


def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'crud/course_form.html', {'form': form})


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'crud/course_detail.html', {'course': course})


def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_detail', pk=pk)
    else:
        form = CourseForm(instance=course)
    return render(request, 'crud/course_form.html', {'form': form})


def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'crud/course_confirm_delete.html', {'course': course})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'crud/student_list.html', {'students': students})


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'crud/student_form.html', {'form': form})


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'crud/student_detail.html', {'student': student})


def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', pk=pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'crud/student_form.html', {'form': form})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'crud/student_confirm_delete.html', {'student': student})


def participant_list(request):
    participants = Participant.objects.all()
    return render(request, 'crud/participant_list.html', {'participants': participants})


def participant_detail(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    return render(request, 'crud/participant_detail.html', {'participant': participant})


def participant_create(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
    else:
        form = ParticipantForm()
    return render(request, 'crud/participant_form.html', {'form': form})


def participant_update(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    if request.method == 'POST':
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
    else:
        form = ParticipantForm(instance=participant)
    return render(request, 'crud/participant_form.html', {'form': form})


def participant_delete(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    if request.method == 'POST':
        participant.delete()
        return redirect('participant_list')
    return render(request, 'crud/participant_confirm_delete.html', {'participant': participant})


def event_list(request):
    events = Event.objects.all()
    return render(request, 'crud/event_list.html', {'events': events})


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'crud/event_detail.html', {'event': event})


def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'crud/event_form.html', {'form': form})


def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'crud/event_form.html', {'form': form})


def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'crud/event_confirm_delete.html', {'event': event})


def my_view(request):
    if request.method == 'GET':
        return render(request, 'crud/my_view.html')


def crud(request):
    if request.method == 'GET':
        return render(request, 'crud/crud.html')
