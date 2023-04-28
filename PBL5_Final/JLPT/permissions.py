from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

content_type = ContentType.objects.get_for_model(User)
#teacher
login_teacher_page = Permission.objects.get_or_create(
    name='Can login teacher page', 
    codename='login_teacher_page',
    content_type = content_type,
    )


#student
login_student_page = Permission.objects.get_or_create(
    name='Can login student page', 
    codename='login_student_page',
    content_type = content_type
    )