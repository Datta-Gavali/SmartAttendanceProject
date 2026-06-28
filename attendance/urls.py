from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add-student/", views.add_student, name="add_student"),
    path("students/", views.student_list, name="student_list"),
    path("mark-attendance/", views.mark_attendance, name="mark_attendance"),
    path("attendance-records/", views.attendance_records, name="attendance_records"),
    path("start-camera/", views.start_camera, name="start_camera"),
]
