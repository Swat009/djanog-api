from rest_framework import generics
from tutorial.permissions import IsAuthenticatedOrCreate
#from django.conf import settings
#from settings.AUTH_USER_MODEL import User
from tutorial.serializers import SignUpSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (IsAuthenticatedOrCreate,)