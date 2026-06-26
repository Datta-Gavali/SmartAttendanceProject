from .models import Student, Attendance
from django.shortcuts import render


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


def mark_attendance(request):

    if request.method == "POST":

        student_id = request.POST["student_id"]

        student = Student.objects.get(id=student_id)

        attendance = Attendance(student=student)

        attendance.save()

        return render(
            request,
            "mark_attendance.html",
            {"message": "Attendance Marked Successfully"},
        )

    return render(request, "mark_attendance.html")
