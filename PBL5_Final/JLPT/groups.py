from .permissions import *

from django.contrib.auth.models import Group

#teahcer group
teacher_group,created = Group.objects.get_or_create(name='Teacher')
teacher_group.permissions.add(login_teacher_page[0].id)

#Student group
student_group,created = Group.objects.get_or_create(name='Student')
student_group.permissions.add(login_student_page[0].id)