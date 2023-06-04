from django.core.exceptions import ValidationError

def validate_phone_number(value):
    if not value.isdigit():
        raise ValidationError('Số điện thoại không hợp lệ. Chỉ chấp nhận các kí tự số.')
