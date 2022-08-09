from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
User = get_user_model()
from applications.account.serializers import RegisterSerializer, LoginSerializer, ChangePasswordSerializer, \
    ForgotPasswordCompleteSerializer, ForgotPasswordSerializer


class RegisterApiView(APIView):

    def post(self, request):
        data = request.data
        email = data.get('email')
        serializers = RegisterSerializer(data=data)

        # print (data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            mes = f'Вы успшено зарегистровались,' \
                  f' На ваш email {email} отправлено письмо с инструкциями по активции'
            return Response (mes, status=201)



class ActivationApiView(APIView):
    def get(self,request,activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active=True
            user.activation_code = ''
            user.save()
            return Response({'Вы успешно зарегистрировались'}, status = 201)
        except:
            return Response({'Ошибка'}, status=400)


class LoginApiView(ObtainAuthToken):
    serializer_class = LoginSerializer

class ChangePasswordApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializers = ChangePasswordSerializer(data=request.data, context={'request': request})
        serializers.is_valid(raise_exception=True)
        serializers.set_new_password()
        return Response('Пароль успшено обновлен')

class ForgotPasswordApiView(APIView):
    def post(self, request):
        data = request.data
        serializer = ForgotPasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.send_code()
        return Response('Вам отправлено письмо для восстановления пароля')


class ForgotPasswordCompleteApiView(APIView):
    def post(self, request):
        data = request.data
        serializer = ForgotPasswordCompleteSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.set_new_pass()
        return Response('Пароль успешно обновлен!')


class LogOutApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user = request.user
            Token.objects.filter(user=user).delete()
            return  Response('Вы успешно вышли')
        except:
            return Response(status=403)