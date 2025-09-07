from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiExample  # ← ADD OpenApiExample
from .serializers import UserSerializer
from .tasks import send_welcome_email

@api_view(['POST'])
@extend_schema(
    request=UserSerializer,
    responses={201: {"type": "object", "properties": {"message": {"type": "string"}}}},
    examples=[
        OpenApiExample(
            'Register User Example',
            value={
                "username": "john_doe",
                "email": "john@example.com",
                "password": "securepassword123"
            },
            request_only=True,  # This example is only for requests
        ),
    ],
)
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        send_welcome_email.delay(user.email)
        return Response({"message": "User created. Welcome email sent!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)