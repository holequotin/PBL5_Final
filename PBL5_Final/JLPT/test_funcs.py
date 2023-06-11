from django.contrib.auth.decorators import user_passes_test,login_required
from django.contrib.auth.models import Group,AnonymousUser

def user_is_teacher(user):
    if user is AnonymousUser:
        return False
    return user.groups.filter(name='Teacher').exists()

def user_is_student(user):
    if user is None:
        return False
    return user.groups.filter(name='Student').exists()