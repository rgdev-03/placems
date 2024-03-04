from rest_framework import viewsets, views, permissions, status
from .models import CustomUser
from django.contrib.auth import get_user_model


from .serializers import UserSerializer
from django.shortcuts import redirect
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.tokens import RefreshToken



class UserDetailView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            serializer = UserSerializer(request.user)
            return Response(serializer.data)
        login_url = "/api-auth/login/"  
        return redirect(login_url)


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [permissions.AllowAny]     
        elif self.action in ["create","update", "partial_update"]:
            permission_classes = [permissions.AllowAny]
        elif self.action == "destroy":
            permission_classes = [permissions.AllowAny]  
        else:
            permission_classes = [permissions.AllowAny]  
        return [permission() for permission in permission_classes]
    

class UserLogoutView(views.APIView):
    def post(self, request, *args, **kwargs):
        # Expire JWT token
        if request.user.is_authenticated:
            try:
                refresh_token = request.COOKIES['access_token']
                RefreshToken(refresh_token).blacklist()
                return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
            except KeyError:
                return Response({"error": "'refresh_token' cookie not found."}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "User not authenticated."}, status=status.HTTP_401_UNAUTHORIZED)
    
    # Allow GET method to provide additional information about the endpoint
    # def get(self, request, *args, **kwargs):
    #     return Response({"message": "Please use POST method to logout."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# class CreateUserView(views.APIView):
#     permission_classes = [IsProjOwnOrProjLead]

#     @swagger_auto_schema(request_body=UserCreateSerializer)
#     def post(self, request, *args, **kwargs):
#         serializer = UserCreateSerializer(
#             data=request.data, context={"request": request}
#         )
#         if serializer.is_valid():
#             user = serializer.save()
#             # Set password and mark user as active
#             user.set_password(request.data["password"])
#             user.is_active = True
#             user.save()
#             return Response({"message": "User created successfully."})
#         return Response(serializer.errors, status=400)


# class PasswordSetView(views.APIView):
#     permission_classes = [permissions.AllowAny]

#     def post(self, request, token):
#         try:
#             User = get_user_model()
#             user = User.objects.get(password_reset_token=token)
#             if user is None:
#                 return Response({"error": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)

#             # Assuming password is sent in request data and set directly during user creation
#             user.is_active = True
#             user.save()

#             # You may optionally invalidate the password_reset_token here
#             # user.password_reset_token = None
#             # user.save()

#             # You can also return user details or tokens if needed
#             serializer = UserSerializer(user)
#             return Response(serializer.data)

#         except User.DoesNotExist:
#             return Response({"error": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)