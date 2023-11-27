from django.contrib import admin

from .models import Teacher, Assignmet, Course

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    fields = ['user', 'designation']

@admin.register(Assignmet)
class AssignmentAdmin(admin.ModelAdmin):
    fields = ['course', 'title', 'description']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    fields = ['creator','students', 'course_code', 'course_title', 'course_description']