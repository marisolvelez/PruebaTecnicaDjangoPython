
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
import re
import pdb #recordar borrar esto


class UserRegistrationView(APIView):
    def post(self, request):
        #de esta forma se esta obteniendo los datos que se mandan por el formulario
        username = request.data.get('username')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        password = request.data.get('password')

        is_valid, error_message = validate_fields(username, first_name, last_name, email, password)
        if is_valid:
            
            #si existe un usuario con el mismo nombre de usuario
            if User.objects.filter(username=username).exists():
                return Response({"message": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
            
            new_user = User.objects.create_user(username=username, first_name = first_name, last_name = last_name, email=email ,password=password)

            new_user.save()

            return Response(status=status.HTTP_201_CREATED)
        else:
            messages.error(request, error_message)
            return render(request, 'registerForm.html', {'title': 'Register'})

class UserLoginView(APIView):
    def post(self, request):
        #pdb.set_trace()
        # obteniendo los datos del formulario del login
        username = request.data.get('username')
        password = request.data.get('password')
        
        # Autentificacion del usuario
        user = authenticate(username=username, password=password)
        print(user)

        if user is not None:
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

class UserLogoutView(APIView):
    def post(self, request):
        # Lógica para cerrar sesión
        return Response(status=status.HTTP_204_NO_CONTENT)

def login(request):
    if request.method == 'POST':
        
        #llamando a la APIView para iniciar sesión
        user_login_view = UserLoginView.as_view()
        response = user_login_view(request)
        
        if response.status_code == status.HTTP_200_OK:
            return redirect('/product/crud/')
        else:
            messages.warning(request, "Invalid username or password")

    return render(request, 'loginForm.html', { 
        'title': 'Login'
    })

def register_user(request):
    if request.method == 'POST':

        # llamando a la API para registrar un nuevo usuario
        api_response = UserRegistrationView.as_view()(request)
        
        if api_response.status_code == status.HTTP_201_CREATED:
            return render(request, 'loginForm.html')

        else:
            messages.warning(request, "failed registration.")

    # Si la solicitud no es POST
    return render(request, 'registerForm.html', { 
        'title': 'Register'
    })

def validate_fields(username, first_name, last_name, email, password):
    username_pattern = r'^[a-zA-Z0-9_]{3,20}$'
    first_name_pattern = r'^[a-zA-Z\s]+$'
    last_name_pattern = r'^[a-zA-Z\s]+$'
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,20}$'

    if not re.match(username_pattern, username):
        return False, "The username must contain between 3 and 20 alphanumeric characters and underscores."
    
    if not re.match(first_name_pattern, first_name):
        return False, "Enter your name."
    
    if not re.match(last_name_pattern, last_name):
        return False, "Enter your lastname."
    
    if not re.match(email_pattern, email):
        return False, "Please enter a valid email address."
    
    if not re.match(password_pattern, password):
        return False, "The password must contain at least one lowercase letter, one uppercase letter, one digit, and be between 6 and 20 characters long."
    
    return True, None
    




#--------------------------------------------------serializacion si se necesita
#from django.contrib.auth.models import User
#from rest_framework import serializers

#class UserSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = User
#        fields = ['id', 'username', 'email', 'password']
#        extra_kwargs = {'password': {'write_only': True}}

#    def create(self, validated_data):
#        user = User.objects.create_user(**validated_data)
#        return user