import random
import string

def random_string_generator(size=6, chars=string.ascii_uppercase + "123456789"):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_id_generator(instance):
    new_id= random_string_generator()
    Klass= instance.__class__
    qs_exists= Klass.objects.filter(order_id=new_id).exists()
    if qs_exists:
        return unique_id_generator(instance)
    return new_id