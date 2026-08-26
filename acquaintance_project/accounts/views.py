
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')
        username = data.get('username') or email.split('@')[0]

        if not email or not password:
            return Response({'error': 'email и password обязательны'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            validate_password(password)
        except ValidationError as e:
            return Response({'error': e.messages}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({'error': 'Пользователь с таким email уже существует'}, status=status.HTTP_409_CONFLICT)

        user = User.objects.create_user(username=username, email=email, password=password)
        # сразу создаём пустой профиль, если нужно, или при первом редактировании
        return Response({'detail': 'Пользователь создан'}, status=status.HTTP_201_CREATED)
