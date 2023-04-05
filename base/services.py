from django.conf import settings
from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, file):
    return f'avatar/{instance.id}/{file}'

def validate_size_image(file_obj):
    if file_obj.size > settings.USER_AVATAR_MEGABYTE_LIMIT * 1024 * 1024:
        raise ValidationError(f'Максимальный размер файла — {settings.USER_AVATAR_MEGABYTE_LIMIT} МБ.')