from rest_framework import serializers
#from django.conf import settings
#from settings.AUTH_USER_MODEL import User
from django.contrib.auth import get_user_model

User = get_user_model()
class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        write_only_fields = ('password',)