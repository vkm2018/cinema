from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

# from applications.account.send_email import send_is_active, forgot_password_email
from applications.account.tasks import celery_confirm_email,forgot_password_email
from applications.cinema.models import Favorite

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(min_length=6, write_only=True, required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2')
        username = attrs.get('username')
        sym = ['@', '/', '#', '!', '*', '"\ "',]

        if password != password2:
            raise serializers.ValidationError('Пароли не совпадают')
        elif any([i in sym for i in username]):
            raise serializers.ValidationError('Не должной быть символов')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        code = user.activation_code
        celery_confirm_email.delay(code, user.email)

        return user

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate_username(self, username):
        if not User.objects.filter(username=username,).exist():
            raise serializers.ValidationError('Пользователь с таким username не существует')
        return username

    def validate(self, attrs):
        password = attrs.get('password')
        username = attrs.get('username')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise serializers.ValidationError('Невервый пароль или username')
            attrs['user']=user
            return attrs

# class FavoriteSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Favorite
#         fields = ['favorite']


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    password = serializers.CharField(required=True, min_length=6)
    password2 = serializers.CharField(required=True, min_length=6)


    def validate_old_password(self, old_password):
        user = self.context.get('request').user

        if not user.check_password(old_password):
            raise serializers.ValidationError('Неверный пароль!')

        return old_password

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2')

        if password != password2:
            raise serializers.ValidationError('Пароли не совпадают!')
        return attrs

    def set_new_password(self):

        user = self.context.get('request').user
        password = self.validated_data.get('password')
        user.set_password(password)
        user.save()


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь не зарегистрирован')
        return email

    def send_code(self):
        email = self.validated_data.get('email')
        user = User.objects.get(email=email)
        user.create_activation_code()
        user.save()
        forgot_password_email.delay(user.activation_code, email)


class ForgotPasswordCompleteSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    code = serializers.CharField(min_length=8, required=True)
    password = serializers.CharField(required=True, min_length=6)
    password_confirm = serializers.CharField(required=True, min_length=6)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь не зарегистрирован')
        return email

    def validate_code(self, code):
        if not User.objects.filter(activation_code=code).exists():
            raise serializers.ValidationError('Пользователь не зарегистрирован')
        return code

    def validate(self, attrs):
        pass1 = attrs.get('password')
        pass2 = attrs.get('password_confirm')
        if pass1 != pass2:
            raise serializers.ValidationError('Пароли не совпадают')
        return attrs

    def set_new_pass(self):
        email = self.validated_data.get('email')
        password = self.validated_data.get('password')
        user = User.objects.get(email=email)
        user.set_password(password)
        user.activation_code = ''
        user.save()
