from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer,ListSerializer,LoginSerializer,LogoutSerializer
from .models import User
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    AllowAny,
) 
# class UserViewList(APIView):
#     def get(self,request,*arg,**kwarg):
#        users = User.objects.all()
#        serializer = UserSerializer(users,many = True)

#        return  Response(serializer.data)

# class UserCreateView(APIView):
#     def post(self,request,*args,**kwargs):
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         username = serializer.validated_data.get("username")
#         first_name = serializer.validated_data.get("first_name")
#         last_name = serializer.validated_data.get("last_name")

#         User.objects.create(username=username,first_name=first_name,last_name=last_name)

#         return Response({"message":"User create Succesfully"})

class LoginView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get("username")
        password = serializer.validated_data.get("password")

        try: 
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"message": "Invalid credentials"}, status=401)

        if not user.check_password(password):  # type:ignore
            return Response({"message": "Invalid credentials"}, status=401)

        #    try:
        #        token = Token.objects.get(user=user)
        #    except Token.DoesNotExist:
        #        token = Token.objects.create(user=user)

        token, created = Token.objects.get_or_create(user=user)

        return Response({"message": "Login successful", "token": token.key})
    
class LogoutView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        Token_from_user=serializer.validated_data.get("token")
        try:
            key = Token.objects.get(key=Token_from_user)
            Token.delete(key)
            return Response({"message":"LogOUt Successfully"})
        except Token.DoesNotExist:
            return Response({"message":"Doesnot Exist"})






class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = ListSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer

class UserRetrieveView(RetrieveAPIView):
     queryset = User.objects.all()
     serializer_class = UserSerializer
class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ListSerializer
class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
