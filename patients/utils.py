import random
import string
from patients.models import Test

def random_string_generator(size=6, chars=string.ascii_uppercase + "123456789"):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_id_generator():
    new_id = random_string_generator()
    qs_exists = Test.objects.filter(code=new_id).exists()
    if qs_exists:
        return unique_id_generator()
    return new_id