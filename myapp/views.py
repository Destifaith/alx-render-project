from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema  # ← ADD THIS IMPORT
from .serializers import UserSerializer
from .tasks import send_welcome_email

@api_view(['POST'])
@extend_schema(
    request=UserSerializer,  # ← TELL Swagger what input to expect
    responses={201: {"type": "object", "properties": {"message": {"type": "string"}}}}
)
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        send_welcome_email.delay(user.email)
        return Response({"message": "User created. Welcome email sent!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)