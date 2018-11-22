from models import *

def authenticate(data):
    user = get_object_or_404(User, pk=data.id)
    return ""
