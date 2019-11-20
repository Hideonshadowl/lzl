from django.core.exceptions import ValidationError
import re
def username_validator(value):

    if not re.match('\d{11}', value):
        return ValidationError('请输入11位整数!')