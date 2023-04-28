from django.contrib.auth.decorators import user_passes_test,login_required
from django.contrib.auth.models import Group

def user_is_teacher(user):
    return user.groups.filter(name='Teacher').exists()
