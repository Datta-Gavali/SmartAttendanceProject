from django.shortcuts import render
from .models import Student


def home(request):
    return render(request, "home.html")


def add_student(request):

    if request.method == "POST":

        name = request.POST["name"]
        roll_number = request.POST["roll_number"]
        department = request.POST["department"]

        student = Student(name=name, roll_number=roll_number, department=department)

        student.save()

        return render(
            request, "add_student.html", {"message": "Student Added Successfully"}
        )

    return render(request, "add_student.html")


def student_list(request):

    students = Student.objects.all()

    return render(request, "students.html", {"students": students})
